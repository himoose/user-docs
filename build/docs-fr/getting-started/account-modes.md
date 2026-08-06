---
source_hash: 807f4fd0f8157bf27491590b13dd7b2b18f5cb12dd648c025f2c46cabf3ea0ed
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/getting-started/account-modes/)

# Types de compte et forfaits

Hi, Moose exécute le travail d'IA de deux façons : avec votre propre clé OpenRouter (BYOK) ou avec les modèles gérés de Hi, Moose. C'est ce choix, et non le prix, qui constitue la véritable ligne de partage. Tout le reste n'est qu'une question de nombre de projets, de sièges et de crédits mensuels.

Les forfaits sont regroupés en deux onglets dans l'écran **Upgrade** : **Startup** et **Enterprise & Agencies**.

## Les deux façons d'exécuter l'IA

### BYOK : apportez votre propre clé

Vous fournissez une clé d'API [OpenRouter](https://openrouter.ai) et les appels aux modèles s'exécutent **depuis l'application de bureau, sur votre machine**, avec cette clé. Hi, Moose ne fait jamais transiter l'inférence BYOK par ses propres serveurs : votre clé et vos prompts restent en local.

Payer un forfait BYOK n'y change rien. Vous payez pour davantage de capacités de travail (projets, sièges, mémoire, workflows, Search Console), pas pour que Hi, Moose exécute vos appels aux modèles. Le coût des modèles est réglé directement à OpenRouter et il n'y a aucun compteur de jetons Hi, Moose à surveiller.

### Géré : Hi, Moose exécute les modèles

Aucune clé d'API. Les modèles gérés de Hi, Moose font le travail et vous consommez un solde mensuel de **crédits**. Un seul compteur, et non plusieurs. La prise en charge des modèles locaux reste disponible en option, sur l'appareil, sur tous les forfaits gérés.

## Forfaits Startup

### Preview Mode (gratuit)

Preview Mode est la façon gratuite d'essayer Hi, Moose. Il est réellement local : 1 projet, 1 siège, stockage local et exécutions de visibilité qui interrogent les surfaces publiques de recherche par IA directement depuis votre appareil.

- 1 projet, 1 siège utilisateur
- Uniquement les LLM gratuits et locaux
- Exécutions de visibilité locales
- Stockage et rappel du contexte, Brand Voice et guide de style
- Connexions : WordPress, Webflow, Grav
- Données de recherche en direct et de concurrence limitées, qualité d'IA limitée, options d'export limitées

!!! warning "Preview Mode nécessite un modèle local pour le scoring et les audits"
    Preview Mode ne comprend aucune allocation d'IA dans le cloud. Les [AEO audits](../features/aeo-audits.md) ainsi que le scoring de sentiment, de narratif et de parité fonctionnelle des [exécutions de visibilité](../visibility/overview.md) ne fonctionnent qu'une fois un modèle local Gemma 4 activé dans **Paramètres → Local Model**. Tant qu'aucun modèle n'est actif, ces vérifications sont ignorées plutôt qu'exécutées dans le cloud.

### BYOK Free

La façon gratuite de travailler avec votre propre clé. Même format à 1 projet et 1 siège que Preview Mode, mais avec accès à tous les modèles proposés par OpenRouter et non aux seuls modèles gratuits.

- 1 projet, 1 siège utilisateur
- Votre propre clé OpenRouter, jetons illimités
- Tous les LLM, y compris les modèles locaux
- Exécutions de visibilité en local uniquement
- Connexions : WordPress, Webflow, Grav
- Stockage et rappel du contexte limités, [Library](../library/overview.md) limitée
- Pas de recherche web dans le chat, pas de Workflows, pas de Google Search Console

### BYOK Premium : 39 USD par mois ou 390 USD par an

Le forfait local complet, et le moment où les sièges d'équipe et le planificateur se débloquent.

- 3 projets, plus des projets supplémentaires à 10 USD par mois chacun
- Jusqu'à 10 sièges d'équipe
- Exécutions de visibilité complètes avec planificateur personnalisé
- Recherche web depuis le chat
- Stockage et rappel du contexte complets, [Library](../library/overview.md) complète
- [Workflows](../workflows/overview.md)
- Brand Voice, guide de style et [Brand Truth Profile](context/brand-truth-profile.md)
- Connexions : WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [générations audio](../audio/overview.md) par mois

### Forfaits gérés

Les trois fonctionnent avec les modèles de Hi, Moose et comprennent des sièges d'équipe illimités, des générations audio illimitées, la journalisation et l'export pour les administrateurs, ainsi qu'un stockage local et cloud.

| Forfait | Prix | Projets | Crédits mensuels | Modèles |
|---|---|---|---|---|
| Standard | 79 USD/mois ou 849 USD/an | 3 | 1 700 000 | Modèles standard, plus locaux |
| Professional | 129 USD/mois ou 1 389 USD/an | 5 | 3 000 000 | Tous les modèles, plus locaux |
| Premium | 249 USD/mois ou 2 689 USD/an | 10 | 6 000 000 | Tous les modèles, plus locaux |

## Forfaits Enterprise et agences

### BYOK Agency : 149 USD par mois ou 1 490 USD par an

BYOK Premium à l'échelle d'une agence. Le même fonctionnement local et le même ensemble de fonctionnalités, dimensionnés pour gérer de nombreux clients.

- 25 projets, plus des projets supplémentaires à 10 USD par mois chacun
- Jusqu'à 25 sièges d'équipe
- 15 générations audio par mois
- [Marque blanche](../agency/white-label.md) sur les rapports et les intégrations audio, comme sur tous les forfaits payants

### Forfaits gérés pour agences

| Forfait | Prix | Projets | Crédits mensuels | Stockage |
|---|---|---|---|---|
| Agent Core | 449 USD/mois ou 4 849 USD/an | 25 | 15 000 000 | Cloud d'équipe |
| Agent Studio | 999 USD/mois ou 10 789 USD/an | 75 | 40 000 000 | Cloud d'équipe |
| Agent Scale | 1 999 USD/mois ou 21 589 USD/an | Illimités | 120 000 000 | Cloud d'équipe |

## Comparatif rapide

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Forfaits gérés |
|---|---|---|---|---|---|
| Clé d'API personnelle requise | Non | Oui | Oui | Oui | Non |
| Où s'exécute l'inférence | Sur votre appareil | Sur votre appareil | Sur votre appareil | Sur votre appareil | Cloud Hi, Moose (local en option) |
| Projets | 1 | 1 | 3 | 25 | De 3 à illimités |
| Sièges d'équipe | 1 | 1 | 10 | 25 | Illimités |
| Recherche web dans le chat | Non | Non | Oui | Oui | Oui |
| [Workflows](../workflows/overview.md) | Non | Non | Oui | Oui | Oui |
| [Google Search Console](../integrations/google-search-console.md) | Non | Non | Oui | Oui | Oui |
| [Audio](../audio/overview.md) | Non | Non | 15 par mois | 15 par mois | Illimité |
| [Marque blanche](../agency/white-label.md) | Non | Non | Oui | Oui | Oui |

## Sièges, projets et crédits

Les **projets supplémentaires** coûtent 10 USD par mois chacun sur tous les forfaits payants. Ajoutez-les ou retirez-les depuis **Upgrade → Extra projects**.

Les **sièges** constituent la véritable frontière entre gratuit et payant. Preview Mode et BYOK Free sont limités au titulaire du compte. BYOK Premium autorise jusqu'à 10 sièges, BYOK Agency jusqu'à 25, et les forfaits gérés sont illimités, car tous les membres consomment le solde de crédits du titulaire.

Les **recharges de crédits** sont disponibles sur les forfaits gérés lorsque vous êtes à court en cours de mois :

- 500 000 crédits pour 25 USD
- 2 500 000 crédits pour 100 USD

Les recharges sont des achats ponctuels, pas des abonnements. Elles ne sont consommées qu'une fois vos crédits mensuels épuisés et n'expirent jamais.

!!! note "Les écoutes audio sont comptabilisées séparément"
    Tous les forfaits comprenant l'audio incluent également les 10 000 premières écoutes pour l'ensemble du compte. Au-delà, les écoutes sont facturées 5,00 USD par tranche de 10 000 par mois. Sur les forfaits gérés, la *génération* audio consomme également votre solde de crédits.

## Codes promotionnels

Si vous disposez d'un code de réduction, saisissez-le au moment du paiement depuis l'écran **Upgrade**.

## Changer de forfait

Vous pouvez changer de forfait à tout moment depuis **Paramètres → Compte** ou depuis l'écran **Upgrade**. Si vous passez d'un forfait géré à un forfait BYOK, ajoutez d'abord votre clé d'API OpenRouter. Hi, Moose valide la clé avant d'y basculer le routage de l'IA.

Votre clé OpenRouter est enregistrée par compte et non par appareil : elle vous suit lors d'une nouvelle installation.
