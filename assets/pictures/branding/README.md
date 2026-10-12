# Identité visuelle de Bob's Hands

## Le logo officiel

| Fichier | Usage |
|---|---|
| `logo-monogramme.svg` / `.png` (1024 px) / `-512.png` | Symbole seul signé **BH** : icône d'application, photo de profil, favicon |
| `logo-horizontal.svg` / `.png` | Miroir + nom à droite : bannière GitHub, en-têtes, signatures |
| `logo-vertical.svg` / `.png` | Miroir + nom en dessous : écran de démarrage, affiche, fiche Play Store |
| `brand-board.svg` / `.png` | Planche d'identité visuelle : les trois logos, la police, les couleurs |

## Ce que dit le logo

Un miroir ovale. Dedans, le **reflet** d'une personne, un visage humain sans traits distinctifs, que chacun peut voir comme le sien. Devant le miroir, bien réels, **un téléphone et deux mains** qui le tiennent.

- L'utilisateur ne peut pas tenir son téléphone. Quand il le regarde, il y voit **Bob, son reflet**, qui le tient et le manipule à sa place.
- Le téléphone cache le bas du visage : de Bob, on ne voit que **des yeux et des mains**. Les yeux regardent l'écran (ce que Bob voit), les mains le manipulent (ce que Bob fait).
- Le nom se lit de deux façons : *Bob's Hands*, les mains de Bob, et *Bob is hands*, Bob **est** des mains.
- L'utilisateur reste au centre : son visage est à l'échelle du téléphone, il interagit avec lui.

Idée originale et croquis : Gianny (Nanou).

## Couleurs

| Rôle | Couleur |
|---|---|
| Bleu nuit (contours, « Bob's », B) | `#22314D` |
| Bleu vif (« Hands », H, pull) | `#3E8EE0` |
| Or du cadre | `#F7D58C` → `#D99A3A` |
| Verre du miroir | `#EAF6FF` → `#CFE6F7` |
| Peau | `#F2D2B6` |

## Police

**Fredoka** (Google Fonts, licence SIL Open Font License), graisse SemiBold (600). Les fichiers SVG contiennent du texte : installer Fredoka pour les ouvrir avec le bon rendu. Les PNG sont déjà rendus.

## Sources

Les logos sont générés par code, dans `tools/branding/` :
- `logo_v5.py` produit le logo officiel (série 5, le miroir) ;
- `logo_v3.py` contient le personnage (visage, yeux, téléphone, mains) ;
- `logo_v4.py` contient le verre du miroir et le cadre ;
- `brand_board.py` produit la planche d'identité visuelle.

Les dossiers `propositions*/` gardent l'historique des pistes explorées.
