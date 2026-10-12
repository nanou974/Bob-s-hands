# Capacités de Bob

## Les mains

Bob dispose d'un accès large, quasi total, au téléphone :

| Famille | Exemples |
|---|---|
| **Navigation et gestes** | Ouvrir une appli, revenir en arrière, faire défiler, toucher un bouton |
| **Saisie de texte** | Écrire un message, rédiger un mail, remplir un champ |
| **Fichiers** | Chercher un fichier dans un dossier et l'afficher |
| **Applis tierces** | Agir dans n'importe quelle appli (messagerie, YouTube, musique…) |
| **Contrôle système** | Volume (par exemple pendant une vidéo), luminosité, réglages |
| **Lecture à voix haute** | Mails, messages, notifications, contenu d'une page |

### Services Google : un modèle mixte

- Pour **Gmail, Agenda, Contacts, Drive** : passer par les **API Google**, plus rapides et plus fiables que de « cliquer » à l'écran.
- Pour les applis sans API : passer par **les mains** (le service d'accessibilité).

## Les yeux : lire l'écran

Deux mécanismes combinés :

1. **L'arbre d'accessibilité Android** — la structure invisible qui décrit boutons, textes et rôles. La voie royale : fiable, légère, locale, gratuite. Limite : inefficace sur une appli mal étiquetée.
2. **L'analyse visuelle** — capture d'écran + reconnaissance de texte (OCR) + petit modèle de vision. **En renfort uniquement**, quand l'arbre ne suffit pas.

**Règles sur les captures :**
- temporaires et jetables : analysées en mémoire vive puis **immédiatement détruites**, jamais écrites sur le disque ;
- analysées **en local sur le téléphone**, jamais envoyées dans le cloud.

### Décrire l'écran

- **Hiérarchisée** : une phrase de contexte d'abord (« on est sur ta boîte mail, tu as cinq messages »), le détail ensuite si on le demande.
- **Orientée action** : « tu peux répondre, archiver ou supprimer » plutôt que « il y a un bouton bleu en bas ».
- **Mémoire contextuelle** : Bob comprend « clique sur le bouton bleu », « celui du milieu ».

### Retour vocal pendant l'action

Bob raconte ce qu'il fait pour qu'on le suive sans regarder : « j'ouvre les réglages… je descends… j'y suis ».

## Les mails et le spam

- Bob lit, résume, répond, archive, supprime (avec confirmation).
- Le dossier spam est accessible comme un autre. Bob ne réinvente pas le filtre de Gmail, mais il peut :
  - repérer un vrai message tombé à tort dans les indésirables ;
  - aider à vider le dossier ;
  - **alerter sur les arnaques** : « attention, ce mail réclame ta carte bancaire, c'est louche ».

## Les yeux dans le monde : la caméra

Fonctions pensées d'abord pour les personnes aveugles et malvoyantes :

| Fonction | Exemples |
|---|---|
| **Couleurs** | « De quelle couleur est ce pull ? » — autonomie vestimentaire |
| **Lecture** | Courrier papier, étiquettes, **notices et boîtes de médicaments**, dates de péremption, menus |
| **Description** | « Qu'est-ce qu'il y a devant moi ? », décrire une photo envoyée par la famille |
| **Identification** | Objets, produits, **billets de banque** |
| **Orientation** | Panneaux, numéro de bus, noms de rue |

### Choix de la caméra à la voix

- **Arrière** : le monde, les objets, le courrier.
- **Avant** : se regarder soi (coiffure, tenue avant une visite — une question de dignité).

Bob peut proposer la caméra adaptée, la personne garde le dernier mot.

### Exemple de référence

> « Bob, prends-moi un selfie et envoie-le à ma fille. »

1. Bob ouvre la caméra avant.
2. Il guide le cadrage à la voix : « recule un peu », « tourne-toi vers la lumière », « c'est bon, je prends ».
3. Il sait que « ma fille », c'est Marie (mémoire des personnes).
4. Double confirmation, puis envoi.

Aucune routine programmée : l'enchaînement naît de la compréhension du langage.
