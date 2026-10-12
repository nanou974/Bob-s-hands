# Apparence : launcher, bulle et personnages

## Le launcher

*Bob's Hands* **remplace l'écran d'accueil Android**. Au centre, en grand, Bob incarné par son personnage (référence : la voiture de l'Inspecteur Gadget, grosse tête au milieu).

La grille d'icônes classique ne sert à rien à quelqu'un qui ne touche pas l'écran. Ici, tout se passe sur ce bureau : la personne a Bob sous les yeux en permanence.

**Accès classique préservé** : un glissement vers le haut ouvre le tiroir d'applications Android normal, pour les proches, aidants et soignants.

## La bulle flottante

Quand une autre appli est ouverte, Bob reste présent sous forme d'une **bulle flottante** (façon bulles Messenger) qui affiche son expression et sert de point de contrôle.

Launcher et bulle sont les deux faces d'une même idée : Bob en grand sur l'accueil, Bob réduit partout ailleurs.

## Les poses fixes : une bande dessinée vivante

**Décision clé : pas d'animation fluide.** Bob fonctionne par **poses fixes expressives qui se succèdent**, comme les cases d'une bande dessinée.

Bob tient une expression, puis **bascule** d'un coup sur une autre au moment juste. Exemple : il lit un mail avec un visage neutre ; arrive une phrase intrigante, il passe au sourcil levé ; une nouvelle triste, il passe au visage peiné. Chaque changement souligne le sens de ce qu'il dit, comme un conteur qui change de visage.

Avantages :
- **très expressif** ;
- **quasi gratuit en ressources** : afficher une image fixe ne coûte presque rien, même sur un vieux téléphone ;
- une **signature visuelle** propre à Bob, avec du caractère.

L'intelligence est dans le **timing** : Bob choisit la pose selon le ton de ce qu'il dit et l'humeur de la personne.

La liste des poses est dans [POSES.md](POSES.md).

## Fabrication des personnages

Pour ne pas crouler sous des centaines d'images :

### Planches de sprites

Chaque personnage tient sur **une planche** (sprite sheet) : une seule image qui contient tous ses morceaux et expressions. Le programme vient piocher la zone qui l'intéresse. Une planche par personnage se charge une fois et s'affiche instantanément.

### Calques

Le visage est découpé en **calques**, comme dans Photoshop :
- la tête (fond) ;
- les yeux ;
- les sourcils ;
- la bouche ;
- les accessoires (mains, porte-voix…).

On compose une expression en superposant les bons morceaux. Avec quelques pièces, on obtient beaucoup d'expressions.

### Calques rattachés à une structure

Pour les **orientations de tête** (penchée, en haut, en bas), les calques sont rattachés à une même structure : quand la tête pivote, yeux, bouche et sourcils pivotent **ensemble** sans se décaler. C'est la technique des dessins animés modernes (type Live2D).
Alternative plus simple : dessiner directement certaines orientations comme des poses à part.

Les fichiers sont rangés dans [`assets/pictures/`](../assets/pictures/).

## Les personnages (24 styles)

| Famille | Personnages |
|---|---|
| **Sympathiques** | Petit robot, chat, chien, hibou, petit fantôme, goutte, bulle à visage |
| **Visages expressifs** | Visage de dessin animé, bonhomme rond style emoji, avatar manga |
| **Futuristes** | Tête holographique, sphère lumineuse, œil d'IA, noyau d'énergie, **interface JARVIS à cercles concentriques** |
| **Doux, abstraits** | Forme géométrique, petite flamme, visage minimaliste |
| **Enfants, ados** | **Voiture cartoon avec les phares en guise d'yeux**, petit dinosaure, personnage pixel art rétro, mascotte animale, petit monstre gentil, super-héros miniature |

### Manies propres à chaque personnage

Chaque personnage a ses petites manies au repos, en poses fixes : le robot cligne ou se dévisse la tête, le chat se lèche la patte ou bâille, la voiture fait clignoter ses phares, JARVIS fait tourner ses cercles, le hibou tourne la tête, la flamme vacille, le dinosaure se dandine. Un personnage figé serait mort.

### Personnages saisonniers

Occasionnels, proposés et jamais imposés : lapin ou œuf à Pâques, sapin ou bonhomme de neige à Noël, citrouille à Halloween… Liste à compléter.

### Choisir son personnage

À la voix, par numéro : « montre-moi les personnages » → « je prends le 3 ». Bob demande d'abord si la liste doit être dite ou affichée.

## Maîtriser la quantité de travail

- **Commencer par un seul personnage**, bien fait, avec ses poses de base. Enrichir ensuite.
- Le personnage est **indépendant de la voix** : pas de « chat masculin » et « chat féminin ».
- À terme, n'installer qu'un ou deux personnages et **télécharger les autres à la demande**.
