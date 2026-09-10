---
source_hash: 1c85ff53a55d4b6ecb7d8fbdd11b64ab53c6c37bdd4cb12540b5dc7616afc495
---
# Concurrents et Share of Voice

## À quoi cela sert

Répondre à la question à laquelle vos propres chiffres ne peuvent pas répondre : lorsqu'un assistant d'IA recommande quelque chose dans votre catégorie, à quelle fréquence s'agit-il de vous, et qui est choisi à votre place ?

Vous le trouverez dans **Visibility → Concurrence**.

## Configurer les concurrents

Ajoutez vos concurrents dans **Visibility → Settings → Competitor tracking**. Chacun demande un nom et, éventuellement, un site web.

Cette liste est partagée avec votre [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) : les concurrents ajoutés à l'un ou l'autre endroit apparaissent dans les deux.

Le nombre de concurrents suivis dans les exécutions de visibilité dépend de votre offre : **5 en Preview Mode et BYOK Free, 15 sur toutes les offres payantes**. L'écran de paramètres indique ce nombre et vous avertit si votre liste est plus longue, afin que vous sachiez que seuls les premiers sont suivis.

Trois à cinq concurrents réels fonctionnent mieux qu'une longue liste. Ce sont les marques auxquelles on vous compare véritablement, pas l'ensemble du secteur.

## Share of Voice

Le **Share of Voice** correspond à la part d'attention que chaque marque obtient dans les réponses d'IA sur la période, mais toutes les mentions ne se valent pas.

Être cité en premier dans une réponse vaut plus qu'être cité en sixième, car c'est ce nom-là que le lecteur retient. Chaque mention est donc pondérée selon la place qu'elle occupe dans la réponse :

| Position dans la réponse | Poids |
|---|---|
| 1re | 1,00 |
| 2e | 0,70 |
| 3e | 0,50 |
| 4e | 0,35 |
| 5e | 0,25 |
| 6e ou au-delà | 0,15 |

Une mention dont la position n'a pas pu être déterminée compte pour 0,50. À cela s'ajoute 0,50 lorsque la réponse **cite le site de la marque**, une citation étant un signal plus fort qu'une simple mention.

Le score pondéré de chaque marque est ensuite divisé par le total de toutes les marques suivies pour donner sa part.

L'onglet Competition affiche en tête votre rang (« You are 3rd ») et la liste classée en dessous présente chaque marque suivie avec sa part. À côté figurent la **part de mentions** et la **part de citations**, les comptages bruts non pondérés, pour que vous puissiez comparer l'image brute et l'image pondérée.

!!! note "Pourquoi le chiffre pondéré peut contredire le comptage brut"
    Vous pouvez être mentionné aussi souvent qu'un concurrent et rester derrière lui au Share of Voice, s'il arrive systématiquement en premier et vous en quatrième. C'est précisément l'intérêt de cette mesure : elle vous dit que les mentions sont là mais pas la proéminence, ce qui est un autre problème et appelle une autre réponse.

!!! warning "Le Share of Voice n'est pas le Mention Rate"
    Ce sont deux chiffres distincts qui évoluent indépendamment.

    Le **Share of Voice** est votre part pondérée de l'attention totale accordée aux marques. Il est concurrentiel : un concurrent peut le faire baisser sans que rien ne change de votre côté.

    Le **Mention Rate** (dans l'onglet Overview) est la proportion de prompts surveillés où votre marque a été mentionnée. Il est absolu, non pondéré, et ignore totalement les concurrents.

    Votre Mention Rate peut monter pendant que votre Share of Voice baisse, si les concurrents ont progressé plus vite que vous. Les deux méritent d'être suivis, pour des raisons différentes.

## Tendance du Share of Voice

Le graphique de tendance représente le **Share of Voice** ou le **Taux de mention** dans le temps, pour voir si une évolution vient de votre progression, de celle d'un concurrent, ou d'une catégorie devenue globalement plus bruyante.

## Top Competitor Citations

Quelles pages concurrentes les moteurs d'IA citent réellement comme sources. C'est le panneau le plus directement actionnable de l'onglet : ce sont les URL précises qui remportent les citations que vous visez, et elles indiquent ce que les moteurs de réponse considèrent aujourd'hui comme la meilleure source sur ces questions.

Comparez-le à **Pages les plus citées** dans l'onglet Overview, qui montre la même chose pour votre propre domaine.

## Competitor Gaps

Les questions pour lesquelles un concurrent est apparu dans une réponse d'IA et pas votre marque.

Chaque écart indique quels concurrents sont apparus et dans quels moteurs, avec une étiquette :

- **Aucune visibilité** : votre marque n'apparaît pour cette question dans aucun moteur.
- **Partiel** : votre marque apparaît bien pour cette question, mais pas dans tous les moteurs. La ligne précise dans lesquels vous apparaissez.

Les lignes partielles ne nécessitent souvent aucune action. Une question où vous apparaissez dans quatre moteurs sur cinq n'est pas le même problème qu'une question où vous n'apparaissez nulle part, et l'étiquette est là pour vous permettre de les distinguer d'un coup d'œil.

Si la liste est tronquée, resserrez la plage de dates ou les filtres pour voir le reste.

## D'où viennent les données concurrentielles

Les mentions et citations de concurrents sont extraites des mêmes observations d'exécutions de visibilité que les vôtres. Rien de supplémentaire n'est exécuté et aucune exploration distincte des sites concurrents n'a lieu pour ces panneaux. Si une exécution a échoué ou qu'un modèle était indisponible, ces observations sont exclues plutôt que comptées comme une absence.

## Dans le rapport exécutif

Le Share of Voice, les principales citations de concurrents et les écarts sont tous inclus dans le [rapport exécutif](overview.md#exporter) exporté : le panorama concurrentiel parvient donc aux clients et aux décideurs sans que vous ayez à le reconstituer à la main.
