#!/usr/bin/env python3
"""
Logo Bob's Hands — série 3, d'après le croquis de Gianny.

La silhouette, c'est Bob : un visage humain sans traits distinctifs. On voit le dos du téléphone : ses yeux regardent
l'écran, ses mains le tiennent et le manipulent. Bob est les yeux et les mains.

Variantes :
  1 · trait        noir et blanc, au plus près du croquis
  2 · couleur      même dessin, palette Bob's Hands
  3 · lumiere      la lumière de l'écran éclaire le visage de Bob

Sorties : assets/pictures/branding/propositions-v3/
Usage : python3 tools/branding/logo_v3.py
"""

import math
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "pictures" / "branding" / "propositions-v3"
FONT = "Fredoka"

NAVY = "#22314D"
HOPE = "#3E8EE0"
SUN_A = "#FFC24D"
SUN_B = "#FF8A5B"
SKY = "#7EC8F2"
GREEN = "#8FD6A0"
CREAM = "#FFF6EA"

DEFS = f"""<defs>
  <linearGradient id="main" x1="0" y1="330" x2="0" y2="512" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{SUN_A}"/><stop offset="1" stop-color="{SUN_B}"/></linearGradient>
  <linearGradient id="ecran" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{SKY}"/><stop offset="1" stop-color="#FFD9A8"/></linearGradient>
  <linearGradient id="soleil" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{SUN_A}"/><stop offset="1" stop-color="{SUN_B}"/></linearGradient>
</defs>"""


def pt(x, y, r, deg):
    a = math.radians(deg)
    return x + r * math.cos(a), y + r * math.sin(a)


def svg(w, h, body, bg=None):
    back = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">{DEFS}{back}{body}</svg>')


# ------------------------------------------------------------------ pièces
PHONE = dict(x=184, y=236, w=144, h=236, r=28)


def head(fill, line, sw):
    return (f'<ellipse cx="256" cy="214" rx="124" ry="166" fill="{fill}" stroke="{line}" stroke-width="{sw}"/>'
            f'<ellipse cx="208" cy="168" rx="24" ry="11" fill="{fill}" stroke="{line}" stroke-width="{sw * .8}"/>'
            f'<ellipse cx="304" cy="168" rx="24" ry="11" fill="{fill}" stroke="{line}" stroke-width="{sw * .8}"/>')


def phone(fill, screen=None, line=None, sw=0):
    p = PHONE
    stroke = f' stroke="{line}" stroke-width="{sw}"' if line else ""
    out = (f'<rect x="{p["x"]}" y="{p["y"]}" width="{p["w"]}" height="{p["h"]}" '
           f'rx="{p["r"]}" fill="{fill}"{stroke}/>')
    if screen:
        out += screen
    return out


def phone_back(fill, line, sw):
    """Le dos du téléphone : coque et bloc photo."""
    p = PHONE
    return (f'<rect x="{p["x"]}" y="{p["y"]}" width="{p["w"]}" height="{p["h"]}" rx="{p["r"]}" '
            f'fill="{fill}" stroke="{line}" stroke-width="{sw}"/>'
            f'<rect x="{p["x"] + 16}" y="{p["y"] + 16}" width="40" height="58" rx="14" fill="none" '
            f'stroke="{"#5A6B8C" if fill != "#3A3A3A" else "#777"}" stroke-width="5"/>'
            f'<circle cx="{p["x"] + 36}" cy="{p["y"] + 34}" r="8" fill="{"#5A6B8C" if fill != "#3A3A3A" else "#777"}"/>'
            f'<circle cx="{p["x"] + 36}" cy="{p["y"] + 56}" r="8" fill="{"#5A6B8C" if fill != "#3A3A3A" else "#777"}"/>')


# Main gauche, vue de dos : la paume serre le bord du téléphone, les quatre
# doigts s'étendent sur le dos de l'appareil (côté spectateur).
LEFT_FINGERS = [(176, 356, -14, 44), (176, 388, -6, 50), (176, 420, 2, 50), (176, 452, 10, 42)]
LEFT_PALM = "M112 540 C112 470 136 396 172 342 L190 350 L196 470 C188 494 184 520 184 540 Z"


def hand(fill, line, sw, side=-1, w=28):
    def caps(color, extra):
        out = ""
        for x, y, a, L in LEFT_FINGERS:
            x2, y2 = pt(x, y, L, a)
            out += (f'<line x1="{x}" y1="{y}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
                    f'stroke-width="{w + extra}" stroke-linecap="round"/>')
        return out
    outline = caps(line, sw * 2) + f'<path d="{LEFT_PALM}" fill="{line}" stroke="{line}" stroke-width="{sw * 2}" stroke-linejoin="round"/>'
    body = caps(fill, 0) + f'<path d="{LEFT_PALM}" fill="{fill}"/>'
    # plis des doigts pour bien les séparer
    creases = "".join(
        f'<path d="M{x - 4} {y + 15} Q{x + 6} {y + 16} {x + 14} {y + 14}" fill="none" stroke="{line}" '
        f'stroke-width="{max(2, sw * .5)}" stroke-linecap="round" opacity=".5"/>'
        for x, y, a, L in LEFT_FINGERS[:3])
    t = "" if side < 0 else ' transform="translate(512 0) scale(-1 1)"'
    return f'<g{t}>{outline}{body}{creases}</g>'


# ------------------------------------------------------------------ Bob
# Un visage humain « Monsieur Tout-le-Monde » : forme simple, aucun trait
# distinctif. Les yeux regardent l'écran : ils représentent ce que Bob voit.
HEAD = dict(cx=256, cy=196, rx=104, ry=128)
SKIN = "#F2D2B6"
SKIN_SHADE = "#E2B996"
HAIR = "#6B5444"
SWEATER = HOPE


def person(fill, line, sw, hair, sweater, shade):
    h = HEAD

    def ear(x):
        return (f'<ellipse cx="{x}" cy="{h["cy"] + 4}" rx="18" ry="28" fill="{fill}" '
                f'stroke="{line}" stroke-width="{sw}"/>')

    l, r, cy = h["cx"] - h["rx"], h["cx"] + h["rx"], h["cy"]
    hair_path = (f"M{l + 2} {cy - 14} "
                 f"C{l - 6} {cy - 184} {r + 6} {cy - 184} {r - 2} {cy - 14} "
                 f"C{r - 30} {cy - 70} {h['cx'] - 10} {cy - 86} {l + 2} {cy - 14} Z")
    return (
        # épaules et cou
        f'<path d="M40 540 C40 430 120 392 200 384 L312 384 C392 392 472 430 472 540 Z" '
        f'fill="{sweater}" stroke="{line}" stroke-width="{sw}" stroke-linejoin="round"/>'
        f'<rect x="222" y="300" width="68" height="96" rx="20" fill="{shade}" stroke="{line}" stroke-width="{sw}"/>'
        # oreilles, tête, cheveux
        + ear(l + 2) + ear(r - 2)
        + f'<ellipse cx="{h["cx"]}" cy="{cy}" rx="{h["rx"]}" ry="{h["ry"]}" fill="{fill}" stroke="{line}" stroke-width="{sw}"/>'
        + f'<path d="{hair_path}" fill="{hair}" stroke="{line}" stroke-width="{sw}" stroke-linejoin="round"/>'
        # sourcils, nez
        + f'<path d="M196 150 Q214 142 232 148 M280 148 Q298 142 316 150" fill="none" stroke="{line}" '
          f'stroke-width="{sw}" stroke-linecap="round"/>'
        + f'<path d="M256 186 Q250 210 256 218 Q262 222 268 218" fill="none" stroke="{line}" '
          f'stroke-width="{sw * .8}" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/>'
    )


def eyes(line, white, iris):
    """Yeux en amande, le regard baissé vers l'écran."""
    out = ""
    for x in (214, 298):
        shape = f"M{x - 22} 172 Q{x} 156 {x + 22} 172 Q{x} 184 {x - 22} 172 Z"
        # La pupille est découpée par la forme de l'œil : elle ne dépasse jamais
        # le bord des paupières, même quand le regard est baissé.
        out += (f'<clipPath id="oeil-{x}"><path d="{shape}"/></clipPath>'
                f'<path d="{shape}" fill="{white}"/>'
                f'<g clip-path="url(#oeil-{x})">'
                f'<circle cx="{x}" cy="174" r="8" fill="{iris}"/>'
                f'<circle cx="{x + 3}" cy="171" r="2.5" fill="#FFFFFF"/></g>'
                f'<path d="{shape}" fill="none" stroke="{line}" stroke-width="5" stroke-linejoin="round"/>')
    return out


def screen_glow():
    """La lumière de l'écran éclaire le bas du visage."""
    h = HEAD
    return ('<radialGradient id="lueur" cx="256" cy="250" r="140" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{SUN_A}" stop-opacity=".7"/>'
            f'<stop offset="1" stop-color="{SUN_A}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="tete"><ellipse cx="{h["cx"]}" cy="{h["cy"]}" rx="{h["rx"]}" ry="{h["ry"]}"/></clipPath>'
            '<g clip-path="url(#tete)"><rect x="100" y="60" width="312" height="300" fill="url(#lueur)"/></g>')


def logo(style):
    if style == "trait":
        body = (person("#FFFFFF", "#111111", 5, "#FFFFFF", "#FFFFFF", "#FFFFFF")
                + eyes("#111111", "#FFFFFF", "#111111")
                + phone_back("#3A3A3A", "#111111", 0)
                + hand("#FFFFFF", "#111111", 4, -1) + hand("#FFFFFF", "#111111", 4, 1))
        return svg(512, 512, body)
    glow = screen_glow() if style == "lumiere" else ""
    body = (f'<circle cx="256" cy="256" r="246" fill="{CREAM}"/>'
            + person(SKIN, NAVY, 7, HAIR, SWEATER, SKIN_SHADE)
            + glow + eyes(NAVY, "#FFFFFF", "#4A3A2E")
            + phone_back(NAVY, NAVY, 0)
            + hand(SKIN, NAVY, 7, -1) + hand(SKIN, NAVY, 7, 1))
    body = (f'<clipPath id="rond"><circle cx="256" cy="256" r="246"/></clipPath>'
            f'<g clip-path="url(#rond)">{body}</g>'
            f'<circle cx="256" cy="256" r="246" fill="none" stroke="{NAVY}" stroke-width="10"/>')
    return svg(512, 512, body)


def lockup(sym, w=1200, h=420):
    inner = sym.split(">", 1)[1].rsplit("</svg>", 1)[0]
    return svg(w, h,
               f'<g transform="translate(40 30) scale(0.70)">{inner}</g>'
               f'<text x="440" y="226" font-family="{FONT}" font-weight="600" font-size="128" fill="{NAVY}">Bob\'s</text>'
               f'<text x="440" y="336" font-family="{FONT}" font-weight="600" font-size="128" fill="{HOPE}">Hands</text>')


def save(name, content):
    (OUT / f"{name}.svg").write_text(content, encoding="utf-8")
    cairosvg.svg2png(bytestring=content.encode(), write_to=str(OUT / f"{name}.png"))


def board(items):
    W, PAD = 1560, 36
    tile = (W - PAD * 4) // 3
    H = PAD + tile + 70 + PAD + 420 + PAD
    out = [f'<rect width="{W}" height="{H}" fill="#F4F7FB"/>']
    for i, (label, sym) in enumerate(items):
        x = PAD + i * (tile + PAD)
        inner = sym.split(">", 1)[1].rsplit("</svg>", 1)[0]
        out.append(
            f'<rect x="{x}" y="{PAD}" width="{tile}" height="{tile + 70}" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
            f'<g transform="translate({x + 24} {PAD + 24}) scale({(tile - 48) / 512})">{inner}</g>'
            f'<text x="{x + tile / 2}" y="{PAD + tile + 46}" text-anchor="middle" font-family="{FONT}" '
            f'font-weight="500" font-size="30" fill="{NAVY}">{label}</text>')
    y = PAD + tile + 70 + PAD
    inner = lockup(items[2][1]).split(">", 1)[1].rsplit("</svg>", 1)[0]
    out.append(f'<rect x="{PAD}" y="{y}" width="{W - 2 * PAD}" height="420" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
               f'<g transform="translate({(W - 1200) / 2 + 120} {y})">{inner}</g>')
    cairosvg.svg2png(bytestring=svg(W, H, "".join(out)).encode(),
                     write_to=str(OUT / "planche-logos-v3.png"))


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = [("1 · Trait", logo("trait")), ("2 · Couleur", logo("couleur")),
             ("3 · Lumière", logo("lumiere"))]
    for label, sym in items:
        slug = label.split("·")[1].strip().lower().replace("è", "e")
        save(f"{label[0]}-{slug}-symbole", sym)
        save(f"{label[0]}-{slug}-logo-complet", lockup(sym))
    board(items)
    print(f"Propositions -> {OUT}")


if __name__ == "__main__":
    build()
