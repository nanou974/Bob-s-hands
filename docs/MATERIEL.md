# Matériel et installation

## Le socle : un téléphone toujours branché, sur un support fixe

Une personne paralysée **ne peut ni brancher ni débrancher son téléphone**. Gérer la batterie au fil de la journée n'a donc aucun sens pour elle.

Installation type, faite **une fois pour toutes par un aidant** :
- le téléphone sur un **support fixe** (bras articulé au-dessus du lit, pied près du fauteuil) ;
- **branché en permanence** sur le secteur ;
- option développeur Android **« Rester activé » (Stay awake)** : l'écran ne se met pas en veille pendant la charge.

Conséquences :
- l'oreille de Bob tourne **en continu**, sans souci de consommation ;
- le visage de Bob reste **affiché en permanence** ;
- pas besoin de puce dédiée basse consommation ni de lutter contre les optimisations de batterie d'Android.

## Le réveil vocal

Exigence forte : dire **« Bob »** ou **« Hey Bob »** doit réveiller l'assistant **à tout moment**. Sans cela, tout le reste est inutile pour quelqu'un qui ne peut pas toucher l'appareil.

« Bob » est un excellent mot de réveil : une syllabe franche, un B qui claque.

## Le bruit ambiant

Télévision, radio, conversations : Bob doit ne réagir qu'à la bonne personne. Pistes :
- le mot de réveil filtre déjà beaucoup ;
- réduction de bruit et annulation d'écho ;
- idéalement, apprendre **la voix de la personne** pour ne réagir qu'à elle (possible puisque Bob est mono-utilisateur).

## Appareils visés

- **Appareil de développement** : Google Pixel 10A.
- **Objectif de compatibilité** : le plus large possible, y compris des téléphones anciens (exemple : Samsung Galaxy S8, 2017), car le public a souvent un appareil ancien ou donné par un proche.

**Tension à arbitrer** : l'IA locale (langage, vision, voix) demande de la puissance. Sur un téléphone ancien, les parties lourdes risquent de ne pas tourner. Pistes envisagées : un Bob complet pour les appareils récents et un Bob allégé pour les anciens. La façon de le faire sans renoncer au « rien ne sort » reste à trancher (voir [QUESTIONS_OUVERTES.md](QUESTIONS_OUVERTES.md)).

Les choix déjà faits allègent la charge : poses fixes au lieu d'animations, planches de sprites, arbre d'accessibilité avant l'analyse visuelle.

## Atelier de développement

- **JARVIS PC** (Windows) avec Claude Code, relié à ce dépôt.
- Le téléphone est la cible où l'on installe et teste.
