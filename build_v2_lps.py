# Three NEW US pre-order pages. Deliberately DIFFERENT visual systems from the cream/serif
# gift page — different palettes, layouts, type and formats, so a split test measures the
# format, not a copy tweak.
import json, pathlib

CHECKOUT = ("https://hawknesthammocks.ca/cart/53200326557993:1,53198306312489:1,"
            "53198306345257:1,46948621254953:1,46948623810857:1,47874384953641:1?country=US")
R = json.load(open("/tmp/jm_us.json"))          # real Judge.me reviews, real photos
def rv(i): return R[i % len(R)]
UNITS = "9,000+"

def stars(n=5): return "★"*n

# ═════════════════════ 1. DARK EDITORIAL ═════════════════════
r0,r1,r2 = rv(8), rv(1), rv(0)      # Pat storm · Bob rain test · Andrew setup
P1 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sleep Above It | Hawk Nest V.3 — US Pre-Order</title>
<meta name="description" content="An all-season hammock-tent for people who are done sleeping on the ground. $159 pre-order, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=Archivo+Narrow:wght@600;700&display=swap" rel="stylesheet">
<style>
:root{{--ink:#0b0d0c;--ink2:#141816;--line:#2a302c;--white:#f4f2ec;--dim:#9aa39c;--amber:#e8933a;--go:#d97a1c}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--ink);color:var(--white);font-family:'Archivo',system-ui,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:720px;margin:0 auto;padding:0 20px}}
.hero{{min-height:78vh;display:flex;flex-direction:column;justify-content:flex-end;
 background:linear-gradient(180deg,rgba(11,13,12,.25),rgba(11,13,12,.9) 72%,var(--ink)),
 url('{r0["pic"]}') center/cover;padding:70px 0 42px}}
.kick{{font-family:'Archivo Narrow';font-size:.76rem;letter-spacing:.22em;text-transform:uppercase;color:var(--amber);font-weight:700}}
h1{{font-size:clamp(2.6rem,10vw,4.4rem);font-weight:900;line-height:.94;letter-spacing:-.03em;margin:12px 0}}
.sub{{font-size:1.15rem;color:var(--dim);max-width:30ch}}
section{{padding:58px 0;border-top:1px solid var(--line)}}
h2{{font-size:clamp(1.7rem,5.5vw,2.4rem);font-weight:800;letter-spacing:-.02em;line-height:1.08;margin-bottom:16px}}
p{{margin-bottom:15px;color:#cfd4cf}}
.big{{font-size:1.3rem;color:var(--white)}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);margin:26px 0}}
.grid3 div{{background:var(--ink2);padding:20px 14px;text-align:center}}
.grid3 b{{display:block;font-size:2rem;font-weight:900;color:var(--amber);line-height:1}}
.grid3 span{{font-size:.76rem;color:var(--dim);letter-spacing:.05em}}
.rev{{border-left:2px solid var(--amber);padding-left:18px;margin:26px 0}}
.rev img{{width:100%;border-radius:6px;margin-bottom:14px;display:block}}
.rev q{{font-size:1.12rem;display:block;margin-bottom:10px}}
.rev cite{{font-style:normal;font-size:.85rem;color:var(--dim)}}
.st{{color:var(--amber);letter-spacing:.15em;font-size:.8rem}}
.buy{{background:var(--ink2);border:1px solid var(--line);border-radius:12px;padding:28px 24px;margin:30px 0}}
.pr{{display:flex;align-items:baseline;gap:12px}}
.pr b{{font-size:3.4rem;font-weight:900;letter-spacing:-.03em}}
.pr s{{color:var(--dim);font-size:1.1rem}}
.pr em{{font-style:normal;background:var(--go);color:#fff;font-size:.7rem;font-weight:700;
 letter-spacing:.1em;padding:5px 10px;border-radius:3px;text-transform:uppercase}}
ul.inc{{list-style:none;margin:20px 0 0}}
ul.inc li{{padding:10px 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;font-size:.94rem}}
ul.inc li i{{font-style:normal;color:var(--amber)}}
a.cta{{display:block;text-align:center;background:var(--go);color:#fff;font-weight:800;font-size:1.1rem;
 padding:19px;border-radius:8px;text-decoration:none;margin-top:22px;letter-spacing:.01em}}
a.cta small{{display:block;font-weight:500;font-size:.78rem;opacity:.92;margin-top:3px}}
.fine{{font-size:.82rem;color:var(--dim);text-align:center;margin-top:12px}}
footer{{padding:40px 0 64px;text-align:center;font-size:.8rem;color:var(--dim);border-top:1px solid var(--line)}}
</style></head><body>
<div class="hero"><div class="w">
 <div class="kick">US pre-order · ships Sept 15</div>
 <h1>Sleep Above It.</h1>
 <p class="sub">The ground is cold, hard and wet. After {UNITS} of these shipped, we think that's a solved problem.</p>
</div></div>

<section><div class="w">
 <h2>Everything that ruins a night happens at ground level</h2>
 <p class="big">Water pools. Cold conducts. Roots find your hip. You spend the last of the daylight hunting for ground flat enough to lie on.</p>
 <p>Hang two straps instead and all four of those stop being your problem. The V.3 is a full enclosed shelter — bug net, detachable rain fly, waterproof bottom — that happens to hang.</p>
 <div class="grid3">
   <div><b>{UNITS}</b><span>UNITS SHIPPED</span></div>
   <div><b>4.8</b><span>FROM 600+ REVIEWS</span></div>
   <div><b>3–4 lb</b><span>TRAIL WEIGHT</span></div>
 </div>
</div></section>

<section><div class="w">
 <h2>Ten hours of rain, in a September storm</h2>
 <div class="rev"><img src="{r0['pic']}" alt="Customer photo — {r0['name']}" loading="lazy">
  <span class="st">{stars()}</span>
  <q>{r0['body'][:330]}</q><cite>{r0['name']} — verified buyer</cite></div>
 <div class="rev"><img src="{r1['pic']}" alt="Customer photo — {r1['name']}" loading="lazy">
  <span class="st">{stars()}</span>
  <q>{r1['body'][:300]}</q><cite>{r1['name']} — verified buyer</cite></div>
</div></section>

<section><div class="w">
 <h2>Up in under five minutes</h2>
 <div class="rev"><img src="{r2['pic']}" alt="Customer photo — {r2['name']}" loading="lazy">
  <span class="st">{stars()}</span>
  <q>{r2['body'][:300]}</q><cite>{r2['name']} — verified buyer</cite></div>
 <p>Two straps round two trunks, clip in, fly over the ridgeline, zip the net. No poles, no stakes, nothing to lose in the dark.</p>
</div></section>

<section><div class="w">
 <h2>The pre-order</h2>
 <div class="buy">
  <div class="pr"><b>$159</b><s>$429</s><em>save 63%</em></div>
  <ul class="inc">
   <li><span>Hawk Nest V.3 all-season hammock-tent</span><i>included</i></li>
   <li><span>Waterproof bottom upgrade</span><i>$39 free</i></li>
   <li><span>Waterproof carry bag</span><i>$19 free</i></li>
   <li><span>Lifetime warranty</span><i>$59 free</i></li>
   <li><span>Gridless app — 1 year</span><i>included</i></li>
   <li><span>Free US shipping &amp; returns</span><i>included</i></li>
  </ul>
  <a class="cta" href="{CHECKOUT}">Reserve mine — $159<small>Pay over time · ships Sept 15</small></a>
  <div class="fine">Ships from South Carolina · duties included · nothing owed on delivery<br>Pre-order batches ship in Navy</div>
 </div>
</div></section>
<footer><div class="w">Hawk Nest Hammocks · designed in Canada · {UNITS} shipped · 4.8 from 600+ verified reviews</div></footer>
</body></html>"""
pathlib.Path("us-dark.html").write_text(P1)
print("wrote us-dark.html", len(P1))

# ═════════════════════ 2. PROOF WALL — light, UGC-led ═════════════════════
wall = "".join(
  f'<figure><img src="{r["pic"]}" alt="Customer photo — {r["name"]}" loading="lazy">'
  f'<figcaption><b>{r["name"]}</b> {stars()}<br>{r["body"][:150]}…</figcaption></figure>'
  for r in R[:8])
P2 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{UNITS} People Stopped Sleeping on the Ground | Hawk Nest V.3</title>
<meta name="description" content="Real photos from real buyers. The V.3 all-season hammock-tent, $159 US pre-order, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#ffffff;--soft:#f4f6f3;--ink:#121a14;--body:#4a544c;--green:#2f6b3f;--green2:#245631;--line:#dfe5df}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--body);font-family:'Inter',system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}}
.w{{max-width:760px;margin:0 auto;padding:0 18px}}
header{{padding:46px 0 26px;text-align:center}}
.pill{{display:inline-block;background:var(--soft);border:1px solid var(--line);border-radius:99px;
 padding:7px 15px;font-size:.78rem;font-weight:600;color:var(--green);margin-bottom:16px}}
h1{{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(2rem,7vw,3.2rem);font-weight:800;
 color:var(--ink);line-height:1.03;letter-spacing:-.03em;text-wrap:balance}}
header p{{font-size:1.12rem;margin-top:12px;max-width:36ch;margin-inline:auto}}
.wall{{columns:2;column-gap:10px;padding:8px 0 30px}}
@media(min-width:620px){{.wall{{columns:3}}}}
.wall figure{{break-inside:avoid;margin:0 0 10px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}}
.wall img{{width:100%;display:block}}
.wall figcaption{{padding:10px 11px;font-size:.76rem;line-height:1.45;color:var(--body)}}
.wall figcaption b{{color:var(--ink)}}
section{{padding:46px 0;border-top:1px solid var(--line)}}
h2{{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(1.5rem,5vw,2.1rem);font-weight:700;
 color:var(--ink);letter-spacing:-.02em;margin-bottom:14px;text-wrap:balance}}
p{{margin-bottom:14px}}
.rowstat{{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}}
.rowstat div{{flex:1;min-width:110px;background:var(--soft);border-radius:10px;padding:16px;text-align:center}}
.rowstat b{{display:block;font-family:'Bricolage Grotesque';font-size:1.7rem;color:var(--green);line-height:1}}
.rowstat span{{font-size:.74rem}}
.buy{{background:var(--soft);border:1px solid var(--line);border-radius:16px;padding:26px 22px}}
.pr{{display:flex;align-items:baseline;gap:11px;margin-bottom:4px}}
.pr b{{font-family:'Bricolage Grotesque';font-size:3rem;font-weight:800;color:var(--ink);letter-spacing:-.03em}}
.pr s{{color:#8b968c}}.pr em{{font-style:normal;background:var(--green);color:#fff;font-size:.68rem;
 font-weight:700;padding:5px 9px;border-radius:5px;letter-spacing:.06em}}
ul.inc{{list-style:none;margin:16px 0 0}}
ul.inc li{{padding:9px 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;font-size:.92rem}}
ul.inc li i{{font-style:normal;color:var(--green);font-weight:600}}
a.cta{{display:block;text-align:center;background:var(--green);color:#fff;font-weight:700;font-size:1.08rem;
 padding:18px;border-radius:10px;text-decoration:none;margin-top:20px}}
a.cta small{{display:block;font-weight:400;font-size:.78rem;opacity:.92;margin-top:3px}}
.fine{{font-size:.8rem;text-align:center;margin-top:11px;color:#7d887e}}
footer{{padding:34px 0 60px;text-align:center;font-size:.78rem;color:#8b968c;border-top:1px solid var(--line)}}
</style></head><body>
<header><div class="w">
 <div class="pill">US pre-order · ships Sept 15</div>
 <h1>{UNITS} people stopped sleeping on the ground.</h1>
 <p>These aren't stock photos. Every picture below came from a verified buyer's review.</p>
</div></header>
<div class="w"><div class="wall">{wall}</div></div>

<section><div class="w">
 <h2>What they all say, roughly</h2>
 <p>Three things come up again and again: it goes up faster than a tent, it stays dry when it
 shouldn't, and people sleep better in it than they do at home. That last one sounds like
 marketing until you read forty reviews saying it unprompted.</p>
 <div class="rowstat">
  <div><b>{UNITS}</b><span>units shipped</span></div>
  <div><b>4.8/5</b><span>600+ reviews</span></div>
  <div><b>Lifetime</b><span>warranty</span></div>
 </div>
</div></section>

<section><div class="w">
 <h2>The pre-order price</h2>
 <p>You're buying from the September batch before it lands. No warehousing, no inventory float,
 no retailer margin — that's the whole discount. You wait until Sept 15, and it costs $159.</p>
 <div class="buy">
  <div class="pr"><b>$159</b><s>$429</s><em>SAVE 63%</em></div>
  <ul class="inc">
   <li><span>Hawk Nest V.3 all-season hammock-tent</span><i>included</i></li>
   <li><span>Waterproof bottom upgrade</span><i>$39 free</i></li>
   <li><span>Waterproof carry bag</span><i>$19 free</i></li>
   <li><span>Lifetime warranty</span><i>$59 free</i></li>
   <li><span>Gridless app — 1 year</span><i>included</i></li>
   <li><span>Free US shipping &amp; returns</span><i>included</i></li>
  </ul>
  <a class="cta" href="{CHECKOUT}">Reserve mine — $159<small>Pay over time · ships Sept 15</small></a>
  <div class="fine">Ships from South Carolina · duties included · pre-order batches ship in Navy</div>
 </div>
</div></section>
<footer><div class="w">Hawk Nest Hammocks · designed in Canada · every photo above is a real customer review</div></footer>
</body></html>"""
pathlib.Path("us-proof.html").write_text(P2)
print("wrote us-proof.html", len(P2))

# ═════════════════════ 3. FIELD SPEC — technical datasheet ═════════════════════
r3 = rv(6)
P3 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>V.3 Field Specification | Hawk Nest — US Pre-Order</title>
<meta name="description" content="Full specification for the Hawk Nest V.3 all-season hammock-tent. $159 US pre-order, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#eef1f4;--card:#fff;--navy:#12263f;--steel:#3d5a7a;--body:#41505f;--rule:#c9d4de;--orange:#c8541f}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--paper);color:var(--body);font-family:'IBM Plex Sans',system-ui,sans-serif;line-height:1.55;
 background-image:linear-gradient(var(--rule) .5px,transparent .5px),linear-gradient(90deg,var(--rule) .5px,transparent .5px);
 background-size:26px 26px;background-position:-1px -1px}}
.w{{max-width:740px;margin:0 auto;padding:0 18px}}
.sheet{{background:var(--card);border:1px solid var(--rule);margin:22px auto;max-width:776px;
 box-shadow:0 1px 3px rgba(18,38,63,.07)}}
.hd{{background:var(--navy);color:#fff;padding:22px 24px;display:flex;justify-content:space-between;
 align-items:flex-start;gap:16px;flex-wrap:wrap}}
.hd .t{{font-family:'IBM Plex Mono';font-size:.68rem;letter-spacing:.18em;opacity:.75}}
.hd h1{{font-size:clamp(1.5rem,5vw,2.1rem);font-weight:700;letter-spacing:-.02em;line-height:1.1;margin-top:4px}}
.hd .rev{{font-family:'IBM Plex Mono';font-size:.7rem;text-align:right;opacity:.8;white-space:nowrap}}
.bd{{padding:24px}}
h2{{font-family:'IBM Plex Mono';font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);
 border-bottom:1px solid var(--rule);padding-bottom:7px;margin:28px 0 14px;font-weight:600}}
h2:first-child{{margin-top:0}}
p{{margin-bottom:13px;font-size:.96rem}}
table{{width:100%;border-collapse:collapse;font-size:.9rem;margin-bottom:8px}}
td{{padding:8px 4px;border-bottom:1px solid var(--rule)}}
td:first-child{{color:var(--steel);width:46%}}
td:last-child{{text-align:right;font-family:'IBM Plex Mono';color:var(--navy);font-weight:500}}
.cmp td:last-child{{text-align:right}}
.cmp .win{{color:var(--orange);font-weight:600}}
.callout{{background:#f6f9fc;border-left:3px solid var(--steel);padding:14px 16px;margin:16px 0;font-size:.92rem}}
figure{{margin:16px 0}}
figure img{{width:100%;border:1px solid var(--rule);display:block}}
figcaption{{font-family:'IBM Plex Mono';font-size:.7rem;color:var(--steel);padding-top:6px}}
.price{{background:var(--navy);color:#fff;padding:22px 24px;margin-top:26px}}
.price .row{{display:flex;align-items:baseline;gap:11px}}
.price b{{font-size:2.9rem;font-weight:700;letter-spacing:-.02em}}
.price s{{opacity:.6}}
.price em{{font-style:normal;background:var(--orange);font-size:.66rem;font-weight:600;letter-spacing:.09em;
 padding:4px 9px;text-transform:uppercase}}
.price table{{margin-top:14px}}
.price td{{border-bottom:1px solid rgba(255,255,255,.14);color:#c6d4e2}}
.price td:last-child{{color:#8fd0a0}}
a.cta{{display:block;text-align:center;background:var(--orange);color:#fff;font-weight:600;font-size:1.06rem;
 padding:17px;text-decoration:none;margin-top:18px;font-family:'IBM Plex Sans'}}
a.cta small{{display:block;font-weight:400;font-size:.76rem;opacity:.9;margin-top:3px}}
.fine{{font-family:'IBM Plex Mono';font-size:.68rem;color:#9db2c4;text-align:center;margin-top:11px;line-height:1.6}}
footer{{padding:18px 24px 30px;font-family:'IBM Plex Mono';font-size:.66rem;color:var(--steel);
 border-top:1px solid var(--rule)}}
</style></head><body>
<div class="sheet">
 <div class="hd">
  <div><div class="t">HAWK NEST HAMMOCKS · FIELD SPECIFICATION</div>
   <h1>V.3 All-Season Hammock-Tent</h1></div>
  <div class="rev">DOC V.3-US<br>PRE-ORDER<br>SHIPS 15 SEP 2026</div>
 </div>
 <div class="bd">

  <h2>1 · Summary</h2>
  <p>A fully enclosed suspended shelter: hammock body, integrated bug net, detachable rain fly
  and a waterproof floor panel. Replaces tent, footprint and — for most of the year — the
  insulated sleeping pad, because there is no ground contact to conduct heat away.</p>

  <h2>2 · Specification</h2>
  <table>
   <tr><td>Trail weight</td><td>3–4 lb</td></tr>
   <tr><td>Packed size</td><td>5.5 × 5.5 × 16 in</td></tr>
   <tr><td>Max load</td><td>500 lb</td></tr>
   <tr><td>Pad pocket</td><td>fits pads to 25 in wide</td></tr>
   <tr><td>Bug net</td><td>integrated, single-side zip</td></tr>
   <tr><td>Rain fly</td><td>detachable</td></tr>
   <tr><td>Anchor span</td><td>10–15 ft between trees</td></tr>
   <tr><td>Setup time</td><td>&lt; 5 min</td></tr>
   <tr><td>Colour (pre-order batch)</td><td>Navy</td></tr>
  </table>

  <h2>3 · Comparison — ground system</h2>
  <table class="cmp">
   <tr><td>2P tent + pad + footprint + hardware</td><td>$450 · 6 lb 8 oz</td></tr>
   <tr><td>Hawk Nest V.3 complete kit</td><td class="win">$159 · 3–4 lb</td></tr>
   <tr><td>Difference</td><td class="win">−$291 · −2.5 lb</td></tr>
  </table>
  <div class="callout"><b>Note on the pad.</b> A ground system needs an insulated pad because
  the earth conducts heat out of you all night. Suspended, there is nothing beneath you to
  conduct to. The pad becomes optional outside deep winter.</div>

  <h2>4 · Field results</h2>
  <figure><img src="{r3['pic']}" alt="Customer field photo — {r3['name']}" loading="lazy">
   <figcaption>Verified buyer photo · {r3['name']}</figcaption></figure>
  <p style="font-size:.94rem">“{r3['body'][:260]}”</p>
  <table>
   <tr><td>Units shipped</td><td>{UNITS}</td></tr>
   <tr><td>Verified reviews</td><td>600+</td></tr>
   <tr><td>Mean rating</td><td>4.8 / 5</td></tr>
   <tr><td>Warranty</td><td>lifetime, hammock body</td></tr>
  </table>

  <h2>5 · Not suitable for</h2>
  <p>Above the treeline, open desert, beach sand — anywhere without two anchor points 10–15 ft
  apart. In those conditions use a tent. Stated plainly because a returned order helps nobody.</p>

  <div class="price">
   <div class="t" style="font-family:'IBM Plex Mono';font-size:.66rem;letter-spacing:.16em;opacity:.7">6 · PRE-ORDER TERMS</div>
   <div class="row" style="margin-top:8px"><b>$159</b><s>$429</s><em>save 63%</em></div>
   <table>
    <tr><td>V.3 hammock-tent</td><td>included</td></tr>
    <tr><td>Waterproof bottom</td><td>$39 → free</td></tr>
    <tr><td>Waterproof carry bag</td><td>$19 → free</td></tr>
    <tr><td>Lifetime warranty</td><td>$59 → free</td></tr>
    <tr><td>Gridless app, 1 yr</td><td>included</td></tr>
    <tr><td>US shipping &amp; returns</td><td>free</td></tr>
   </table>
   <a class="cta" href="{CHECKOUT}">Reserve unit — $159<small>Pay over time available · ships 15 Sep</small></a>
   <div class="fine">SHIPPED FROM SOUTH CAROLINA · DUTIES INCLUDED · NOTHING OWED ON DELIVERY</div>
  </div>
 </div>
 <footer>HAWK NEST HAMMOCKS · DESIGNED IN CANADA · {UNITS} UNITS SHIPPED · 4.8/5 FROM 600+ VERIFIED REVIEWS</footer>
</div>
</body></html>"""
pathlib.Path("us-spec.html").write_text(P3)
print("wrote us-spec.html", len(P3))
