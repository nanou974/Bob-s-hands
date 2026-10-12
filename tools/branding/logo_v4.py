#!/usr/bin/env python3
"""
Logo Bob's Hands — série 4 : le miroir.

L'utilisateur ne peut pas tenir son téléphone. Quand il le regarde, il y voit
Bob : un reflet de lui-même qui tient le téléphone à sa place, le regarde et
le manipule. Bob est le reflet du téléphone aux yeux de l'utilisateur.

Le personnage reprend la série 3 (tools/branding/logo_v3.py), retourné comme
dans un miroir (le bloc photo passe de l'autre côté), teinté et traversé de
reflets de verre.

Variantes :
  1 · miroir     un miroir ovale, cadre doré
  2 · telephone  le téléphone lui-même est le miroir
  3 · lumiere    le téléphone-miroir, avec la lueur de l'écran sur le visage

Sorties : assets/pictures/branding/propositions-v4/
Usage : python3 tools/branding/logo_v4.py
"""

import sys
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "branding"))
import logo_v3 as V3  # noqa: E402

OUT = ROOT / "assets" / "pictures" / "branding" / "propositions-v4"
NAVY, HOPE, CREAM, FONT = V3.NAVY, V3.HOPE, V3.CREAM, V3.FONT
GOLD, GOLD_DARK = "#F2C066", "#D99A3A"

DEFS = """<defs>
  <linearGradient id="fond-miroir" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#EAF6FF"/><stop offset="1" stop-color="#CFE6F7"/></linearGradient>
  <linearGradient id="cadre" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#F7D58C"/><stop offset="1" stop-color="#D99A3A"/></linearGradient>
</defs>"""


def scene(glow=False):
    """Le personnage de la série 3, retourné comme dans un miroir."""
    p = V3
    body = (p.person(p.SKIN, NAVY, 7, p.HAIR, p.SWEATER, p.SKIN_SHADE)
            + (p.screen_glow() if glow else "")
            + p.eyes(NAVY, "#FFFFFF", "#4A3A2E")
            + p.phone_back(NAVY, NAVY, 0)
            + p.hand(p.SKIN, NAVY, 7, -1) + p.hand(p.SKIN, NAVY, 7, 1))
    return f'<g transform="translate(512 0) scale(-1 1)">{body}</g>'


def glass(x0, y0, x1, y1):
    """Reflets de verre : deux bandes claires en diagonale, et un voile bleuté."""
    w, h = x1 - x0, y1 - y0
    band = lambda a, b, op: (f'<path d="M{x0 + w * a} {y0} L{x0 + w * b} {y0} '
                             f'L{x0 + w * b - w * .55} {y1} L{x0 + w * a - w * .55} {y1} Z" '
                             f'fill="#FFFFFF" opacity="{op}"/>')
    return (f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#BFE3FA" opacity=".18"/>'
            + band(.62, .78, .38) + band(.84, .90, .30))


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">{V3.DEFS}{DEFS}{body}</svg>')


# ------------------------------------------------------------- 1 · miroir ovale
def miroir():
    cx, cy, rx, ry = 256, 256, 176, 232
    inner = (f'<clipPath id="glace"><ellipse cx="{cx}" cy="{cy}" rx="{rx - 22}" ry="{ry - 22}"/></clipPath>'
             f'<g clip-path="url(#glace)">'
             f'<rect width="512" height="512" fill="url(#fond-miroir)"/>'
             f'<g transform="translate(70 70) scale(0.74)">{scene()}</g>'
             + glass(cx - rx, cy - ry, cx + rx, cy + ry) + '</g>')
    frame = (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 11}" ry="{ry - 11}" fill="none" stroke="url(#cadre)" stroke-width="22"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{NAVY}" stroke-width="8"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 22}" ry="{ry - 22}" fill="none" stroke="{NAVY}" stroke-width="6"/>')
    return svg(512, 512, inner + frame)


# ------------------------------------------------------------- 2 · téléphone-miroir
def telephone(glow=False):
    x, y, w, h, r = 120, 16, 272, 480, 52
    sx, sy, sw, sh, sr = x + 16, y + 16, w - 32, h - 32, 38
    body = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{NAVY}"/>'
            f'<clipPath id="ecran-miroir"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{sr}"/></clipPath>'
            f'<g clip-path="url(#ecran-miroir)">'
            f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="url(#fond-miroir)"/>'
            f'<g transform="translate(56 94) scale(0.78)">{scene(glow)}</g>'
            + glass(sx, sy, sx + sw, sy + sh) + '</g>'
            # caméra frontale
            f'<circle cx="256" cy="{sy + 22}" r="9" fill="{NAVY}"/>'
            f'<circle cx="259" cy="{sy + 19}" r="3" fill="#5A6B8C"/>'
            # boutons latéraux
            f'<rect x="{x + w - 2}" y="130" width="8" height="64" rx="4" fill="{NAVY}"/>'
            f'<rect x="{x - 6}" y="110" width="8" height="40" rx="4" fill="{NAVY}"/>'
            f'<rect x="{x - 6}" y="162" width="8" height="40" rx="4" fill="{NAVY}"/>')
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


def board(items, featured):
    W, PAD = 1560, 36
    tile = (W - PAD * 4) // 3
    H = PAD + tile + 70 + PAD + 420 + PAD
    out = [f'<rect width="{W}" height="{H}" fill="#F4F7FB"/>']
    for i, (label, _, sym) in enumerate(items):
        x = PAD + i * (tile + PAD)
        inner = sym.split(">", 1)[1].rsplit("</svg>", 1)[0]
        out.append(
            f'<rect x="{x}" y="{PAD}" width="{tile}" height="{tile + 70}" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
            f'<g transform="translate({x + 24} {PAD + 24}) scale({(tile - 48) / 512})">{inner}</g>'
            f'<text x="{x + tile / 2}" y="{PAD + tile + 46}" text-anchor="middle" font-family="{FONT}" '
            f'font-weight="500" font-size="30" fill="{NAVY}">{label}</text>')
    y = PAD + tile + 70 + PAD
    inner = lockup(featured).split(">", 1)[1].rsplit("</svg>", 1)[0]
    out.append(f'<rect x="{PAD}" y="{y}" width="{W - 2 * PAD}" height="420" rx="28" fill="#fff" stroke="#E3E8F0" stroke-width="2"/>'
               f'<g transform="translate({(W - 1200) / 2 + 120} {y})">{inner}</g>')
    cairosvg.svg2png(bytestring=svg(W, H, "".join(out)).encode(),
                     write_to=str(OUT / "planche-logos-v4.png"))


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = [("1 · Miroir", "miroir", miroir()),
             ("2 · Téléphone-miroir", "telephone", telephone()),
             ("3 · Lumière", "lumiere", telephone(glow=True))]
    for label, slug, sym in items:
        save(f"{label[0]}-{slug}-symbole", sym)
        save(f"{label[0]}-{slug}-logo-complet", lockup(sym))
    board(items, items[1][2])
    print(f"Propositions -> {OUT}")


if __name__ == "__main__":
    build()
