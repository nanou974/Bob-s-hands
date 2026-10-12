#!/usr/bin/env python3
"""
Propositions de logo pour Bob's Hands, construites avec les mêmes calques
que le personnage « petit robot » (tools/sprites/petit_robot.py).

Sorties (dans assets/pictures/branding/propositions/) :
  - A-menton-dans-les-mains.svg/.png
  - B-coucou.svg/.png
  - C-icone-appli.svg/.png
  - D-logotype.svg/.png          nom écrit, le « o » de Bob est son visage
  - planche-logos.png            les quatre pistes côte à côte

Police : Fredoka (Google Fonts, licence SIL OFL), à installer pour ouvrir
les SVG avec le bon rendu du texte.

Usage :  python3 tools/branding/logo.py
"""

import sys
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "sprites"))
import petit_robot as R  # noqa: E402

OUT = ROOT / "assets" / "pictures" / "branding" / "propositions"
NS = ('xmlns="http://www.w3.org/2000/svg" '
      'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"')
ACCENT = "#3E8EE0"
FONT = "Fredoka"


def robot(pose):
    """Le contenu SVG d'une pose du robot, dans un repère 256 x 256."""
    return R.pose_svg(pose).split(">", 1)[1].rsplit("</svg>", 1)[0]


def big_mitten(x, y, rot=0, scale=1.5):
    return f'<g transform="translate({x} {y}) scale({scale})">{R.mitten(0, 0, rot)}</g>'


def svg(w, h, body, bg=None):
    back = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg {NS} width="{w}" height="{h}" viewBox="0 0 {w} {h}">{back}{body}</svg>'


# ------------------------------------------------------------- piste A
def piste_a():
    """Bob, menton dans les mains : attentif, prêt à aider."""
    face = robot(dict(id="a", nom="", yeux="rieur", sourcils="aucun",
                      bouche="grand_sourire", joues=True))
    hands = big_mitten(88, 222, 14) + big_mitten(168, 222, -14)
    return svg(512, 512, f'<g transform="translate(16 0) scale(1.875)">{face}{hands}</g>')


# ------------------------------------------------------------- piste B
def piste_b():
    """Bob qui fait coucou : chaleureux, accueillant."""
    face = robot(dict(id="b", nom="", yeux="rieur", sourcils="aucun",
                      bouche="grand_sourire", joues=True, incl=-6, mains="salut"))
    return svg(512, 512, f'<g transform="translate(16 16) scale(1.8)">{face}</g>')


# ------------------------------------------------------------- piste C
def piste_c():
    """Icône d'application : le visage de Bob plein cadre."""
    s = 512
    body = (
        f'<rect x="16" y="16" width="480" height="480" rx="112" fill="{R.SHELL}" stroke="{R.LINE}" stroke-width="14"/>'
        f'<path d="M86 70 Q140 48 200 52" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" opacity=".8"/>'
        f'<rect x="72" y="118" width="368" height="292" rx="84" fill="{R.SCREEN}"/>'
        # visage agrandi, recentré sur l'écran
        f'<g transform="translate(-90 -128) scale(2.72)">'
        f'{R.cheeks(True)}{R.eyes("rieur")}{R.mouth("grand_sourire")}</g>'
        # antenne
        f'<line x1="256" y1="118" x2="256" y2="66" stroke="{R.LINE}" stroke-width="12" stroke-linecap="round"/>'
        f'<circle cx="256" cy="56" r="20" fill="{R.ANTENNA["jaune"]}" stroke="{R.LINE}" stroke-width="10"/>'
        # deux mains en bas
        + big_mitten(120, 446, 10, 2.0) + big_mitten(392, 446, -10, 2.0)
    )
    return svg(s, s, body)


# ------------------------------------------------------------- piste D
def piste_d():
    """Logotype : « Bob's Hands », le « o » de Bob est son visage."""
    w, h = 1200, 360
    face = robot(dict(id="d", nom="", yeux="rieur", sourcils="aucun",
                      bouche="grand_sourire", joues=True))
    t = f'font-family="{FONT}" font-weight="600" font-size="150"'
    body = (
        f'<text x="88" y="250" {t} fill="{R.LINE}">B</text>'
        f'<g transform="translate(170 74) scale(0.82)">{face}</g>'
        f'<text x="366" y="250" {t} fill="{R.LINE}">b\'s</text>'
        f'<text x="592" y="250" {t} fill="{ACCENT}">Hands</text>'
        f'<text x="596" y="312" font-family="{FONT}" font-weight="500" font-size="34" '
        f'fill="#6B7A90">tes mains, tes yeux, à la voix</text>'
    )
    return svg(w, h, body)


def save(name, content):
    (OUT / f"{name}.svg").write_text(content, encoding="utf-8")
    cairosvg.svg2png(bytestring=content.encode(), write_to=str(OUT / f"{name}.png"))
    return content


def board(items):
    """Planche de présentation des pistes."""
    W, PAD = 1600, 40
    tile = (W - PAD * 4) // 3
    y_word = PAD + tile + 90
    H = y_word + 420
    out = [f'<rect width="{W}" height="{H}" fill="#F4F7FB"/>']
    for i, (label, content) in enumerate(items[:3]):
        x = PAD + i * (tile + PAD)
        inner = content.split(">", 1)[1].rsplit("</svg>", 1)[0]
        out.append(
            f'<rect x="{x}" y="{PAD}" width="{tile}" height="{tile + 60}" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
            f'<g transform="translate({x + 20} {PAD + 20}) scale({(tile - 40) / 512})">{inner}</g>'
            f'<text x="{x + tile / 2}" y="{PAD + tile + 40}" text-anchor="middle" font-family="{FONT}" '
            f'font-weight="500" font-size="30" fill="{R.LINE}">{label}</text>')
    label, content = items[3]
    inner = content.split(">", 1)[1].rsplit("</svg>", 1)[0]
    out.append(
        f'<rect x="{PAD}" y="{y_word - 20}" width="{W - PAD * 2}" height="400" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
        f'<g transform="translate({(W - 1200) / 2} {y_word})">{inner}</g>'
        f'<text x="{W / 2}" y="{y_word + 360}" text-anchor="middle" font-family="{FONT}" '
        f'font-weight="500" font-size="30" fill="{R.LINE}">{label}</text>')
    cairosvg.svg2png(bytestring=svg(W, H, "".join(out)).encode(),
                     write_to=str(OUT / "planche-logos.png"))


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = [
        ("A · Menton dans les mains", save("A-menton-dans-les-mains", piste_a())),
        ("B · Coucou", save("B-coucou", piste_b())),
        ("C · Icône d'application", save("C-icone-appli", piste_c())),
        ("D · Logotype", save("D-logotype", piste_d())),
    ]
    board(items)
    print(f"Propositions -> {OUT}")


if __name__ == "__main__":
    build()
