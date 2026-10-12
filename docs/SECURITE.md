# Sécurité

La personne ne peut pas rattraper une erreur d'un geste. La sécurité de Bob repose donc sur la prévention.

## Double confirmation en deux temps

Obligatoire avant toute action sensible : **envoyer, supprimer, publier, acheter, partager**.

Exemple pour une suppression :

| Étape | Bob | Personne |
|---|---|---|
| Ordre | | « Supprime le trois. » |
| 1er temps — reformulation | « Tu veux supprimer le mail de la banque, tu es sûr ? » | « Oui. » |
| 2e temps — confirmation | « Tu confirmes la suppression de ce mail ? » | « Oui, je confirme. » |
| Action | « C'est supprimé. » | |

**Les deux questions sont formulées différemment**, pour éviter le « oui, oui » machinal.

## Le frein d'urgence

« **Stop** » ou « **annule** » arrête Bob immédiatement, en pleine action.

## Zone interdite par conception : la banque

Bob **ne touche jamais** aux applications bancaires ni aux comptes bancaires. Ni lecture, ni saisie, ni ouverture.

- Ce n'est pas un réglage : c'est un **verrou de conception**, impossible à désactiver.
- Raisons : risque maximal et irréversible ; principale porte d'entrée des arnaques visant un public vulnérable.
- Argument de confiance : *« Bob ne touchera jamais à votre argent, c'est verrouillé dans sa conception. »*

La liste des zones interdites reste ouverte si d'autres cas se présentent.

## Protection contre les arnaques

Bob alerte quand un message semble frauduleux (demande de carte bancaire, d'identifiants, urgence suspecte).

## Identifiants sensibles

Certains services (exemple : l'espace Ameli) demandent identifiant, mot de passe et code reçu par SMS ou mail. Bob peut lire le code et le saisir lui-même, mais stocker des identifiants impose qu'ils soient **chiffrés et strictement locaux**. Le mécanisme reste à concevoir (voir [QUESTIONS_OUVERTES.md](QUESTIONS_OUVERTES.md)).
