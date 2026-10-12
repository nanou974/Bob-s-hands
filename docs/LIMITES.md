# Limites techniques connues

## Double authentification (code par SMS ou mail)

**Surmontable.** Bob sait lire les SMS et les mails : il peut récupérer le code et le saisir lui-même.
Pour les espaces en ligne (exemple : Ameli), cela suppose de stocker identifiant et mot de passe de façon **chiffrée et strictement locale**. Mécanisme à concevoir.

## CAPTCHA

**Le vrai mur.** Ils sont conçus précisément pour bloquer les programmes automatiques — une ironie d'accessibilité.

Stratégie : Bob **demande un coup de main ponctuel** plutôt que d'abandonner :
> « Là, il y a une vérification que je ne peux pas faire seul. Quelqu'un peut m'aider un instant ? »

Beaucoup de CAPTCHA modernes sont invisibles et ne se déclenchent pas.

## Applis mal étiquetées

L'arbre d'accessibilité ne suffit pas toujours. Renfort : analyse visuelle locale (OCR, petit modèle de vision), plus coûteuse en calcul.

## Puissance des modèles locaux

Les modèles qui tournent sur un téléphone sont plus légers, donc un peu moins « intelligents » que les gros modèles du cloud. Ils restent suffisants pour des tâches cadrées. Tension acceptée en échange de la gratuité et de la vie privée.

## Téléphones anciens

Voir [MATERIEL.md](MATERIEL.md).

## Bruit ambiant

Voir [MATERIEL.md](MATERIEL.md).
