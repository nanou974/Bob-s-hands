#!/usr/bin/env python3
"""
Propositions de logo symboliques pour Bob's Hands (série 2).

Le logo ne représente pas un personnage : il dit ce que Bob apporte.
Mobilité retrouvée, espoir, une fenêtre sur le monde.

  A · L'envol      un oiseau dont les ailes sont des mains ouvertes
  B · La fenêtre   des volets qui s'ouvrent sur un lever de soleil
  C · La voix      un soleil qui se lève, ses rayons sont une onde de voix,
                   un chemin part vers lui

Sorties : assets/pictures/branding/propositions-v2/
Police : Fredoka (SIL OFL).
Usage : python3 tools/branding/logo_symboles.py
"""

import math
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "pictures" / "branding" / "propositions-v2"
FONT = "Fredoka"

NAVY = "#22314D"
SKY_TOP = "#7EC8F2"
SKY_LOW = "#FFD9A8"
SUN_A = "#FFC24D"
SUN_B = "#FF8A5B"
HOPE = "#3E8EE0"
GREEN = "#8FD6A0"
CREAM = "#FFF6EA"

DEFS = f"""
<defs>
  <linearGradient id="ciel" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{SKY_TOP}"/><stop offset="1" stop-color="{SKY_LOW}"/>
  </linearGradient>
  <linearGradient id="soleil" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{SUN_A}"/><stop offset="1" stop-color="{SUN_B}"/>
  </linearGradient>
  <linearGradient id="aile" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="{SUN_B}"/><stop offset="1" stop-color="{SUN_A}"/>
  </linearGradient>
  <linearGradient id="main" x1="0" y1="250" x2="0" y2="440" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{SUN_A}"/><stop offset="1" stop-color="{SUN_B}"/>
  </linearGradient>
  <linearGradient id="corps" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{HOPE}"/><stop offset="1" stop-color="#2A6CC0"/>
  </linearGradient>
</defs>"""


def svg(w, h, body, bg=None):
    back = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">{DEFS}{back}{body}</svg>')


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# --------------------------------------------------------------- A · L'envol
def cupped_hand(side):
    """Une main ouverte, doigts vers le haut, qui porte l'oiseau.

    Silhouette unie : on trace d'abord le contour (paume + doigts, en épais),
    puis le remplissage par-dessus, pour que les doigts fassent corps avec la paume.
    """
    palm = "M258 436 C196 436 132 408 120 352 L134 332 L234 326 L258 366 Z"
    # (base x, base y, angle en degrés, longueur, épaisseur)
    fingers = [
        (140, 344, -122, 62, 30),   # auriculaire
        (168, 334, -108, 80, 32),   # annulaire
        (198, 330, -96, 86, 32),    # majeur
        (226, 332, -84, 76, 32),    # index
        (244, 388, -64, 58, 32),    # pouce, vers le centre
    ]

    def strokes(color, extra):
        out = ""
        for x, y, a, L, w in fingers:
            x2, y2 = pt(x, y, L, a)
            out += (f'<line x1="{x}" y1="{y}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
                    f'stroke-width="{w + extra}" stroke-linecap="round"/>')
        return out

    outline = strokes(NAVY, 18) + f'<path d="{palm}" fill="{NAVY}" stroke="{NAVY}" stroke-width="18" stroke-linejoin="round"/>'
    fill = strokes("url(#main)", 0) + f'<path d="{palm}" fill="url(#main)"/>'
    crease = (f'<path d="M150 380 Q186 404 226 404" fill="none" stroke="{SUN_B}" '
              f'stroke-width="6" stroke-linecap="round" opacity=".55"/>')
    t = "" if side < 0 else ' transform="translate(512 0) scale(-1 1)"'
    return f'<g{t}>{outline}{fill}{crease}</g>'


def envol():
    bird = (
        # aile arrière
        f'<path d="M250 214 Q214 150 162 146 Q190 182 232 226 Z" fill="#7FB8F0" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>'
        # corps
        f'<path d="M206 252 Q246 214 300 206 Q322 204 330 190 Q336 214 314 228 Q276 256 222 262 Z" '
        f'fill="url(#corps)" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>'
        # queue
        f'<path d="M212 254 L176 270 L190 248 Z" fill="url(#corps)" stroke="{NAVY}" stroke-width="7" stroke-linejoin="round"/>'
        # aile avant, déployée vers le haut
        f'<path d="M262 220 Q284 140 352 112 Q338 170 292 228 Z" fill="url(#corps)" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>'
        # bec et œil
        f'<path d="M330 190 L350 192 L334 202 Z" fill="{SUN_A}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
        f'<circle cx="316" cy="200" r="4.5" fill="{NAVY}"/>'
    )
    body = (
        f'<circle cx="256" cy="256" r="236" fill="{CREAM}"/>'
        f'<circle cx="256" cy="190" r="120" fill="url(#soleil)" opacity=".28"/>'
        f'<circle cx="256" cy="190" r="78" fill="url(#soleil)" opacity=".35"/>'
        + cupped_hand(-1) + cupped_hand(1)
        + f'<g transform="translate(-6 -52)">{bird}</g>'
    )
    return svg(512, 512, body)


# --------------------------------------------------------------- B · La fenêtre
def fenetre():
    # ouverture en arche : x 156..356, y 110..400
    arch = "M156 400 L156 210 A100 100 0 0 1 356 210 L356 400 Z"
    inside = (
        f'<clipPath id="arche"><path d="{arch}"/></clipPath>'
        f'<g clip-path="url(#arche)">'
        f'<rect x="150" y="100" width="212" height="310" fill="url(#ciel)"/>'
        # soleil qui se lève
        f'<circle cx="256" cy="330" r="62" fill="url(#soleil)"/>'
        + "".join(
            f'<line x1="{pt(256, 330, 78, d)[0]:.1f}" y1="{pt(256, 330, 78, d)[1]:.1f}" '
            f'x2="{pt(256, 330, 104, d)[0]:.1f}" y2="{pt(256, 330, 104, d)[1]:.1f}" '
            f'stroke="{SUN_A}" stroke-width="10" stroke-linecap="round"/>'
            for d in range(-165, -10, 25)) +
        # collines
        f'<path d="M140 350 Q210 312 270 342 Q320 318 372 336 L372 410 L140 410 Z" fill="{GREEN}"/>'
        f'<path d="M140 372 Q230 340 372 372 L372 410 L140 410 Z" fill="#6CC487"/>'
        # oiseau qui s'envole
        f'<path d="M292 182 Q304 170 314 182 Q324 170 336 182" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<path d="M222 210 Q230 202 237 210 Q244 202 252 210" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</g>'
    )
    frame = (
        f'<path d="{arch}" fill="none" stroke="{NAVY}" stroke-width="14" stroke-linejoin="round"/>'
        # volets ouverts vers l'extérieur
        f'<path d="M150 212 L76 168 L76 412 L150 402 Z" fill="{HOPE}" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>'
        f'<path d="M362 212 L436 168 L436 412 L362 402 Z" fill="{HOPE}" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>'
        f'<line x1="98" y1="230" x2="130" y2="240" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="98" y1="290" x2="130" y2="292" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="98" y1="350" x2="130" y2="346" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="414" y1="230" x2="382" y2="240" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="414" y1="290" x2="382" y2="292" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="414" y1="350" x2="382" y2="346" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        # appui de fenêtre
        f'<rect x="132" y="398" width="248" height="26" rx="12" fill="{CREAM}" stroke="{NAVY}" stroke-width="12"/>'
    )
    return svg(512, 512, f'<circle cx="256" cy="268" r="236" fill="{CREAM}"/>' + inside + frame)


# --------------------------------------------------------------- C · La voix
def voix():
    cx, cy = 256, 300
    rays = ""
    # rayons = barres d'une onde de voix, longueurs irrégulières comme une parole
    lengths = [38, 64, 92, 70, 110, 84, 120, 84, 110, 70, 92, 64, 38]
    n = len(lengths)
    for i, L in enumerate(lengths):
        d = -180 + (i + 0.5) * 180 / n
        x1, y1 = pt(cx, cy, 104, d)
        x2, y2 = pt(cx, cy, 104 + L, d)
        rays += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="url(#soleil)" stroke-width="16" stroke-linecap="round"/>')
    body = (
        f'<clipPath id="disque"><circle cx="256" cy="256" r="236"/></clipPath>'
        f'<g clip-path="url(#disque)">'
        f'<rect width="512" height="512" fill="{CREAM}"/>'
        + rays +
        f'<path d="M{cx - 88} {cy} A88 88 0 0 1 {cx + 88} {cy} Z" fill="url(#soleil)"/>'
        # terre et chemin qui part vers le soleil
        f'<rect x="0" y="{cy}" width="512" height="220" fill="{GREEN}"/>'
        f'<path d="M206 512 Q236 380 252 {cy} L260 {cy} Q290 380 330 512 Z" fill="{CREAM}"/>'
        f'<path d="M256 506 Q256 420 256 {cy + 8}" fill="none" stroke="{SUN_A}" stroke-width="6" stroke-dasharray="18 16" stroke-linecap="round"/>'
        f'</g>'
        f'<circle cx="256" cy="256" r="236" fill="none" stroke="{NAVY}" stroke-width="14"/>'
        f'<line x1="26" y1="{cy}" x2="486" y2="{cy}" stroke="{NAVY}" stroke-width="8"/>'
    )
    return svg(512, 512, body)


# --------------------------------------------------------------- présentation
def lockup(symbol_svg, w=1200, h=420):
    """Symbole + nom de l'appli, pour voir le logo complet."""
    inner = symbol_svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    body = (
        f'<g transform="translate(40 30) scale(0.70)">{inner}</g>'
        f'<text x="440" y="226" font-family="{FONT}" font-weight="600" font-size="128" fill="{NAVY}">Bob\'s</text>'
        f'<text x="440" y="336" font-family="{FONT}" font-weight="600" font-size="128" fill="{HOPE}">Hands</text>'
    )
    return svg(w, h, body)


def save(name, content):
    (OUT / f"{name}.svg").write_text(content, encoding="utf-8")
    cairosvg.svg2png(bytestring=content.encode(), write_to=str(OUT / f"{name}.png"))


def board(items):
    W, PAD, TH = 1500, 36, 420
    H = PAD + len(items) * (TH + PAD)
    out = [f'<rect width="{W}" height="{H}" fill="#F4F7FB"/>']
    for i, (label, sym) in enumerate(items):
        y = PAD + i * (TH + PAD)
        inner = lockup(sym).split(">", 1)[1].rsplit("</svg>", 1)[0]
        out.append(
            f'<rect x="{PAD}" y="{y}" width="{W - 2 * PAD}" height="{TH}" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
            f'<g transform="translate({PAD} {y})">{inner}</g>'
            f'<text x="{W - PAD - 40}" y="{y + 60}" text-anchor="end" font-family="{FONT}" '
            f'font-weight="500" font-size="34" fill="#6B7A90">{label}</text>')
    cairosvg.svg2png(bytestring=svg(W, H, "".join(out)).encode(),
                     write_to=str(OUT / "planche-logos-v2.png"))


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = [("A · L'envol", envol()), ("B · La fenêtre", fenetre()), ("C · La voix", voix())]
    for label, sym in items:
        slug = label.split("·")[0].strip()
        save(f"{slug}-symbole", sym)
        save(f"{slug}-logo-complet", lockup(sym))
    board(items)
    print(f"Propositions -> {OUT}")


if __name__ == "__main__":
    build()
