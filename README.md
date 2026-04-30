<!DOCTYPE html>

<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>elopin42 — 42 Paris</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Departure+Mono&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0d0e14;
    --bg2: #12131a;
    --panel: #181922;
    --border: #2a2d3e;
    --green: #a6e3a1;
    --blue: #89b4fa;
    --mauve: #cba6f7;
    --peach: #fab387;
    --yellow: #f9e2af;
    --red: #f38ba8;
    --teal: #94e2d5;
    --sky: #89dceb;
    --text: #cdd6f4;
    --subtext: #a6adc8;
    --muted: #585b70;
    --glow-green: 0 0 20px rgba(166,227,161,0.3);
    --glow-blue: 0 0 20px rgba(137,180,250,0.3);
    --glow-mauve: 0 0 20px rgba(203,166,247,0.3);
  }

- { margin: 0; padding: 0; box-sizing: border-box; }

body {
background: var(–bg);
color: var(–text);
font-family: ‘JetBrains Mono’, monospace;
min-height: 100vh;
overflow-x: hidden;
cursor: none;
}

/* Custom cursor */
.cursor {
width: 8px; height: 16px;
background: var(–green);
position: fixed;
pointer-events: none;
z-index: 9999;
animation: blink 1s step-end infinite;
box-shadow: var(–glow-green);
transition: opacity 0.1s;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

/* Scanlines overlay */
body::after {
content: ‘’;
position: fixed; inset: 0;
background: repeating-linear-gradient(
0deg,
transparent,
transparent 2px,
rgba(0,0,0,0.08) 2px,
rgba(0,0,0,0.08) 4px
);
pointer-events: none;
z-index: 1000;
}

/* Noise texture */
body::before {
content: ‘’;
position: fixed; inset: 0;
background-image: url(“data:image/svg+xml,%3Csvg viewBox=‘0 0 200 200’ xmlns=‘http://www.w3.org/2000/svg’%3E%3Cfilter id=‘n’%3E%3CfeTurbulence type=‘fractalNoise’ baseFrequency=‘0.9’ numOctaves=‘4’ stitchTiles=‘stitch’/%3E%3C/filter%3E%3Crect width=‘100%25’ height=‘100%25’ filter=‘url(%23n)’ opacity=‘0.04’/%3E%3C/svg%3E”);
pointer-events: none;
z-index: 999;
opacity: 0.4;
}

.container {
max-width: 960px;
margin: 0 auto;
padding: 40px 24px;
position: relative;
}

/* Top bar */
.topbar {
display: flex; align-items: center; gap: 8px;
margin-bottom: 40px;
opacity: 0;
animation: fadeIn 0.5s ease forwards 0.2s;
}
.dot { width:12px; height:12px; border-radius:50%; }
.dot-r { background: var(–red); box-shadow: 0 0 8px rgba(243,139,168,0.6); }
.dot-y { background: var(–yellow); box-shadow: 0 0 8px rgba(249,226,175,0.6); }
.dot-g { background: var(–green); box-shadow: 0 0 8px rgba(166,227,161,0.6); }
.topbar-title {
margin-left: 12px;
font-size: 11px;
color: var(–muted);
letter-spacing: 0.15em;
text-transform: uppercase;
}
.topbar-path { color: var(–subtext); margin-left: 4px; }

/* Header */
.header {
display: grid;
grid-template-columns: 1fr 1fr;
gap: 24px;
margin-bottom: 32px;
}

.ascii-block {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 20px;
position: relative;
overflow: hidden;
opacity: 0;
animation: slideUp 0.6s ease forwards 0.3s;
}
.ascii-block::before {
content: ‘’;
position: absolute; top: 0; left: 0; right: 0; height: 1px;
background: linear-gradient(90deg, transparent, var(–green), transparent);
}

pre.ascii {
font-size: 7px;
line-height: 1.2;
color: var(–mauve);
text-shadow: var(–glow-mauve);
font-family: ‘JetBrains Mono’, monospace;
}

.info-block {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 20px 24px;
display: flex; flex-direction: column; justify-content: center;
gap: 10px;
opacity: 0;
animation: slideUp 0.6s ease forwards 0.45s;
position: relative;
overflow: hidden;
}
.info-block::before {
content: ‘’;
position: absolute; top: 0; left: 0; right: 0; height: 1px;
background: linear-gradient(90deg, transparent, var(–blue), transparent);
}

.info-line {
display: flex; align-items: baseline; gap: 8px;
font-size: 12px;
}
.info-key { color: var(–blue); min-width: 70px; }
.info-sep { color: var(–muted); }
.info-val { color: var(–text); }
.info-val.highlight { color: var(–green); font-weight: 700; }
.info-val.mauve { color: var(–mauve); }
.info-val.peach { color: var(–peach); }

.prompt-line {
margin-top: 8px;
font-size: 12px;
color: var(–muted);
display: flex; align-items: center; gap: 6px;
}
.prompt-sym { color: var(–green); }
.prompt-user { color: var(–mauve); }
.prompt-at { color: var(–muted); }
.prompt-host { color: var(–blue); }
.prompt-dir { color: var(–yellow); }

/* Section title */
.section-label {
font-size: 10px;
letter-spacing: 0.2em;
text-transform: uppercase;
color: var(–muted);
margin-bottom: 12px;
display: flex; align-items: center; gap: 8px;
}
.section-label::after {
content: ‘’;
flex: 1; height: 1px;
background: var(–border);
}
.section-label span { color: var(–green); }

/* Stats bar */
.stats-grid {
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 12px;
margin-bottom: 24px;
opacity: 0;
animation: slideUp 0.6s ease forwards 0.6s;
}

.stat-card {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 16px;
text-align: center;
transition: border-color 0.3s, box-shadow 0.3s;
position: relative;
overflow: hidden;
}
.stat-card:hover {
border-color: var(–blue);
box-shadow: var(–glow-blue);
}
.stat-card::after {
content: ‘’;
position: absolute; bottom: 0; left: 0; right: 0; height: 2px;
background: var(–blue);
transform: scaleX(0);
transition: transform 0.3s;
}
.stat-card:hover::after { transform: scaleX(1); }
.stat-num {
font-size: 28px;
font-weight: 700;
color: var(–green);
text-shadow: var(–glow-green);
display: block;
font-family: ‘JetBrains Mono’, monospace;
}
.stat-label {
font-size: 10px;
color: var(–muted);
letter-spacing: 0.1em;
text-transform: uppercase;
margin-top: 4px;
}

/* Skills / Tech */
.skills-block {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 20px;
margin-bottom: 24px;
opacity: 0;
animation: slideUp 0.6s ease forwards 0.75s;
}

.skill-row {
display: flex; align-items: center; gap: 12px;
margin-bottom: 10px;
}
.skill-name {
font-size: 11px;
color: var(–subtext);
min-width: 80px;
}
.skill-bar {
flex: 1; height: 4px;
background: var(–border);
border-radius: 2px;
overflow: hidden;
}
.skill-fill {
height: 100%;
border-radius: 2px;
width: 0;
transition: width 1.2s cubic-bezier(0.25,1,0.5,1);
}
.skill-fill.c    { background: var(–blue); box-shadow: 0 0 8px rgba(137,180,250,0.5); }
.skill-fill.cpp  { background: var(–mauve); box-shadow: 0 0 8px rgba(203,166,247,0.5); }
.skill-fill.py   { background: var(–green); box-shadow: 0 0 8px rgba(166,227,161,0.5); }
.skill-fill.erp  { background: var(–peach); box-shadow: 0 0 8px rgba(250,179,135,0.5); }
.skill-fill.sh   { background: var(–teal); box-shadow: 0 0 8px rgba(148,226,213,0.5); }
.skill-pct {
font-size: 10px;
color: var(–muted);
min-width: 32px;
text-align: right;
}

/* Projects / focus */
.two-col {
display: grid;
grid-template-columns: 1fr 1fr;
gap: 12px;
margin-bottom: 24px;
opacity: 0;
animation: slideUp 0.6s ease forwards 0.9s;
}

.card {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 16px;
transition: border-color 0.3s, transform 0.3s;
}
.card:hover {
border-color: var(–mauve);
transform: translateY(-2px);
box-shadow: var(–glow-mauve);
}
.card-tag {
font-size: 9px;
letter-spacing: 0.15em;
text-transform: uppercase;
color: var(–mauve);
margin-bottom: 6px;
}
.card-title {
font-size: 14px;
color: var(–text);
font-weight: 500;
margin-bottom: 6px;
}
.card-desc {
font-size: 10px;
color: var(–subtext);
line-height: 1.6;
}

/* Footer / contact */
.footer-block {
background: var(–panel);
border: 1px solid var(–border);
border-radius: 4px;
padding: 20px 24px;
display: flex; align-items: center; justify-content: space-between;
opacity: 0;
animation: slideUp 0.6s ease forwards 1.05s;
}

.contact-line {
font-size: 11px;
color: var(–subtext);
display: flex; align-items: center; gap: 8px;
}
.contact-link {
color: var(–green);
text-decoration: none;
transition: text-shadow 0.3s;
}
.contact-link:hover { text-shadow: var(–glow-green); }

.badge-row {
display: flex; gap: 8px;
}
.badge {
font-size: 9px;
padding: 3px 8px;
border-radius: 2px;
letter-spacing: 0.1em;
text-transform: uppercase;
border: 1px solid;
}
.badge-arch { color: var(–sky); border-color: var(–sky); }
.badge-nvim { color: var(–green); border-color: var(–green); }
.badge-42   { color: var(–mauve); border-color: var(–mauve); }

/* Blinking underline for live feel */
.live-dot {
display: inline-block;
width: 6px; height: 6px; border-radius: 50%;
background: var(–green);
box-shadow: var(–glow-green);
animation: pulse 2s ease-in-out infinite;
vertical-align: middle;
}
@keyframes pulse {
0%,100% { opacity:1; transform:scale(1); }
50% { opacity:0.4; transform:scale(0.7); }
}

@keyframes fadeIn { from{opacity:0} to{opacity:1} }
@keyframes slideUp {
from { opacity:0; transform:translateY(16px); }
to   { opacity:1; transform:translateY(0); }
}

/* Responsive */
@media(max-width:640px) {
.header { grid-template-columns: 1fr; }
.two-col { grid-template-columns: 1fr; }
.stats-grid { grid-template-columns: repeat(3,1fr); }
pre.ascii { font-size: 5px; }
}
</style>

</head>
<body>

<div class="cursor" id="cursor"></div>

<div class="container">

  <!-- Top bar -->

  <div class="topbar">
    <div class="dot dot-r"></div>
    <div class="dot dot-y"></div>
    <div class="dot dot-g"></div>
    <span class="topbar-title">terminal <span class="topbar-path">~/elopin42</span></span>
    <span style="margin-left:auto;font-size:10px;color:var(--muted)"><span class="live-dot"></span> online</span>
  </div>

  <!-- Header: ASCII + Info -->

  <div class="header">
    <div class="ascii-block">
      <pre class="ascii">                     -`
                    .o+`
                   `ooo/
                  `+oooo:
                 `+oooooo:
                 -+oooooo+:
               `/:-:++oooo+:
              `/++++/+++++++:
             `/++++++++++++++:
            `/+++ooooooooooooo/`
           ./ooosssso++osssssso+`
          .oossssso-````/ossssss+`
         -osssssso.      :ssssssso.
        :osssssss/        osssso+++
       /ossssssss/        +ssssooo/-
     `/ossssso+/:-        -:/+osssso+-
    `+sso+:-`                `.-/+oso:
   `++:.                           `-/+/
   .`                                 `</pre>
    </div>

```
<div class="info-block">
  <div class="prompt-line">
    <span class="prompt-sym">❯</span>
    <span class="prompt-user">ethan</span><span class="prompt-at">@</span><span class="prompt-host">42paris</span>
    <span class="prompt-dir">~/profile</span>
  </div>

  <div style="height:1px;background:var(--border);margin:4px 0;"></div>

  <div class="info-line">
    <span class="info-key">name</span>
    <span class="info-sep">=</span>
    <span class="info-val highlight">Ethan Lopin</span>
  </div>
  <div class="info-line">
    <span class="info-key">role</span>
    <span class="info-sep">=</span>
    <span class="info-val mauve">student @ 42 Paris</span>
  </div>
  <div class="info-line">
    <span class="info-key">focus</span>
    <span class="info-sep">=</span>
    <span class="info-val peach">ERP · CRM · Systems</span>
  </div>
  <div class="info-line">
    <span class="info-key">stack</span>
    <span class="info-sep">=</span>
    <span class="info-val" style="color:var(--sky)">Django · Tryton · Odoo</span>
  </div>
  <div class="info-line">
    <span class="info-key">os</span>
    <span class="info-sep">=</span>
    <span class="info-val">Arch Linux / Hyprland</span>
  </div>
  <div class="info-line">
    <span class="info-key">editor</span>
    <span class="info-sep">=</span>
    <span class="info-val">Neovim</span>
  </div>
  <div class="info-line">
    <span class="info-key">mail</span>
    <span class="info-sep">=</span>
    <a class="contact-link" href="mailto:ethan@42entrepreneurs.com" style="font-size:12px;">ethan@42entrepreneurs.com</a>
  </div>
</div>
```

  </div>

  <!-- Stats -->

  <div class="section-label"><span>#</span> 42 network</div>
  <div class="stats-grid">
    <div class="stat-card">
      <span class="stat-num" data-target="21">0</span>
      <div class="stat-label">cursus id</div>
    </div>
    <div class="stat-card">
      <span class="stat-num" data-target="45">0</span>
      <div class="stat-label">coalition</div>
    </div>
    <div class="stat-card">
      <span class="stat-num" data-target="42">0</span>
      <div class="stat-label">school</div>
    </div>
  </div>

  <!-- Skills -->

  <div class="section-label"><span>#</span> stack</div>
  <div class="skills-block">
    <div class="skill-row">
      <span class="skill-name">C</span>
      <div class="skill-bar"><div class="skill-fill c" data-w="88"></div></div>
      <span class="skill-pct">88%</span>
    </div>
    <div class="skill-row">
      <span class="skill-name">C++</span>
      <div class="skill-bar"><div class="skill-fill cpp" data-w="75"></div></div>
      <span class="skill-pct">75%</span>
    </div>
    <div class="skill-row">
      <span class="skill-name">Python</span>
      <div class="skill-bar"><div class="skill-fill py" data-w="82"></div></div>
      <span class="skill-pct">82%</span>
    </div>
    <div class="skill-row">
      <span class="skill-name">ERP/CRM</span>
      <div class="skill-bar"><div class="skill-fill erp" data-w="70"></div></div>
      <span class="skill-pct">70%</span>
    </div>
    <div class="skill-row">
      <span class="skill-name">Bash</span>
      <div class="skill-bar"><div class="skill-fill sh" data-w="65"></div></div>
      <span class="skill-pct">65%</span>
    </div>
  </div>

  <!-- Focus cards -->

  <div class="section-label"><span>#</span> focus</div>
  <div class="two-col">
    <div class="card">
      <div class="card-tag">// erp</div>
      <div class="card-title">Odoo 19 CE · Tryton</div>
      <div class="card-desc">Développement et customisation d'ERP/CRM open-source. Modules métier, intégrations API, workflow automation.</div>
    </div>
    <div class="card">
      <div class="card-tag">// 42</div>
      <div class="card-title">42 Paris Curriculum</div>
      <div class="card-desc">Projets système bas-niveau en C/C++. Algorithmie, gestion mémoire, programmation réseau et concurrence.</div>
    </div>
    <div class="card">
      <div class="card-tag">// web</div>
      <div class="card-title">Django Framework</div>
      <div class="card-desc">Backend Python robuste. ORM, REST APIs, architecture MVC pour des applications métier scalables.</div>
    </div>
    <div class="card">
      <div class="card-tag">// env</div>
      <div class="card-title">Arch · Hyprland · Neovim</div>
      <div class="card-desc">Environnement de développement entièrement configuré. dotfiles, scripts, workflow terminal-first.</div>
    </div>
  </div>

  <!-- Footer -->

  <div class="section-label"><span>#</span> contact</div>
  <div class="footer-block">
    <div class="contact-line">
      <span style="color:var(--muted)">❯</span>
      <span>reach out →</span>
      <a href="mailto:ethan@42entrepreneurs.com" class="contact-link">ethan@42entrepreneurs.com</a>
    </div>
    <div class="badge-row">
      <span class="badge badge-arch">arch</span>
      <span class="badge badge-nvim">nvim</span>
      <span class="badge badge-42">42</span>
    </div>
  </div>

</div>

<script>
  // Cursor
  const cursor = document.getElementById('cursor');
  document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top  = e.clientY - 8 + 'px';
  });

  // Animate stat counters
  function animateCounter(el) {
    const target = parseInt(el.dataset.target);
    let current = 0;
    const step = Math.ceil(target / 30);
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current;
      if (current >= target) clearInterval(timer);
    }, 40);
  }

  // Animate skill bars
  function animateBars() {
    document.querySelectorAll('.skill-fill').forEach(bar => {
      bar.style.width = bar.dataset.w + '%';
    });
  }

  // Trigger on load after animations
  setTimeout(() => {
    document.querySelectorAll('.stat-num').forEach(animateCounter);
    animateBars();
  }, 900);
</script>

</body>
</html>
