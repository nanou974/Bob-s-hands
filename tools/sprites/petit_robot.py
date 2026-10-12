#!/usr/bin/env python3
"""
Générateur de la planche d'humeurs du personnage « petit robot » de Bob's Hands.

Le personnage est construit en CALQUES (tête, écran, yeux, sourcils, bouche,
joues, mains, effets). Chaque pose est une simple combinaison de morceaux,
et la tête entière pivote d'un bloc pour les inclinaisons.

Sorties (dans assets/pictures/characters/petit-robot/) :
  - sheet.png    planche de sprites transparente (sans texte), à utiliser dans l'appli
  - sheet.json   coordonnées de chaque pose dans la planche
  - preview.png  planche annotée avec le nom des poses, pour relire
  - layers/*.svg une source SVG par pose, chaque élément dans son calque
                 (s'ouvre dans Inkscape avec les calques séparés)

Usage :  python3 tools/sprites/petit_robot.py
Dépendance : pip install cairosvg
"""

import json
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "pictures" / "characters" / "petit-robot"

CELL = 256          # taille d'une case de la planche, en pixels
COLS = 6            # nombre de colonnes de la planche

# ---------------------------------------------------------------- palette
LINE = "#2B3A55"        # contour
SHELL = "#A9DAF2"       # coque de la tête
SHELL_SHADE = "#86C3E3"
SCREEN = "#24324B"      # écran du visage
GLOW = "#8CF5E4"        # traits lumineux (yeux, sourcils, bouche)
BLUSH = "#FF8FB1"
WHITE = "#FFFFFF"
ANTENNA = {
    "jaune": "#FFD45C",   # repos
    "bleu": "#6FB8FF",    # écoute
    "orange": "#FFA94D",  # action, attente de confirmation
    "vert": "#7BE495",    # réussite
    "rose": "#FF8FB1",    # émotion douce
    "gris": "#9AA6B8",    # veille, sommeil, tristesse
    "rouge": "#FF6B6B",   # volume fort
}

CX = 128                 # centre horizontal du visage
EYE_Y = 135
EYE_DX = 28              # écart des yeux par rapport au centre
MOUTH_Y = 172


# ---------------------------------------------------------------- calques
def layer(name, content, transform=""):
    t = f' transform="{transform}"' if transform else ""
    return (f'<g id="{name}" inkscape:label="{name}" '
            f'inkscape:groupmode="layer"{t}>{content}</g>')


def head_shell():
    return (
        # oreilles / boulons
        f'<rect x="26" y="122" width="22" height="38" rx="9" fill="{SHELL_SHADE}" stroke="{LINE}" stroke-width="6"/>'
        f'<rect x="208" y="122" width="22" height="38" rx="9" fill="{SHELL_SHADE}" stroke="{LINE}" stroke-width="6"/>'
        # coque
        f'<rect x="42" y="62" width="172" height="156" rx="46" fill="{SHELL}" stroke="{LINE}" stroke-width="6"/>'
        # reflet
        f'<path d="M70 82 Q90 72 112 74" fill="none" stroke="{WHITE}" stroke-width="7" stroke-linecap="round" opacity=".8"/>'
    )


def antenna(color):
    c = ANTENNA[color]
    return (
        f'<line x1="128" y1="62" x2="128" y2="36" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>'
        f'<circle cx="128" cy="28" r="11" fill="{c}" stroke="{LINE}" stroke-width="5"/>'
        f'<circle cx="124" cy="24" r="3.5" fill="{WHITE}" opacity=".85"/>'
    )


def screen():
    return f'<rect x="60" y="90" width="136" height="108" rx="32" fill="{SCREEN}"/>'


def _stroke(d, w=6):
    return (f'<path d="{d}" fill="none" stroke="{GLOW}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def eye(kind, x, y):
    """Un œil centré en (x, y)."""
    if kind == "ouvert":
        return (f'<ellipse cx="{x}" cy="{y}" rx="11" ry="14" fill="{GLOW}"/>'
                f'<circle cx="{x + 4}" cy="{y - 5}" r="3.5" fill="{WHITE}"/>')
    if kind == "ecarquille":
        return (f'<ellipse cx="{x}" cy="{y}" rx="14" ry="17" fill="{GLOW}"/>'
                f'<circle cx="{x}" cy="{y}" r="5" fill="{SCREEN}"/>'
                f'<circle cx="{x + 5}" cy="{y - 7}" r="3.5" fill="{WHITE}"/>')
    if kind == "mi_clos":
        return (f'<path d="M{x - 11} {y + 1} A11 9 0 0 0 {x + 11} {y + 1} Z" fill="{GLOW}"/>'
                + _stroke(f"M{x - 13} {y + 1} L{x + 13} {y + 1}", 5))
    if kind == "ferme":
        return _stroke(f"M{x - 12} {y} Q{x} {y + 9} {x + 12} {y}")
    if kind == "rieur":
        return _stroke(f"M{x - 12} {y + 4} Q{x} {y - 11} {x + 12} {y + 4}")
    if kind == "plisse":
        return f'<ellipse cx="{x}" cy="{y}" rx="12" ry="5" fill="{GLOW}"/>'
    if kind == "triste":
        return (f'<ellipse cx="{x}" cy="{y + 3}" rx="10" ry="12" fill="{GLOW}"/>'
                f'<circle cx="{x + 3}" cy="{y - 1}" r="3" fill="{WHITE}"/>')
    raise ValueError(kind)


def eyes(kind, look=(0, 0)):
    dx, dy = look
    return (eye(kind, CX - EYE_DX + dx, EYE_Y + dy)
            + eye(kind, CX + EYE_DX + dx, EYE_Y + dy))


def brows(kind, look=(0, 0)):
    if kind == "aucun":
        return ""
    dx, dy = look
    lx, rx = CX - EYE_DX + dx, CX + EYE_DX + dx
    y = 112 + dy
    shapes = {
        # (gauche), (droite) : décalages des extrémités (ext_y, int_y)
        "neutres": ((0, 0), (0, 0)),
        "leves": ((-7, -7), (-7, -7)),
        "fronces": ((-4, 4), (-4, 4)),
        "inclines": ((4, -5), (4, -5)),
        "un_leve": ((0, 0), (-10, -10)),
    }
    (le, li), (re, ri) = shapes[kind]
    left = f"M{lx - 12} {y + le} L{lx + 10} {y + li}"
    right = f"M{rx + 12} {y + re} L{rx - 10} {y + ri}"
    if kind == "leves":
        left = f"M{lx - 12} {y - 4} Q{lx} {y - 12} {lx + 10} {y - 5}"
        right = f"M{rx + 12} {y - 4} Q{rx} {y - 12} {rx - 10} {y - 5}"
    return _stroke(left) + _stroke(right)


def mouth(kind, look=(0, 0)):
    dx, dy = look
    x, y = CX + dx, MOUTH_Y + dy
    m = {
        "fermee": _stroke(f"M{x - 12} {y} L{x + 12} {y}"),
        "leger_sourire": _stroke(f"M{x - 12} {y - 2} Q{x} {y + 6} {x + 12} {y - 2}"),
        "sourire": _stroke(f"M{x - 16} {y - 4} Q{x} {y + 12} {x + 16} {y - 4}"),
        "grand_sourire": f'<path d="M{x - 20} {y - 6} Q{x} {y + 22} {x + 20} {y - 6} Z" fill="{GLOW}" stroke="{GLOW}" stroke-width="3" stroke-linejoin="round"/>',
        "rire": (f'<path d="M{x - 22} {y - 8} Q{x} {y + 26} {x + 22} {y - 8} Z" fill="{GLOW}" stroke="{GLOW}" stroke-width="3" stroke-linejoin="round"/>'
                 f'<path d="M{x - 10} {y + 9} Q{x} {y + 3} {x + 10} {y + 9} Q{x} {y + 15} {x - 10} {y + 9} Z" fill="{BLUSH}"/>'),
        "parle": f'<ellipse cx="{x}" cy="{y + 1}" rx="10" ry="7" fill="{GLOW}"/>',
        "crie": f'<ellipse cx="{x}" cy="{y + 2}" rx="14" ry="12" fill="{GLOW}"/>',
        "petite": f'<ellipse cx="{x}" cy="{y}" rx="5" ry="3.5" fill="{GLOW}"/>',
        "o": f'<circle cx="{x}" cy="{y + 1}" r="7" fill="none" stroke="{GLOW}" stroke-width="5"/>',
        "moue": _stroke(f"M{x - 10} {y + 2} Q{x - 5} {y - 4} {x} {y + 2} Q{x + 5} {y + 8} {x + 10} {y + 2}", 5),
        "de_travers": _stroke(f"M{x - 14} {y + 1} Q{x + 4} {y + 4} {x + 16} {y - 7}"),
        "triste": _stroke(f"M{x - 13} {y + 5} Q{x} {y - 6} {x + 13} {y + 5}"),
        "ondulee": _stroke(f"M{x - 16} {y + 2} L{x - 10} {y - 3} L{x - 4} {y + 2} L{x + 2} {y - 3} L{x + 8} {y + 2} L{x + 14} {y - 3}", 5),
    }
    return m[kind]


def cheeks(on, look=(0, 0)):
    if not on:
        return ""
    dx, dy = look
    return (f'<ellipse cx="{CX - 46 + dx}" cy="{160 + dy}" rx="10" ry="6" fill="{BLUSH}" opacity=".7"/>'
            f'<ellipse cx="{CX + 46 + dx}" cy="{160 + dy}" rx="10" ry="6" fill="{BLUSH}" opacity=".7"/>')


def mitten(x, y, rot=0, cupped=False):
    """Une main de robot (moufle) centrée en (x, y)."""
    body = (f'<rect x="-15" y="-17" width="30" height="34" rx="14" fill="{SHELL}" stroke="{LINE}" stroke-width="5"/>'
            f'<rect x="-22" y="-6" width="12" height="17" rx="6" fill="{SHELL}" stroke="{LINE}" stroke-width="5"/>')
    if cupped:
        body = (f'<path d="M-6 -20 Q16 -20 16 0 Q16 20 -6 20" fill="none" stroke="{LINE}" stroke-width="16" stroke-linecap="round"/>'
                f'<path d="M-6 -20 Q16 -20 16 0 Q16 20 -6 20" fill="none" stroke="{SHELL}" stroke-width="7" stroke-linecap="round"/>')
    return f'<g transform="translate({x} {y}) rotate({rot})">{body}</g>'


def hands(kind):
    if kind == "aucune":
        return ""
    if kind == "porte_voix":
        # porte-voix horizontal : petit bout contre la bouche, pavillon vers la droite
        cone = (f'<path d="M134 164 L134 182 L200 206 L200 140 Z" fill="{ANTENNA["rouge"]}" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
                f'<ellipse cx="200" cy="173" rx="9" ry="33" fill="{WHITE}" stroke="{LINE}" stroke-width="5"/>'
                f'<rect x="126" y="160" width="14" height="26" rx="6" fill="{WHITE}" stroke="{LINE}" stroke-width="5"/>')
        return cone + mitten(160, 206, 0)
    if kind == "doigt_levres":
        return (mitten(128, 224, 0)
                + f'<rect x="120" y="166" width="16" height="46" rx="8" fill="{SHELL}" stroke="{LINE}" stroke-width="5"/>')
    if kind == "main_oreille":
        # main levée contre l'oreille droite, avec le son qui arrive
        arcs = "".join(
            f'<path d="M{246 - i * 4} {116 + i * 2} Q{234 - i * 4} {141} {246 - i * 4} {166 - i * 2}" '
            f'fill="none" stroke="{ANTENNA["bleu"]}" stroke-width="4" stroke-linecap="round" opacity="{1 - i * .3}"/>'
            for i in range(2))
        return mitten(222, 142, -12) + arcs
    if kind == "salut":
        return (mitten(214, 94, 18)
                + _fx_lines([(196, 64, 202, 54), (220, 58, 222, 46), (238, 70, 246, 62)]))
    raise ValueError(kind)


def _fx_lines(segments, color=LINE, w=5):
    return "".join(
        f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
        for a, b, c, d in segments)


def _text(x, y, s, size, color=LINE, rot=0):
    return (f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-weight="bold" '
            f'font-size="{size}" fill="{color}" '
            f'transform="rotate({rot} {x} {y})">{s}</text>')


def fx(kinds):
    out = ""
    for k in kinds:
        if k == "zzz":
            c = ANTENNA["bleu"]
            out += _text(178, 82, "z", 20, c) + _text(194, 64, "z", 26, c) + _text(212, 46, "Z", 32, c)
        elif k == "question":
            out += _text(204, 62, "?", 44, ANTENNA["bleu"], 12)
        elif k == "exclamation":
            out += _text(206, 64, "!", 48, ANTENNA["orange"], 10)
        elif k == "goutte":
            out += (f'<path d="M206 82 Q198 98 206 104 Q214 98 206 82 Z" fill="#7FD0FF" stroke="{LINE}" stroke-width="4"/>')
        elif k == "coeur":
            out += (f'<path d="M214 62 C206 48 188 56 196 70 L214 86 L232 70 C240 56 222 48 214 62 Z" '
                    f'fill="{BLUSH}" stroke="{LINE}" stroke-width="4" stroke-linejoin="round"/>')
        elif k == "etincelles":
            for x, y, r in ((36, 56, 12), (222, 50, 14), (230, 196, 9)):
                out += (f'<path d="M{x} {y - r} Q{x} {y} {x + r} {y} Q{x} {y} {x} {y + r} '
                        f'Q{x} {y} {x - r} {y} Q{x} {y} {x} {y - r} Z" fill="{ANTENNA["jaune"]}" stroke="{LINE}" stroke-width="3"/>')
        elif k == "ondes_son":
            out += "".join(
                f'<path d="M{186 + i * 14} {200 - i * 6} Q{198 + i * 16} {214} {186 + i * 14} {228 + i * 6}" '
                f'fill="none" stroke="{ANTENNA["rouge"]}" stroke-width="5" stroke-linecap="round"/>'
                for i in range(3))
        elif k == "haha":
            out += _text(190, 62, "ha", 28, "#F08A24", -12) + _text(14, 76, "ha", 24, "#F08A24", 12)
        elif k == "points":
            out += "".join(f'<circle cx="{196 + i * 14}" cy="60" r="5" fill="{LINE}"/>' for i in range(3))
        elif k == "chut":
            out += _text(176, 58, "chut…", 24, "#3E8EE0", -8)
        else:
            raise ValueError(k)
    return out


# ---------------------------------------------------------------- poses
# Chaque pose combine : yeux, sourcils, bouche, inclinaison (degrés),
# regard (décalage du visage dans l'écran : gauche/droite, haut/bas),
# antenne, joues, mains, effets.
POSES = [
    # --- repos et veille
    dict(id="repos", nom="Repos", yeux="ouvert", sourcils="neutres", bouche="leger_sourire"),
    dict(id="veille", nom="Veille douce", yeux="mi_clos", sourcils="neutres", bouche="fermee", regard=(0, 6), antenne="gris"),
    dict(id="endormi", nom="Endormi", yeux="ferme", sourcils="aucun", bouche="petite", regard=(0, 8), incl=8, antenne="gris", fx=["zzz"]),
    # --- écoute et conversation
    dict(id="ecoute", nom="Écoute", yeux="ouvert", sourcils="leves", bouche="fermee", incl=-12, antenne="bleu"),
    dict(id="parle", nom="Parle", yeux="ouvert", sourcils="neutres", bouche="parle"),
    dict(id="reflechit", nom="Réfléchit", yeux="ouvert", sourcils="un_leve", bouche="moue", regard=(8, -8), incl=6, antenne="bleu", fx=["points"]),
    # --- émotions
    dict(id="content", nom="Content", yeux="ouvert", sourcils="neutres", bouche="sourire", joues=True),
    dict(id="joyeux", nom="Joyeux, complice", yeux="rieur", sourcils="leves", bouche="grand_sourire", incl=6, joues=True),
    dict(id="rit", nom="Rit avec toi", yeux="rieur", sourcils="leves", bouche="rire", regard=(0, -4), incl=-6, joues=True, antenne="orange", fx=["haha"]),
    dict(id="triste", nom="Triste, peiné", yeux="triste", sourcils="inclines", bouche="triste", regard=(0, 6), antenne="gris"),
    dict(id="surpris", nom="Surpris, intrigué", yeux="ecarquille", sourcils="leves", bouche="o", fx=["exclamation"]),
    dict(id="taquin", nom="Taquin, malicieux", yeux="ouvert", sourcils="un_leve", bouche="de_travers", regard=(8, 0), incl=10, antenne="orange"),
    dict(id="gene", nom="Désolé, gêné", yeux="mi_clos", sourcils="inclines", bouche="ondulee", regard=(-4, 6), incl=-6, joues=True, fx=["goutte"]),
    dict(id="attendri", nom="Attendri, doux", yeux="mi_clos", sourcils="inclines", bouche="sourire", incl=-10, joues=True, antenne="rose", fx=["coeur"]),
    # --- action et résultat
    dict(id="concentre", nom="Concentré, agit", yeux="plisse", sourcils="fronces", bouche="fermee", antenne="orange"),
    dict(id="satisfait", nom="Satisfait, réussite", yeux="rieur", sourcils="leves", bouche="grand_sourire", regard=(0, -6), antenne="vert", fx=["etincelles"]),
    dict(id="confirmation", nom="Demande confirmation", yeux="ouvert", sourcils="leves", bouche="leger_sourire", incl=-8, antenne="orange", fx=["question"]),
    # --- relation
    dict(id="salut", nom="Salue", yeux="rieur", sourcils="leves", bouche="grand_sourire", joues=True, mains="salut"),
    # --- attitudes sonores
    dict(id="crie", nom="Parle fort", yeux="ecarquille", sourcils="leves", bouche="crie", regard=(0, -6), antenne="rouge", mains="porte_voix", fx=["ondes_son"]),
    dict(id="chuchote", nom="Chuchote", yeux="mi_clos", sourcils="neutres", bouche="petite", incl=6, antenne="bleu", mains="doigt_levres", fx=["chut"]),
    dict(id="tend_oreille", nom="Tend l'oreille", yeux="ouvert", sourcils="leves", bouche="fermee", regard=(8, 0), incl=14, antenne="bleu", mains="main_oreille"),
    # --- orientations
    dict(id="tete_face", nom="Tête de face", yeux="ouvert", sourcils="neutres", bouche="fermee"),
    dict(id="tete_gauche", nom="Tête à gauche", yeux="ouvert", sourcils="neutres", bouche="fermee", regard=(-14, 0), incl=-4),
    dict(id="tete_droite", nom="Tête à droite", yeux="ouvert", sourcils="neutres", bouche="fermee", regard=(14, 0), incl=4),
    dict(id="tete_haut", nom="Tête en haut", yeux="ouvert", sourcils="neutres", bouche="fermee", regard=(0, -12)),
    dict(id="tete_bas", nom="Tête en bas", yeux="ouvert", sourcils="neutres", bouche="fermee", regard=(0, 12)),
]


def pose_svg(p, size=CELL):
    look = p.get("regard", (0, 0))
    tilt = p.get("incl", 0)
    rot = f"rotate({tilt} 128 150)" if tilt else ""
    # Le visage bouge moins verticalement dans l'écran que le regard ne le dit
    face_parts = (
        layer("joues", cheeks(p.get("joues", False), look))
        + layer("yeux", eyes(p["yeux"], look))
        + layer("sourcils", brows(p["sourcils"], look))
        + layer("bouche", mouth(p["bouche"], look))
    )
    tete = (layer("antenne", antenna(p.get("antenne", "jaune")))
            + layer("coque", head_shell())
            + layer("ecran", screen())
            + face_parts)
    mains = p.get("mains", "aucune")
    # Les mains liées au visage pivotent avec la tête ; le salut reste droit
    head_group = layer("tete", tete + (layer("mains", hands(mains)) if mains != "salut" else ""), rot)
    hors_tete = layer("mains_libres", hands(mains)) if mains == "salut" else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'width="{size}" height="{size}" viewBox="0 0 256 256">'
            f'{head_group}{hors_tete}{layer("effets", fx(p.get("fx", [])))}</svg>')


def build():
    (OUT / "layers").mkdir(parents=True, exist_ok=True)
    rows = (len(POSES) + COLS - 1) // COLS
    W, H = COLS * CELL, rows * CELL

    frames = {}
    sheet_cells, preview_cells = [], []
    LABEL = 40
    for i, p in enumerate(POSES):
        cx, cy = (i % COLS) * CELL, (i // COLS) * CELL
        svg = pose_svg(p)
        (OUT / "layers" / f"{i + 1:02d}-{p['id']}.svg").write_text(svg, encoding="utf-8")
        inner = svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
        sheet_cells.append(f'<g transform="translate({cx} {cy})">{inner}</g>')
        py = (i // COLS) * (CELL + LABEL)
        preview_cells.append(
            f'<g transform="translate({cx} {py})">'
            f'<rect x="6" y="6" width="{CELL - 12}" height="{CELL + LABEL - 12}" rx="22" fill="#FFFFFF" stroke="#E3E8F0" stroke-width="2"/>'
            f'{inner}'
            f'<text x="{CELL / 2}" y="{CELL + 18}" text-anchor="middle" font-family="DejaVu Sans" '
            f'font-size="17" fill="#2B3A55">{i + 1}. {p["nom"]}</text></g>')
        frames[p["id"]] = {"numero": i + 1, "nom": p["nom"], "x": cx, "y": cy, "w": CELL, "h": CELL}

    ns = ('xmlns="http://www.w3.org/2000/svg" '
          'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"')
    sheet = f'<svg {ns} width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(sheet_cells)}</svg>'
    PH = rows * (CELL + LABEL)
    preview = (f'<svg {ns} width="{W}" height="{PH}" viewBox="0 0 {W} {PH}">'
               f'<rect width="{W}" height="{PH}" fill="#F4F7FB"/>{"".join(preview_cells)}</svg>')

    cairosvg.svg2png(bytestring=sheet.encode(), write_to=str(OUT / "sheet.png"))
    cairosvg.svg2png(bytestring=preview.encode(), write_to=str(OUT / "preview.png"))
    (OUT / "sheet.json").write_text(json.dumps({
        "personnage": "petit-robot",
        "image": "sheet.png",
        "taille_case": CELL,
        "colonnes": COLS,
        "poses": frames,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(POSES)} poses -> {OUT}")


if __name__ == "__main__":
    build()
