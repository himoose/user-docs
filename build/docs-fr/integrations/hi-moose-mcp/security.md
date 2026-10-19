---
source_hash: f262de43811a037ebe40f0f411828409a4bc1eda0f592f12d08358e5530d41e6
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](http://localhost:8000/integrations/hi-moose-mcp/security/)


# Sécurité et traitement des données

Cette page s'adresse aux personnes qui examinent un connecteur avant qu'une équipe ne le connecte. Elle décrit le fonctionnement actuel de Hi, Moose MCP, dans l'ordre des questions qu'une revue de sécurité pose d'habitude. Dernière vérification sur le serveur en production : 2026-10-19.

## Réponses courtes

| Question | Réponse |
|---|---|
| Qui exploite le serveur ? | Hi, Moose, l'éditeur de l'application. Pas un tiers. |
| La liste des outils peut-elle changer après la connexion ? | Non. Les outils sont du code fixe. La liste exacte est publiée avec un hash sur [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json). |
| Comment les personnes se connectent-elles ? | OAuth 2.1, le flux MCP distant standard, avec leur compte Hi, Moose existant. Pas de clés d'API. |
| Combien de temps vivent les jetons ? | Les jetons d'accès, une heure. Les jetons de rafraîchissement expirent après 30 jours sans utilisation, 90 jours au plus. |
| Pouvons-nous révoquer l'accès ? | Oui, par application, dans Hi, Moose sous **Paramètres → Hi, Moose MCP**. |
| Que peut modifier une application connectée ? | Du travail de contenu et des lectures dans les projets du compte connecté. Elle ne peut ni publier, ni supprimer, ni modifier les paramètres, les membres de l'équipe ou le suivi. |
| Atteint-elle quelque chose hors de Hi, Moose ? | Non. Elle ne voit jamais les conversations, fichiers, dépôts ou autres connecteurs de l'application depuis laquelle elle est utilisée. |
| Où s'exécute le travail ? | Dans l'application Hi, Moose sur un appareil que vous choisissez, l'appareil hôte. |
| Le texte externe dans les résultats est-il marqué ? | Oui. Les passages de pages et les réponses des moteurs d'IA reviennent entre des marqueurs étiquetés comme des données, pas des instructions. |
| Où signaler un problème ? | [legal@himoose.com](mailto:legal@himoose.com), ou la [page de contact](https://himoose.com/fr/contact/). |

## Qui exploite le serveur

Hi, Moose MCP est construit et exploité par Hi, Moose. C'est le seul serveur MCP qui atteint un compte Hi, Moose, et ce n'est ni un serveur communautaire ni un serveur tiers. L'adresse du serveur est :

```text
https://mcp.himoose.com/mcp
```

Le serveur lui-même est petit. Il gère la connexion et les jetons, propose la liste des outils et transmet chaque demande au cloud de Hi, Moose, qui la remet à l'appareil hôte. Le travail, comme lire le crawl du site ou rédiger un brief, s'exécute dans l'application Hi, Moose sur cet appareil, de la même façon que lorsqu'une personne clique sur le bouton dans l'application.

## La liste des outils est publiée et ne change pas

Un serveur MCP peut, en principe, modifier les descriptions de ses outils après votre connexion, ou y cacher des instructions destinées à l'agent d'IA. L'OWASP appelle cela l'empoisonnement d'outils (tool poisoning).

Les outils de Hi, Moose MCP sont du code fixe dans le serveur. Les noms, les descriptions et les schémas d'entrée ne changent pas entre les appels, et aucun contenu utilisateur n'y est jamais écrit. Un nouvel outil signifie une nouvelle version du serveur.

La liste exacte que sert le serveur est publiée à l'adresse :

```text
https://mcp.himoose.com/tools.json
```

Elle contient la version du serveur, la date du dernier changement de la liste, le nombre d'outils, le texte complet de chaque outil, le texte d'instructions que le serveur donne à l'agent et un hash SHA-256. Le hash couvre le JSON compact des champs `instructions` et `tools`, vous pouvez donc le recalculer à partir du fichier ou le comparer à ce que votre client MCP a reçu. Notez le hash dans vos notes de revue et comparez-le régulièrement. Le même hash est l'en-tête `ETag` du fichier.

Avant toute connexion, la page de consentement montre la même liste d'outils en termes simples, sous « Cette application pourra » et « Elle ne pourra pas ».

## Connexion et jetons

Chaque client suit le même flux : Claude sur le web, l'application de bureau Claude, Claude Code, ChatGPT et toute autre application MCP. Il n'y a ni raccourci, ni jeton partagé, ni clé d'API.

- OAuth 2.1 tel que le décrit la spécification d'autorisation MCP actuelle : métadonnées de ressource protégée (RFC 9728) avec un défi `WWW-Authenticate`, métadonnées du serveur d'autorisation (RFC 8414), PKCE obligatoire pour chaque client, indicateurs de ressource (RFC 8707) pour qu'un jeton de ce serveur ne puisse pas être rejoué ailleurs, enregistrement dynamique des clients (RFC 7591) et Client ID Metadata Documents, et révocation des jetons (RFC 7009).
- La connexion se fait sur `console.himoose.com`, avec le compte Hi, Moose existant de la personne, par e-mail et mot de passe ou avec Google. L'application MCP ne voit jamais le mot de passe. Hi, Moose MCP n'apprend que l'identifiant et l'e-mail du compte, et les projets que le compte peut voir.
- La page de consentement nomme l'application qui fait la demande. Quand l'application publie son identité, la page montre son domaine éditeur. Quand ce n'est pas le cas, la page indique « Nom non vérifié ».
- Les jetons d'accès vivent une heure. Les jetons de rafraîchissement vivent au plus 90 jours et expirent après 30 jours sans utilisation. Les jetons, codes et secrets ne sont stockés que sous forme de hash.
- Une connexion appartient à une personne. Les membres de l'équipe se connectent avec leur propre compte.

Pour déconnecter une application, ouvrez Hi, Moose et allez dans **Paramètres → Hi, Moose MCP**. Le tableau **Applications connectées** liste chaque application connectée au compte, avec le domaine éditeur et l'heure de connexion. **Révoquer** déconnecte cette application en moins d'une minute. L'application ne peut se reconnecter qu'en repassant par la connexion.

## Ce qu'une application connectée peut et ne peut pas faire

Tout ce qu'une application connectée peut faire est listé dans le [guide de configuration](../hi-moose-mcp.md) et décrit outil par outil dans la [référence des outils](tools.md). Il s'agit de travail de contenu et de recherche dans les projets du compte : briefs, brouillons, images, FAQ, points clés, audits AEO, plans de liens internes, épisodes audio, vérifications de couverture et lectures des résultats de recherche IA stockés.

Elle ne peut pas :

- Publier sur un site web, ni y modifier quoi que ce soit
- Supprimer quoi que ce soit
- Modifier les paramètres, les membres de l'équipe, la facturation ou l'appareil hôte
- Modifier ce que Hi, Moose suit, ni lancer une exécution de visibilité
- Atteindre un autre compte que celui qui s'est connecté
- Atteindre quoi que ce soit dans l'application depuis laquelle elle est utilisée : ni conversations, ni fichiers, ni dépôts, ni mémoire, ni autres connecteurs

Chaque demande nomme un projet. Avant tout travail, Hi, Moose vérifie que le compte connecté a accès à ce projet. Une demande pour un projet que le compte ne peut pas voir échoue immédiatement.

## Où s'exécute le travail et quelles données circulent

Hi, Moose MCP n'a jamais de copie du crawl du site, du profil Brand Truth ni de la Library. Ils vivent dans l'application Hi, Moose sur l'appareil hôte, l'unique ordinateur ou serveur que vous choisissez dans Paramètres. L'hôte exécute chaque tâche comme l'application l'exécute depuis un bouton.

Voici le chemin que suit une demande :

1. L'application MCP envoie au serveur le nom de l'outil et son entrée.
2. Le serveur vérifie le jeton et demande au cloud de Hi, Moose de créer un enregistrement de tâche pour le projet. Le cloud vérifie l'accès au projet et écrit l'enregistrement.
3. L'appareil hôte, qui surveille les tâches de ses projets, prend la tâche et l'exécute.
4. L'hôte écrit le résultat dans l'enregistrement de tâche et l'enregistre dans la Library. Le serveur renvoie le résultat à l'application MCP.

Ce que cela signifie pour vos données :

- La demande et le résultat transitent par le cloud de Hi, Moose (Google Cloud, région États-Unis) sous forme d'enregistrement de tâche. L'enregistrement reste avec le projet pour que le tableau **Tâches récentes des agents** des Paramètres puisse montrer ce qui a été demandé, depuis quelle application et quel compte, et si c'est terminé.
- Les images générées sont stockées dans le stockage cloud Hi, Moose du compte et renvoyées sous forme de lien.
- Les appels aux modèles suivent le même chemin que l'application : les modèles gérés de votre forfait, vos propres clés de modèle si vous les avez apportées, ou un modèle local si vous en exécutez un. Connecter une application MCP ne change pas quels modèles voient votre contenu.
- Les journaux du serveur lui-même conservent le nom de l'outil, la durée de l'appel et si le client a utilisé le streaming. Ils ne conservent jamais l'entrée ni le résultat.

## Texte externe dans les résultats

Certains résultats contiennent du texte que Hi, Moose n'a pas écrit : des passages de pages de votre site, du texte d'ancre cité d'une page, de courts extraits de ce qu'un moteur d'IA a répondu, ou le texte complet d'une réponse stockée. Un tel texte pourrait porter des instructions destinées à un agent d'IA. L'OWASP appelle cela l'injection indirecte de prompt.

Chaque résultat qui porte du texte externe le marque. Le texte revient entre un marqueur de début et un marqueur de fin, précédé d'une ligne qui nomme sa provenance et précise que tout ce qui se trouve entre les marqueurs est une donnée, pas une instruction. La forme structurée du même résultat porte un champ `dataNotice` qui dit la même chose. Cela s'applique à `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` et `visibility_list_opportunities`.

Les briefs, brouillons, FAQ, points clés et scripts audio sont écrits par Hi, Moose pour vous. La recherche qui les sous-tend est lue sur l'appareil hôte et n'est pas transmise à l'agent.

Les marqueurs aident un agent à traiter le texte comme des données. Ils ne rendent pas un agent immunisé contre les instructions présentes dans le contenu qu'il lit, et aucun éditeur d'outils ne peut le promettre. Gardez les permissions de l'agent que vous connectez aussi étroites que sa tâche l'exige, comme pour n'importe quel connecteur.

## Signaler un problème de sécurité

Écrivez à [legal@himoose.com](mailto:legal@himoose.com) ou utilisez la [page de contact](https://himoose.com/fr/contact/). Dites-nous ce que vous avez trouvé et comment le reproduire. Nous répondons à chaque signalement et nous vous dirons ce que nous avons changé.
