# Questions ouvertes

Ce qui reste à décider ou à approfondir.

## Conception

- [ ] **Grille détaillée des poses** : yeux, bouche, sourcils, orientation, accessoire pour chaque pose ([POSES.md](POSES.md)).
- [ ] **Voix** : nombre de voix par genre, caractère précis, état de l'art de la synthèse locale en français ([VOIX.md](VOIX.md)).
- [ ] **Premier personnage** à réaliser.
- [ ] **Expressions sonores** de chaque personnage.
- [ ] **Personnages saisonniers** : liste détaillée.
- [ ] **Zones interdites** : faut-il en ajouter d'autres que la banque ?

## Technique

- [ ] **Langage** : Kotlin natif (recommandé pour le launcher, le service d'accessibilité, la bulle et l'écoute continue) ou autre.
- [ ] **Modèle de langage local** : lequel, quelle taille, quelle bibliothèque (pistes : MediaPipe, modèles GGUF).
- [ ] **Reconnaissance vocale locale** : laquelle.
- [ ] **Synthèse vocale locale** : Piper ou autre.
- [ ] **Mot de réveil** : moteur de détection local.
- [ ] **Compatibilité téléphones anciens** (exemple : Galaxy S8) : Bob complet pour les récents, Bob allégé pour les anciens ? Comment alléger sans faire sortir de données ?
- [ ] **Identifiants sensibles** : stockage chiffré local.
- [ ] **Trace du consentement** : format et stockage de la note datée.
- [ ] **Isolation de la voix** dans le bruit ambiant.
- [ ] **API Google** : ce qui transite exactement, et comment le présenter honnêtement à l'utilisateur.

## Projet

- [ ] Vérifier la disponibilité du nom **Bob's Hands** directement sur le Play Store.
- [ ] Choisir une **licence** pour le dépôt.
- [ ] Moyen de recevoir les **dons**.
