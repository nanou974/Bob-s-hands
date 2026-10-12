# assets/pictures

Toutes les images de Bob's Hands : planches de sprites des personnages, calques, icônes.

## Organisation

```
assets/pictures/
├── characters/          Un dossier par personnage
│   └── <personnage>/
│       ├── sheet.png        La planche complète (sprite sheet)
│       ├── sheet.json       Coordonnées de chaque morceau dans la planche
│       └── layers/          Sources en calques séparés (tête, yeux, sourcils, bouche, accessoires)
├── seasonal/            Personnages saisonniers (Pâques, Noël, Halloween…)
├── ui/                  Éléments d'interface (bulle flottante, fonds, icônes)
└── branding/            Logo, icône de l'application, visuels du dépôt
```

## Conventions

- **Noms de fichiers** : minuscules, sans accents ni espaces, mots séparés par des tirets (`petit-robot`, `voiture-cartoon`).
- **Une planche par personnage** : tous les morceaux et expressions sur une seule image, rangés en grille.
- **Calques** : chaque élément du visage sur son calque (tête, yeux, sourcils, bouche, accessoires), pour recomposer les expressions et faire pivoter la tête d'un bloc.
- **Format** : PNG avec transparence.
- **Fichiers sources** (Photoshop, Krita, GIMP…) : dans `layers/`.

## Référence

La liste des poses à dessiner est dans [docs/POSES.md](../../docs/POSES.md), et le principe des poses fixes dans [docs/APPARENCE.md](../../docs/APPARENCE.md).
