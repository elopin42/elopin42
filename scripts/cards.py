"""Generate README SVGs for github.com/elopin42 (header + project cards)."""
import sys
from pathlib import Path
from html import escape

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

# ink ramp, amber accent (kept from the existing brand)
BG = "#0e0f12"
SURF = "#15161a"
LINE = "rgba(236,233,227,0.08)"
T1 = "#ece9e3"
T2 = "#a3a6ae"
T3 = "#6f727b"
ACC = "#e0b074"
SANS = "'Helvetica Neue', Helvetica, Arial, 'Liberation Sans', sans-serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace"


def e(s):
    return escape(s, quote=True)


def svg(w, h, body, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{e(label)}">
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="16" fill="{SURF}" stroke="{LINE}"/>
{body}
</svg>
'''


def lines(x, y, rows, size, color, lh, family=SANS, weight=400):
    out = []
    for i, r in enumerate(rows):
        out.append(f'<text x="{x}" y="{y + i*lh}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}">{e(r)}</text>')
    return "\n".join(out)


def card_head(x, tag, domain, w, title_size):
    return f'''<circle cx="{x+4}" cy="40" r="4" fill="{ACC}"/>
<text x="{x+16}" y="44.5" font-family="{MONO}" font-size="13" fill="{T3}">{e(tag)}</text>
<text x="{w-32}" y="45" text-anchor="end" font-family="{SANS}" font-size="16" fill="{T3}">↗</text>
<text x="{x}" y="{88 if title_size > 28 else 84}" font-family="{SANS}" font-size="{title_size}" font-weight="400" fill="{T1}">{e(domain)}</text>'''


# ---------- header ----------
header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Elopin, elopin42. 42 Paris. Six sites live, two built in 24 hours.">
<rect x="0.5" y="0.5" width="999" height="299" rx="16" fill="{BG}" stroke="{LINE}"/>
<g>
  <text x="56" y="76" font-family="{MONO}" font-size="14" fill="{T3}">github.com/elopin42</text>
  <text x="54" y="164" font-family="{SANS}" font-size="76" font-weight="400" letter-spacing="-1.5" fill="{T1}">Elopin<tspan fill="{ACC}">.</tspan></text>
  <text x="56" y="212" font-family="{SANS}" font-size="20" fill="{T2}">Student at 42 Paris. I write C for school and ship the web for real clients.</text>
  <line x1="56" y1="244" x2="944" y2="244" stroke="{LINE}"/>
  <g font-family="{MONO}" font-size="13" fill="{T3}">
    <circle cx="60" cy="267" r="4" fill="{ACC}"/>
    <text x="72" y="271.5"><tspan fill="{T2}">6</tspan> sites live</text>
    <text x="210" y="271.5"><tspan fill="{T2}">2</tspan> built in 24h</text>
    <text x="356" y="271.5">Saudi Arabia · Lisbon · Paris</text>
    <text x="944" y="271.5" text-anchor="end">Paris, FR</text>
  </g>
</g>
</svg>
'''
(OUT / "header.svg").write_text(header)


# ---------- featured cards (1000 x 240) with a product moment on the right ----------
def featured(name, tag, domain, desc, stack, moment, label):
    body = "\n".join([
        card_head(32, tag, domain, 1000, 34),
        lines(32, 128, desc, 16, T2, 24),
        f'<text x="32" y="208" font-family="{MONO}" font-size="13" fill="{T3}">{e("  ·  ".join(stack))}</text>',
        f'<line x1="600" y1="32" x2="600" y2="208" stroke="{LINE}"/>',
        moment,
    ])
    (OUT / f"{name}.svg").write_text(svg(1000, 240, body, label))


def box(x, y, w, h, text, accent=False):
    stroke = ACC if accent else "rgba(236,233,227,0.14)"
    fill = "rgba(224,176,116,0.08)" if accent else BG
    col = ACC if accent else T2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}"/>'
            f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{col}">{e(text)}</text>')


# SIPS: pharmacies pool into one tender, one supplier wins, each pharmacy gets its own delivery
P = "rgba(236,233,227,0.22)"
sips_m = [f'<text x="632" y="44" font-family="{MONO}" font-size="12" fill="{T3}">pooled tender</text>']
ys = [72, 120, 168]
for i, y in enumerate(ys):
    sips_m.append(box(632, y, 104, 32, f"pharmacy {'ABC'[i]}"))
    sips_m.append(f'<path d="M736 {y+16} C 760 {y+16}, 760 136, 780 136" fill="none" stroke="{P}"/>')
sips_m.append(box(780, 120, 72, 32, "RFQ", accent=True))
sips_m.append(f'<path d="M852 136 L 872 136" stroke="{ACC}"/>')
sips_m.append(box(872, 120, 96, 32, "1 supplier"))
sips_m.append(f'<text x="920" y="186" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{T3}">3 deliveries</text>')
sips_m.append(f'<path d="M920 152 L 920 172" stroke="{P}" stroke-dasharray="2 3"/>')
featured(
    "sips", "client · Saudi Arabia", "sips.sa",
    ["Purchasing network for Saudi pharmacies. Pharmacies pool",
     "their orders into one tender, suppliers bid once on the",
     "volume, and each pharmacy gets its own delivery."],
    ["Django", "Odoo 19", "PostgreSQL", "Redis", "Docker"],
    "\n".join(sips_m),
    "sips.sa, purchasing network for Saudi pharmacies",
)

# loprem: trailer brake pad wear per axle
lp = [f'<text x="632" y="44" font-family="{MONO}" font-size="12" fill="{T3}">trailer brake pads</text>']
axles = [("axle 1", 72), ("axle 2", 64), ("axle 3", 23)]
for i, (a, v) in enumerate(axles):
    y = 80 + i * 40
    low = v < 30
    lp.append(f'<text x="632" y="{y+4}" font-family="{MONO}" font-size="12" fill="{T2}">{a}</text>')
    lp.append(f'<rect x="700" y="{y-3}" width="208" height="6" rx="3" fill="rgba(236,233,227,0.08)"/>')
    lp.append(f'<rect x="700" y="{y-3}" width="{208*v/100:.0f}" height="6" rx="3" fill="{ACC if low else "rgba(236,233,227,0.45)"}"/>')
    lp.append(f'<text x="968" y="{y+4}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{ACC if low else T2}">{v}%</text>')
lp.append(f'<text x="632" y="208" font-family="{MONO}" font-size="11" fill="{T3}">Teltonika FMC650 · Codec 8E</text>')
featured(
    "loprem", "client · France", "loprem.fr",
    ["Fleet tracking for trucks. Live position and trailer brake",
     "pad wear, decoded straight from the Teltonika boxes over",
     "raw TCP, on a map split per company."],
    ["Django", "PostGIS", "TCP ingestion", "Leaflet"],
    "\n".join(lp),
    "loprem.fr, truck fleet tracking and brake pad wear",
)


# ---------- half cards (488 x 232) ----------
def half(name, tag, domain, desc, stack, label):
    body = "\n".join([
        card_head(28, tag, domain, 488, 26),
        lines(28, 120, desc, 15, T2, 22),
        f'<text x="28" y="200" font-family="{MONO}" font-size="12" fill="{T3}">{e("  ·  ".join(stack))}</text>',
    ])
    (OUT / f"{name}.svg").write_text(svg(488, 232, body, label))


half("coutrio", "product", "coutrio.com",
     ["Meet people from your own country, city or",
      "neighbourhood, wherever you live now."],
     ["globe map", "trip planner", "QR partner deals", "EN / FR"],
     "coutrio.com, connects people who share the same origins")
half("42entrepreneurs", "42 Paris club", "42entrepreneurs.com",
     ["Site of the 42 Paris entrepreneurs club. The",
      "school building in 3D, driven by the scroll."],
     ["Vite", "three.js", "anime.js", "Netlify"],
     "42entrepreneurs.com, site of the 42 Paris entrepreneurs club")
half("taskvault", "hackathon · 24h · Lisbon", "taskvault.art",
     ["Task board for freelancers. Each task is paid",
      "in USDC from its own escrow on Stellar."],
     ["Django", "Stellar", "USDC escrow", "Hack Meridian"],
     "taskvault.art, 24 hour hackathon in Lisbon")
half("darkdatagent", "hackathon · 24h · Paris", "darkdatagent.art",
     ["Turns a company's tutorial videos into agents",
      "that do the task by house rules."],
     ["Python", "Gladia", "H Company", "42AI"],
     "darkdatagent.art, 24 hour hackathon in Paris")
print("ok")
