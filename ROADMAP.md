# Feuille de route

Bob est un projet ambitieux : launcher Android complet, IA locale, service d'accessibilité, bulle flottante, synthèse vocale, API Google. La règle est donc simple : **avancer par petits pas**, et toujours avoir un Bob qui marche, même tout petit.

---

## Phase 0 — Conception fonctionnelle ✅ (en grande partie terminée)

- [x] Vision, public, besoins réels
- [x] Nom et mot de réveil (« Bob », « Hey Bob »)
- [x] Personnalité, humeur, signaux non verbaux
- [x] Launcher, bulle, personnages, système de poses fixes
- [x] Capacités (mains, yeux, caméra)
- [x] Mémoire, sécurité, vie privée, consentement
- [x] Notifications et modes de silence
- [x] Modèle économique
- [ ] Grille détaillée des poses (yeux, bouche, sourcils, orientation) — voir [docs/POSES.md](docs/POSES.md)
- [ ] Choix des voix (caractère, nombre, genres)
- [ ] Liste des personnages saisonniers

## Phase 1 — L'atelier

- [ ] Installer l'environnement de développement Android sur JARVIS PC
- [ ] Installer et configurer Claude Code sur JARVIS PC, relié à ce dépôt
- [ ] Trancher le langage (Kotlin natif recommandé)
- [ ] Première appli « Hello Bob » installée sur le Pixel 10A

## Phase 2 — Le plus petit Bob qui marche

Objectif : prouver la chaîne de base, rien de plus.

- [ ] Un launcher minimal qui affiche **une** image de Bob au centre
- [ ] Le glissement vers le haut ouvre le tiroir d'applications Android normal
- [ ] Bob se réveille au mot « Bob » (écran allumé, téléphone branché)
- [ ] Bob comprend « ouvre [nom d'appli] » et l'ouvre
- [ ] Bob répond avec une voix de synthèse locale

## Phase 3 — Les mains

- [ ] Service d'accessibilité : lire l'arbre de l'écran
- [ ] Gestes : toucher, faire défiler, revenir, accueil
- [ ] Saisie de texte
- [ ] Commande « stop / annule »
- [ ] Double confirmation des actions sensibles
- [ ] Verrou de la zone interdite bancaire
- [ ] Retour vocal pendant l'action (« j'ouvre les réglages… j'y suis »)

## Phase 4 — Le cerveau local

- [ ] Choisir et intégrer un modèle de langage local
- [ ] Reconnaissance vocale locale
- [ ] Réglage de la patience d'écoute
- [ ] Schéma lister → numéroter → choisir → agir

## Phase 5 — Les yeux

- [ ] Description hiérarchisée et orientée action de l'écran
- [ ] Lecture des mails, messages, notifications
- [ ] Analyse visuelle locale en renfort (OCR, petit modèle de vision)
- [ ] Caméra : lecture de documents, couleurs, objets, billets, selfie guidé

## Phase 6 — La mémoire

- [ ] Mémoire longue persistante et locale
- [ ] Historique consultable à la voix
- [ ] Mémoire des personnes

## Phase 7 — L'âme

- [ ] Personnage avec poses fixes expressives (planche de sprites, calques)
- [ ] Changement de pose synchronisé avec le sens de ce que Bob dit
- [ ] Bulle flottante par-dessus les autres applis
- [ ] Détection d'humeur par les mots
- [ ] Humour, petits jeux vocaux, mimétisme
- [ ] Expressions sonores du personnage

## Phase 8 — L'accueil et la confiance

- [ ] Formulaire d'accueil, à la main ou mené à la voix par Bob
- [ ] Consentement vocal en deux validations, avec trace datée
- [ ] Notifications vocales et trois modes de silence
- [ ] Intégration API Google (Gmail, Agenda, Contacts, Drive)

## Plus tard

- Détection du ton de la voix, des rires, soupirs, bâillements, chuchotements
- Isolation de la voix de la personne dans le bruit ambiant
- Choix de plusieurs personnages, téléchargés à la demande
- Personnages saisonniers
- Compatibilité étendue aux téléphones anciens
- Publication sur le Play Store
