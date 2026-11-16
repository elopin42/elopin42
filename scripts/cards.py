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

# ---------- site cards (488 x 120): tag, domain, nothing else ----------
SITES = [
    ("sips", "client · Saudi Arabia", "sips.sa"),
    ("loprem", "client · France", "loprem.fr"),
    ("coutrio", "product", "coutrio.com"),
    ("42entrepreneurs", "42 Paris club", "42entrepreneurs.com"),
    ("taskvault", "hackathon · 24h · Lisbon", "taskvault.art"),
    ("darkdatagent", "hackathon · 24h · Paris", "darkdatagent.art"),
]
for name, tag, domain in SITES:
    body = f'''<circle cx="32" cy="36" r="4" fill="{ACC}"/>
<text x="44" y="40.5" font-family="{MONO}" font-size="13" fill="{T3}">{e(tag)}</text>
<text x="456" y="41" text-anchor="end" font-family="{SANS}" font-size="16" fill="{T3}">↗</text>
<text x="28" y="88" font-family="{SANS}" font-size="28" font-weight="400" fill="{T1}">{e(domain)}</text>'''
    (OUT / f"{name}.svg").write_text(svg(488, 120, body, f"{domain}, {tag}"))
print("ok")
