---
source_hash: eef50f1fe484ff2af95068f006064217adac902f902e7159b98801260bb5cb9a
---

# Clés et authentification

## Créer une clé

1. Ouvrez Hi, Moose et connectez-vous en tant que propriétaire du compte. Seul le propriétaire peut créer, voir et révoquer des clés.
2. Allez dans **Paramètres → Hi, Moose REST API**.
3. Donnez un libellé à la clé, choisissez les projets qu'elle peut lire (tous ou un seul), choisissez quand elle expire et cochez les permissions dont elle a besoin.
4. Cliquez sur **Créer la clé** et copiez la clé. Elle s'affiche une seule fois. Hi, Moose ne peut pas la réafficher ; si vous la perdez, révoquez-la et créez-en une nouvelle.

Les clés commencent par `hmk_live_` suivi de 64 caractères. Le tableau sous le formulaire liste chaque clé active avec ses permissions, sa date de création, sa dernière utilisation et son expiration. **Révoquer** arrête une clé immédiatement.

Hi, Moose ne conserve qu'un hachage de la clé, comme pour les mots de passe, donc personne chez Hi, Moose ne peut non plus relire une clé.

## Une clé par application

Créez une clé distincte pour chaque application ou script, avec un libellé qui dit à quoi elle sert. Une clé peut alors être révoquée sans rien casser d'autre, et la colonne **dernière utilisation** dans les Paramètres montre quelle application a fait les appels.

## Permissions

| Permission | Ce que la clé peut faire |
|---|---|
| Lire les données de visibilité | Tous les points d'accès `GET`. Toujours actif. |
| Gérer le suivi | Créer des projets, définir les termes de marque et les concurrents, ajouter, modifier et supprimer des prompts, définir les moteurs et la planification, enregistrer et supprimer des webhooks. |
| Lancer des analyses | Lancer une analyse de visibilité. Les analyses consomment le crédit du compte sur les moteurs cloud, donc n'accordez cette permission qu'à une clé qui en a besoin. |

Un appel sans la permission nécessaire répond `403 insufficient_scope` et nomme la permission. Choisissez les permissions à la création de la clé ; elles ne peuvent pas être modifiées ensuite. Créez plutôt une nouvelle clé.

Dans l'API, les permissions apparaissent sous la forme `visibility:read`, `tracking:write` et `runs:execute`, par exemple dans la réponse de `GET /me`.

## Accès aux projets

Une clé lit soit tous les projets du compte, soit un seul projet, au choix à la création de la clé. Un projet que la clé ne peut pas lire répond `404 not_found`, comme un projet qui n'existe pas, donc une clé ne permet pas de découvrir quels projets un compte possède.

## Authentification

Envoyez la clé comme jeton Bearer dans l'en-tête `Authorization` de chaque requête :

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La réponse indique la clé, ses permissions et les identifiants de projet qu'elle peut lire. C'est un bon premier appel pour vérifier qu'une clé fonctionne.

Une requête sans clé, ou avec une clé mal formée, révoquée ou expirée, répond `401` avec l'un de ces codes :

| Code | Signification |
|---|---|
| `invalid_key` | Pas d'en-tête `Authorization`, une clé au mauvais format, ou une clé que Hi, Moose ne connaît pas |
| `key_revoked` | La clé a été révoquée dans les Paramètres |
| `key_expired` | La clé a dépassé sa date d'expiration |

## Gardez la clé sur votre serveur

Utilisez la clé uniquement depuis votre propre serveur. L'API n'envoie aucun en-tête CORS, donc une page web ne peut pas l'appeler directement. Un tableau de bord dans le navigateur doit appeler votre backend, et votre backend appelle l'API. La clé reste ainsi hors de la page et hors du journal réseau du navigateur.

Stockez la clé dans une variable d'environnement ou un gestionnaire de secrets, jamais dans le dépôt de code. Si une clé fuite, révoquez-la dans les Paramètres et créez-en une nouvelle. La révocation prend effet immédiatement.

## Expiration

Une clé peut expirer après 30, 90 ou 365 jours, ou jamais. Une clé qui expire est le choix le plus sûr pour un script qui sera remplacé ; une clé sans expiration convient à un tableau de bord durable dont la clé vit dans un gestionnaire de secrets. Le tableau des Paramètres montre la date d'expiration de chaque clé.
