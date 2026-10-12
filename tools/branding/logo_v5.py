#!/usr/bin/env python3
"""
Logo Bob's Hands — série 5 : le miroir, mains et téléphone au premier plan.

Le téléphone et les mains sont réels, devant le miroir. Dans le miroir, il n'y
a que le visage : le reflet de l'utilisateur, qui regarde le téléphone. Le
téléphone cache le bas du visage, seuls les yeux restent visibles.
Bob est ce reflet, et ses mains sortent du miroir pour tenir le téléphone.

Variantes :
  1 · ovale    miroir ovale, cadre doré
  2 · rond     miroir rond (format icône)
  3 · lumiere  miroir rond, lueur de l'écran sur le visage reflété

Sorties : assets/pictures/branding/propositions-v5/
Usage : python3 tools/branding/logo_v5.py
"""

import sys
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "branding"))
import logo_v3 as V3  # noqa: E402
import logo_v4 as V4  # noqa: E402

OUT = ROOT / "assets" / "pictures" / "branding" / "propositions-v5"
NAVY, HOPE, FONT = V3.NAVY, V3.HOPE, V3.FONT


def reflection(glow=False):
    """Le visage seul (tête, cou, épaules), retourné comme dans un miroir."""
    p = V3
    body = (p.person(p.SKIN, NAVY, 7, p.HAIR, p.SWEATER, p.SKIN_SHADE)
            + (p.screen_glow() if glow else "")
            + p.eyes(NAVY, "#FFFFFF", "#4A3A2E"))
    return f'<g transform="translate(512 0) scale(-1 1)">{body}</g>'


def foreground():
    """Le téléphone (vu de dos) et les mains, hors du miroir."""
    p = V3
    return (p.phone_back(NAVY, NAVY, 0)
            + p.hand(p.SKIN, NAVY, 7, -1) + p.hand(p.SKIN, NAVY, 7, 1))


def mirror(shape, glow=False):
    if shape == "ovale":
        # Le miroir occupe presque toute la hauteur de l'image
        cx, cy, rx, ry = 256, 256, 196, 246
        place = "translate(-77 -48) scale(1.30)"
        front_scale, front_dx, front_dy = 1.15, -38, -70
    else:
        cx, cy, rx, ry = 256, 214, 196, 196
        place = "translate(40 40) scale(0.84)"
        front_scale, front_dx, front_dy = 1.10, -26, -44
    glass = (f'<clipPath id="glace"><ellipse cx="{cx}" cy="{cy}" rx="{rx - 20}" ry="{ry - 20}"/></clipPath>'
             f'<g clip-path="url(#glace)">'
             f'<rect width="512" height="512" fill="url(#fond-miroir)"/>'
             f'<g transform="{place}">{reflection(glow)}</g>'
             + V4.glass(cx - rx, cy - ry, cx + rx, cy + ry) + '</g>')
    frame = (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 10}" ry="{ry - 10}" fill="none" stroke="url(#cadre)" stroke-width="20"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{NAVY}" stroke-width="8"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 20}" ry="{ry - 20}" fill="none" stroke="{NAVY}" stroke-width="6"/>')
    # Premier plan, légèrement agrandi : le téléphone cache le bas du visage,
    # seuls les yeux dépassent au-dessus de lui
    front = (f'<g transform="translate({front_dx} {front_dy}) scale({front_scale})">'
             f'{foreground()}</g>')
    body = (f'<clipPath id="cadre-total"><rect width="512" height="512"/></clipPath>'
            f'<g clip-path="url(#cadre-total)">{glass}{frame}{front}</g>')
    return V4.svg(512, 512, body)


def lockup_h(sym):
    """Logo complet horizontal : miroir à gauche, nom à droite, mise en page serrée."""
    inner = sym.split(">", 1)[1].rsplit("</svg>", 1)[0]
    return V4.svg(840, 400,
                  f'<g transform="translate(0 6) scale(0.76)">{inner}</g>'
                  f'<text x="376" y="196" font-family="{FONT}" font-weight="600" font-size="132" fill="{NAVY}">Bob\'s</text>'
                  f'<text x="376" y="320" font-family="{FONT}" font-weight="600" font-size="132" fill="{HOPE}">Hands</text>')


def lockup_v(sym):
    """Logo complet vertical : miroir au-dessus, nom en dessous."""
    inner = sym.split(">", 1)[1].rsplit("</svg>", 1)[0]
    return V4.svg(640, 820,
                  f'<g transform="translate(64 0) scale(1.0)">{inner}</g>'
                  f'<text x="320" y="652" text-anchor="middle" font-family="{FONT}" font-weight="600" '
                  f'font-size="120" fill="{NAVY}">Bob\'s</text>'
                  f'<text x="320" y="778" text-anchor="middle" font-family="{FONT}" font-weight="600" '
                  f'font-size="120" fill="{HOPE}">Hands</text>')


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = [("1 · Ovale", "ovale", mirror("ovale")),
             ("2 · Rond", "rond", mirror("rond")),
             ("3 · Lumière", "lumiere", mirror("rond", glow=True))]
    for label, slug, sym in items:
        (OUT / f"{label[0]}-{slug}-symbole.svg").write_text(sym, encoding="utf-8")
        cairosvg.svg2png(bytestring=sym.encode(), write_to=str(OUT / f"{label[0]}-{slug}-symbole.png"))
        full = lockup_h(sym)
        (OUT / f"{label[0]}-{slug}-logo-complet.svg").write_text(full, encoding="utf-8")
        cairosvg.svg2png(bytestring=full.encode(), write_to=str(OUT / f"{label[0]}-{slug}-logo-complet.png"))
    vert = lockup_v(items[0][2])
    (OUT / "1-ovale-logo-vertical.svg").write_text(vert, encoding="utf-8")
    cairosvg.svg2png(bytestring=vert.encode(), write_to=str(OUT / "1-ovale-logo-vertical.png"))
    V4.OUT = OUT
    V4.board(items, items[0][2])
    (OUT / "planche-logos-v4.png").rename(OUT / "planche-logos-v5.png")
    print(f"Propositions -> {OUT}")


if __name__ == "__main__":
    build()
