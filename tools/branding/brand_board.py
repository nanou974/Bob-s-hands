#!/usr/bin/env python3
"""
Planche d'identité visuelle (branding board) de Bob's Hands.

Rassemble les trois logos officiels, la police Fredoka et la palette.
Sortie : assets/pictures/branding/brand-board.svg / .png
Usage : python3 tools/branding/brand_board.py
"""

from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
BR = ROOT / "assets" / "pictures" / "branding"
FONT = "Fredoka"

NAVY = "#22314D"
HOPE = "#3E8EE0"
GREY = "#6B7A90"
BG = "#F4F7FB"
CARD = "#FFFFFF"
LINE = "#E3E8F0"

W, H = 2400, 1720
M, GAP = 80, 40


def inner(name):
    s = (BR / name).read_text(encoding="utf-8")
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]


def card(x, y, w, h, title=None):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="32" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>'
    if title:
        out += (f'<text x="{x + 40}" y="{y + 60}" font-family="{FONT}" font-weight="500" '
                f'font-size="26" letter-spacing="3" fill="{GREY}">{title.upper()}</text>')
    return out


def text(x, y, s, size, weight=400, color=NAVY, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-weight="{weight}" font-size="{size}" '
            f'fill="{color}" text-anchor="{anchor}" {extra}>{s}</text>')


def build():
    out = [f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    # ---------------------------------------------------------- en-tête
    out.append(text(M, 130, "Bob's", 84, 600, NAVY) + text(M + 220, 130, "Hands", 84, 600, HOPE))
    out.append(text(M, 180, "Planche d'identité visuelle", 34, 500, GREY))
    out.append(text(W - M, 130, "Des yeux et des mains.", 40, 500, NAVY, "end"))
    out.append(text(W - M, 180, "Bob's Hands · Bob is hands", 30, 400, GREY, "end"))

    # ---------------------------------------------------------- logos
    y0, ch = 230, 660
    wm, wh = 560, 1040
    x1, x2, x3 = M, M + wm + GAP, M + wm + GAP + wh + GAP
    out.append(card(x1, y0, wm, ch, "Monogramme"))
    out.append(f'<g transform="translate({x1 + (wm - 470) / 2} {y0 + 110}) scale({470 / 512})">{inner("logo-monogramme.svg")}</g>')
    out.append(text(x1 + wm / 2, y0 + ch - 34, "Icône d'appli · profil · favicon", 24, 400, GREY, "middle"))

    out.append(card(x2, y0, wh, ch, "Logo horizontal"))
    s = 0.96
    out.append(f'<g transform="translate({x2 + (wh - 840 * s) / 2} {y0 + 130}) scale({s})">{inner("logo-horizontal.svg")}</g>')
    out.append(text(x2 + wh / 2, y0 + ch - 34, "Bannière GitHub · en-têtes · signatures", 24, 400, GREY, "middle"))

    out.append(card(x3, y0, wm, ch, "Logo vertical"))
    s = 0.60
    out.append(f'<g transform="translate({x3 + (wm - 640 * s) / 2} {y0 + 96}) scale({s})">{inner("logo-vertical.svg")}</g>')
    out.append(text(x3 + wm / 2, y0 + ch - 34, "Démarrage · affiche · Play Store", 24, 400, GREY, "middle"))

    # ---------------------------------------------------------- typographie
    y1 = y0 + ch + GAP
    tw, th = 1180, H - y1 - M
    out.append(card(M, y1, tw, th, "Typographie"))
    tx = M + 40
    out.append(text(tx - 6, y1 + 300, "Aa", 250, 600, NAVY))
    out.append(text(tx + 330, y1 + 150, "Fredoka", 72, 600, NAVY))
    out.append(text(tx + 330, y1 + 196, "Google Fonts · licence SIL Open Font", 26, 400, GREY))
    sample = "Bob est les mains et les yeux"
    for i, (label, wgt) in enumerate([("Regular 400", 400), ("Medium 500", 500), ("SemiBold 600", 600)]):
        yy = y1 + 252 + i * 50
        out.append(text(tx + 330, yy, label, 24, 500, GREY))
        out.append(text(tx + 520, yy, sample, 32, wgt, NAVY))
    out.append(f'<line x1="{tx}" y1="{y1 + 430}" x2="{M + tw - 40}" y2="{y1 + 430}" stroke="{LINE}" stroke-width="2"/>')
    out.append(text(tx, y1 + 490, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 40, 500, NAVY))
    out.append(text(tx, y1 + 546, "abcdefghijklmnopqrstuvwxyz àéèêçô", 40, 500, NAVY))
    out.append(text(tx, y1 + 602, "0123456789  ! ? « » , . ' &amp;", 40, 500, NAVY))
    out.append(text(tx, y1 + 660, "Titres et nom : SemiBold 600 · Textes : Regular 400 / Medium 500", 24, 400, GREY))

    # ---------------------------------------------------------- couleurs
    cx0 = M + tw + GAP
    cw = W - M - cx0
    out.append(card(cx0, y1, cw, th, "Couleurs"))
    out.append('<defs><linearGradient id="bb-or" x1="0" y1="0" x2="1" y2="1">'
               '<stop offset="0" stop-color="#F7D58C"/><stop offset="1" stop-color="#D99A3A"/></linearGradient>'
               '<linearGradient id="bb-verre" x1="0" y1="0" x2="1" y2="1">'
               '<stop offset="0" stop-color="#EAF6FF"/><stop offset="1" stop-color="#CFE6F7"/></linearGradient></defs>')
    colors = [
        ("Bleu nuit", NAVY, NAVY, "Contours · « Bob's » · B"),
        ("Bleu vif", HOPE, HOPE, "« Hands » · H · accents"),
        ("Or du cadre", "url(#bb-or)", "#F7D58C à #D99A3A", "Cadre du miroir"),
        ("Verre", "url(#bb-verre)", "#EAF6FF à #CFE6F7", "Fond du miroir"),
        ("Peau", "#F2D2B6", "#F2D2B6", "Visage · mains"),
        ("Fond clair", BG, BG, "Arrière-plans"),
    ]
    cols, sw, sh = 3, (cw - 80 - 2 * 32) / 3, 160
    for i, (name, fill, code, use) in enumerate(colors):
        col, row = i % cols, i // cols
        x = cx0 + 40 + col * (sw + 32)
        y = y1 + 96 + row * (sh + 126)
        out.append(f'<rect x="{x}" y="{y}" width="{sw}" height="{sh}" rx="24" fill="{fill}" stroke="{LINE}" stroke-width="2"/>')
        out.append(text(x, y + sh + 42, name, 30, 600, NAVY))
        out.append(text(x, y + sh + 76, code, 22, 500, GREY))
        out.append(text(x, y + sh + 106, use, 21, 400, GREY))

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}">{"".join(out)}</svg>')
    (BR / "brand-board.svg").write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(BR / "brand-board.png"))
    print(f"-> {BR / 'brand-board.png'}")


if __name__ == "__main__":
    build()
