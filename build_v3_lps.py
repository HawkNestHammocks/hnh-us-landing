import sys; sys.path.insert(0,'.')
import lp_parts as L, lp_shared as S, pathlib, json

R = json.load(open("/tmp/jm_us.json"))
def rv(i): return R[i % len(R)]

def offer(cls=""):
    rows = "".join(f'<li><span>{n}</span><i>{v}</i></li>' for n,v in L.INCLUDES)
    return f"""<div class="buy rv">
 <div class="pr"><b>$159</b><s>$429</s><em>SAVE 63%</em></div>
 <ul class="inc">{rows}</ul>
 <a class="cta" href="{L.CHECKOUT}">Reserve mine — $159<small>Pay over time · ships Sept 15</small></a>
 <div class="fine">Ships from South Carolina · duties included · nothing owed on delivery<br>
 Pre-order batches ship in Navy</div></div>"""

# ══════════ 1 · DARK EDITORIAL ══════════
r0,r1,r2 = rv(8), rv(1), rv(0)
DARK = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sleep Above It | Hawk Nest V.3 — US Pre-Order</title>
<meta name="description" content="All-season hammock-tent that also pitches on the ground. $159 US pre-order, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=Archivo+Narrow:wght@600;700&display=swap" rel="stylesheet">
<style>
:root{{--ink:#0b0d0c;--card:#141816;--line:#2a302c;--white:#f4f2ec;--dim:#9aa39c;--accent:#e8933a;
 --go:#d97a1c;--h:#f4f2ec;--b:#cfd4cf;--fh:'Archivo';--hw:800;--hls:-.02em;--r:10px}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--ink);color:var(--white);font-family:'Archivo',system-ui,sans-serif;
 line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:720px;margin:0 auto;padding:0 20px}}
.hero{{min-height:70vh;display:flex;flex-direction:column;justify-content:flex-end;
 background:linear-gradient(180deg,rgba(11,13,12,.30),rgba(11,13,12,.92) 74%,var(--ink)),
 url('{L.IMG["trees"]}') center/cover;padding:64px 0 40px}}
.kick{{font-family:'Archivo Narrow';font-size:.76rem;letter-spacing:.22em;text-transform:uppercase;
 color:var(--accent);font-weight:700}}
h1{{font-size:clamp(2.5rem,9.5vw,4.2rem);font-weight:900;line-height:.95;letter-spacing:-.03em;margin:12px 0}}
.sub{{font-size:1.12rem;color:var(--dim);max-width:32ch}}
section{{border-top:1px solid var(--line)}}
p{{margin-bottom:15px;color:var(--b)}}
.big{{font-size:1.26rem;color:var(--white)}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);margin:24px 0}}
.grid3 div{{background:var(--card);padding:18px 12px;text-align:center}}
.grid3 b{{display:block;font-size:1.8rem;font-weight:900;color:var(--accent);line-height:1}}
.grid3 span{{font-size:.72rem;color:var(--dim)}}
.rev{{border-left:2px solid var(--accent);padding-left:18px;margin:24px 0}}
.rev img{{width:100%;border-radius:8px;margin-bottom:13px;display:block}}
.rev q{{font-size:1.08rem;display:block;margin-bottom:9px}}
.rev cite{{font-style:normal;font-size:.84rem;color:var(--dim)}}
.st{{color:var(--accent);letter-spacing:.15em;font-size:.78rem}}
.buy{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 22px;margin:26px 0}}
.pr{{display:flex;align-items:baseline;gap:11px}}
.pr b{{font-size:3.2rem;font-weight:900;letter-spacing:-.03em}}
.pr s{{color:var(--dim);font-size:1.05rem}}
.pr em{{font-style:normal;background:var(--go);color:#fff;font-size:.68rem;font-weight:700;
 letter-spacing:.1em;padding:5px 10px;border-radius:3px}}
ul.inc{{list-style:none;margin:18px 0 0}}
ul.inc li{{padding:10px 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;
 gap:12px;font-size:.92rem}}
ul.inc li i{{font-style:normal;color:var(--accent);white-space:nowrap}}
a.cta{{display:block;text-align:center;background:var(--go);color:#fff;font-weight:800;font-size:1.08rem;
 padding:18px;border-radius:8px;text-decoration:none;margin-top:20px;
 transition:transform .2s,box-shadow .2s}}
a.cta:active{{transform:scale(.985)}}
a.cta small{{display:block;font-weight:500;font-size:.76rem;opacity:.92;margin-top:3px}}
.fine{{font-size:.8rem;color:var(--dim);text-align:center;margin-top:11px;line-height:1.55}}
footer{{padding:36px 0 60px;text-align:center;font-size:.78rem;color:var(--dim);border-top:1px solid var(--line)}}
{S.CORE_CSS}
</style></head><body>
<div class="hero"><div class="w">
 <div class="kick">US pre-order · ships Sept 15</div>
 <h1>Sleep Above It.<br>Or On It.</h1>
 <p class="sub">An all-season shelter that hangs between two trees — and pitches on the ground when there aren't any.</p>
</div></div>

<section class="lp-sec"><div class="w">
 {S.logos()}
 {S.urgency()}
 <h2 class="lp-h rv">Everything that ruins a night happens at ground level</h2>
 <p class="big rv">Water pools. Cold conducts. Roots find your hip. You lose the last of the daylight hunting for ground flat enough to lie on.</p>
 <p class="rv">Hang two straps and all four stop being your problem. And when there's nothing to hang from, the same shelter goes up on the ground as a tent — so you're never carrying the wrong kit.</p>
 <div class="grid3 rv">
  <div><b>{L.UNITS}</b><span>UNITS SHIPPED</span></div>
  <div><b>{L.RATING}</b><span>{L.REVIEWS} REVIEWS</span></div>
  <div><b>3–4 lb</b><span>TRAIL WEIGHT</span></div>
 </div>
 {S.band("ground","No trees? It pitches on the ground as a tent — same fly, same bug net.")}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">Look at the thing properly</h2>
 <p class="rv">Swipe through — build detail, the pad pocket, packed size, and the ground setup.</p>
 {S.carousel()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">Ten hours of rain, in a September storm</h2>
 <div class="rev rv"><img src="{r0['pic']}" alt="Customer photo — {r0['name']}" loading="lazy">
  <span class="st">★★★★★</span><q>{r0['body'][:320]}</q><cite>{r0['name']} — verified buyer</cite></div>
 <div class="rev rv"><img src="{r1['pic']}" alt="Customer photo — {r1['name']}" loading="lazy">
  <span class="st">★★★★★</span><q>{r1['body'][:290]}</q><cite>{r1['name']} — verified buyer</cite></div>
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">Up in under five minutes</h2>
 <div class="rev rv"><img src="{r2['pic']}" alt="Customer photo — {r2['name']}" loading="lazy">
  <span class="st">★★★★★</span><q>{r2['body'][:290]}</q><cite>{r2['name']} — verified buyer</cite></div>
 {S.band("packed","Packs to 5.5 x 5.5 x 16in — smaller than the tent it replaces.")}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">What happens after you order</h2>
 {S.timeline()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">The pre-order</h2>
 {offer()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">Questions people actually ask</h2>
 {S.faq()}
</div></section>

<footer><div class="w">Hawk Nest Hammocks · designed in Canada · {L.UNITS} shipped · {L.RATING} from {L.REVIEWS} verified reviews</div></footer>
{S.CORE_JS}
</body></html>"""
pathlib.Path("us-dark.html").write_text(DARK)
print("us-dark.html", len(DARK))

# ══════════ 2 · PROOF WALL ══════════
wall = "".join(
  f'<figure><img src="{r["pic"]}" alt="Customer photo — {r["name"]}" loading="lazy">'
  f'<figcaption><b>{r["name"]}</b> ★★★★★<br>{r["body"][:140]}…</figcaption></figure>'
  for r in R[:8])
PROOF = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{L.UNITS} People Stopped Sleeping on the Ground | Hawk Nest V.3</title>
<meta name="description" content="Real photos from real buyers. All-season hammock-tent that also pitches on the ground. $159, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fff;--card:#f4f6f3;--h:#121a14;--b:#4a544c;--accent:#2f6b3f;--green2:#245631;
 --line:#dfe5df;--fh:'Bricolage Grotesque';--hw:700;--hls:-.02em;--r:12px}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--b);font-family:'Inter',system-ui,sans-serif;line-height:1.6;
 -webkit-font-smoothing:antialiased}}
.w{{max-width:760px;margin:0 auto;padding:0 18px}}
header{{padding:34px 0 22px;text-align:center}}
.pill{{display:inline-block;background:var(--card);border:1px solid var(--line);border-radius:99px;
 padding:7px 15px;font-size:.78rem;font-weight:600;color:var(--accent);margin-bottom:14px}}
h1{{font-family:var(--fh);font-size:clamp(1.95rem,6.6vw,3.05rem);font-weight:800;color:var(--h);
 line-height:1.04;letter-spacing:-.03em;text-wrap:balance}}
header p{{font-size:1.1rem;margin-top:11px;max-width:38ch;margin-inline:auto}}
.wall{{columns:2;column-gap:10px;padding:6px 0 24px}}
@media(min-width:620px){{.wall{{columns:3}}}}
.wall figure{{break-inside:avoid;margin:0 0 10px;border:1px solid var(--line);border-radius:10px;
 overflow:hidden;background:#fff}}
.wall img{{width:100%;display:block}}
.wall figcaption{{padding:10px 11px;font-size:.75rem;line-height:1.45}}
.wall figcaption b{{color:var(--h)}}
section{{border-top:1px solid var(--line)}}
p{{margin-bottom:14px}}
.rowstat{{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}}
.rowstat div{{flex:1;min-width:106px;background:var(--card);border-radius:10px;padding:15px;text-align:center}}
.rowstat b{{display:block;font-family:var(--fh);font-size:1.6rem;color:var(--accent);line-height:1}}
.rowstat span{{font-size:.73rem}}
.buy{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 20px}}
.pr{{display:flex;align-items:baseline;gap:11px;margin-bottom:3px}}
.pr b{{font-family:var(--fh);font-size:2.9rem;font-weight:800;color:var(--h);letter-spacing:-.03em}}
.pr s{{color:#8b968c}}
.pr em{{font-style:normal;background:var(--accent);color:#fff;font-size:.66rem;font-weight:700;
 padding:5px 9px;border-radius:5px}}
ul.inc{{list-style:none;margin:15px 0 0}}
ul.inc li{{padding:9px 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;
 gap:12px;font-size:.9rem}}
ul.inc li i{{font-style:normal;color:var(--accent);font-weight:600;white-space:nowrap}}
a.cta{{display:block;text-align:center;background:var(--accent);color:#fff;font-weight:700;
 font-size:1.06rem;padding:17px;border-radius:10px;text-decoration:none;margin-top:18px;
 transition:transform .2s}}
a.cta:active{{transform:scale(.985)}}
a.cta small{{display:block;font-weight:400;font-size:.76rem;opacity:.92;margin-top:3px}}
.fine{{font-size:.78rem;text-align:center;margin-top:10px;color:#7d887e;line-height:1.5}}
footer{{padding:30px 0 56px;text-align:center;font-size:.77rem;color:#8b968c;border-top:1px solid var(--line)}}
{S.CORE_CSS}
</style></head><body>
<header><div class="w">
 {S.logos()}
 <div class="pill">US pre-order · ships Sept 15</div>
 <h1>{L.UNITS} people stopped sleeping on the ground.</h1>
 <p>These aren't stock photos. Every picture below came from a verified buyer's review.</p>
</div></header>
<div class="w"><div class="wall">{wall}</div>{S.urgency()}</div>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">What they all say, roughly</h2>
 <p class="rv">Three things come up again and again: it goes up faster than a tent, it stays dry when
 it shouldn't, and people sleep better in it than they do at home. That last one sounds like
 marketing until you've read forty reviews saying it unprompted.</p>
 <div class="rowstat rv">
  <div><b>{L.UNITS}</b><span>units shipped</span></div>
  <div><b>{L.RATING}/5</b><span>{L.REVIEWS} reviews</span></div>
  <div><b>Lifetime</b><span>warranty</span></div>
 </div>
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">No trees? It becomes a ground tent</h2>
 <p class="rv">This is the part most people don't realise. The V.3 isn't only a hammock — pitch it on
 the ground with poles and it's a full tent, same fly, same bug net, same waterproof floor. Above the
 treeline, on sand, in a bare campsite, you're still covered.</p>
 {S.band("ground","The same shelter, set up on the ground.")}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">The product, close up</h2>
 {S.carousel()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">What happens after you order</h2>
 {S.timeline()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">The pre-order price</h2>
 <p class="rv">You're buying from the September batch before it lands. No warehousing, no inventory
 float, no retailer margin — that's the whole discount.</p>
 {offer()}
</div></section>

<section class="lp-sec"><div class="w">
 <h2 class="lp-h rv">Questions people actually ask</h2>
 {S.faq()}
</div></section>

<footer><div class="w">Hawk Nest Hammocks · designed in Canada · every photo above is a real customer review</div></footer>
{S.CORE_JS}
</body></html>"""
pathlib.Path("us-proof.html").write_text(PROOF)
print("us-proof.html", len(PROOF))

# ══════════ 3 · FIELD SPEC ══════════
r3 = rv(6)
SPEC = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>V.3 Field Specification | Hawk Nest — US Pre-Order</title>
<meta name="description" content="Full spec for the Hawk Nest V.3. Hangs between trees or pitches on the ground. $159 US pre-order, ships Sept 15.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#eef1f4;--card:#fff;--navy:#12263f;--steel:#3d5a7a;--b:#41505f;--line:#c9d4de;
 --accent:#c8541f;--h:#12263f;--fh:'IBM Plex Sans';--hw:700;--hls:-.01em;--r:6px}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--paper);color:var(--b);font-family:'IBM Plex Sans',system-ui,sans-serif;
 line-height:1.55;background-image:linear-gradient(var(--line) .5px,transparent .5px),
 linear-gradient(90deg,var(--line) .5px,transparent .5px);background-size:26px 26px}}
.w{{max-width:740px;margin:0 auto;padding:0 18px}}
.sheet{{background:var(--card);border:1px solid var(--line);margin:20px auto;max-width:778px;
 box-shadow:0 1px 3px rgba(18,38,63,.07)}}
.hd{{background:var(--navy);color:#fff;padding:20px 22px;display:flex;justify-content:space-between;
 align-items:center;gap:14px;flex-wrap:wrap}}
.hd img{{height:34px}}
.hd .t{{font-family:'IBM Plex Mono';font-size:.66rem;letter-spacing:.18em;opacity:.75}}
.hd h1{{font-size:clamp(1.4rem,4.8vw,2rem);font-weight:700;letter-spacing:-.02em;line-height:1.1;margin-top:3px}}
.hd .rev{{font-family:'IBM Plex Mono';font-size:.68rem;text-align:right;opacity:.8;white-space:nowrap}}
.bd{{padding:22px}}
h2.sec{{font-family:'IBM Plex Mono';font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;
 color:var(--accent);border-bottom:1px solid var(--line);padding-bottom:6px;margin:26px 0 12px;font-weight:600}}
h2.sec:first-child{{margin-top:0}}
p{{margin-bottom:12px;font-size:.95rem}}
table{{width:100%;border-collapse:collapse;font-size:.89rem;margin-bottom:8px}}
td{{padding:8px 4px;border-bottom:1px solid var(--line)}}
td:first-child{{color:var(--steel);width:46%}}
td:last-child{{text-align:right;font-family:'IBM Plex Mono';color:var(--navy);font-weight:500}}
.cmp .win{{color:var(--accent);font-weight:600}}
.callout{{background:#f6f9fc;border-left:3px solid var(--steel);padding:13px 15px;margin:14px 0;font-size:.91rem}}
.price{{background:var(--navy);color:#fff;padding:20px 22px;margin-top:24px}}
.price .row{{display:flex;align-items:baseline;gap:11px}}
.price b{{font-size:2.7rem;font-weight:700;letter-spacing:-.02em}}
.price s{{opacity:.6}}
.price em{{font-style:normal;background:var(--accent);font-size:.64rem;font-weight:600;
 letter-spacing:.09em;padding:4px 9px;text-transform:uppercase}}
.price ul{{list-style:none;margin-top:12px}}
.price li{{display:flex;justify-content:space-between;gap:12px;padding:7px 0;
 border-bottom:1px solid rgba(255,255,255,.14);color:#c6d4e2;font-size:.87rem}}
.price li i{{font-style:normal;color:#8fd0a0;white-space:nowrap}}
a.cta{{display:block;text-align:center;background:var(--accent);color:#fff;font-weight:600;
 font-size:1.04rem;padding:16px;text-decoration:none;margin-top:16px;transition:transform .2s}}
a.cta:active{{transform:scale(.985)}}
a.cta small{{display:block;font-weight:400;font-size:.74rem;opacity:.9;margin-top:3px}}
.fine{{font-family:'IBM Plex Mono';font-size:.66rem;color:#9db2c4;text-align:center;margin-top:10px;line-height:1.6}}
footer{{padding:16px 22px 28px;font-family:'IBM Plex Mono';font-size:.64rem;color:var(--steel);
 border-top:1px solid var(--line)}}
{S.CORE_CSS}
.car-item,.band{{border-color:var(--line)}}
</style></head><body>
<div class="sheet">
 <div class="hd">
  <div><div class="t">HAWK NEST HAMMOCKS · FIELD SPECIFICATION</div>
   <h1>V.3 All-Season Hammock-Tent</h1></div>
  <img src="{L.LOGO_ALT}" alt="Hawk Nest Hammocks">
  <div class="rev">DOC V.3-US<br>PRE-ORDER<br>SHIPS 15 SEP 2026</div>
 </div>
 <div class="bd">
  <h2 class="sec">1 · Summary</h2>
  <p>A fully enclosed suspended shelter: hammock body, integrated bug net, detachable rain fly and a
  waterproof floor panel. <b>Also pitches on the ground as a conventional tent</b>, so it covers sites
  with no anchor points. Replaces tent, footprint and — for most of the year — the insulated pad,
  because suspended there is no ground contact to conduct heat away.</p>

  <h2 class="sec">2 · Two configurations</h2>
  {S.band("ground","Ground configuration — same fly, same bug net, no trees required.")}
  <table>
   <tr><td>Suspended</td><td>2 anchor points, 10–15 ft apart</td></tr>
   <tr><td>Ground</td><td>pole-pitched, freestanding</td></tr>
   <tr><td>Changeover</td><td>same shelter, no extra parts</td></tr>
  </table>

  <h2 class="sec">3 · Specification</h2>
  <table>
   <tr><td>Trail weight</td><td>3–4 lb</td></tr>
   <tr><td>Packed size</td><td>5.5 × 5.5 × 16 in</td></tr>
   <tr><td>Max load</td><td>500 lb</td></tr>
   <tr><td>Pad pocket</td><td>fits pads to 25 in wide</td></tr>
   <tr><td>Bug net</td><td>integrated, single-side zip</td></tr>
   <tr><td>Rain fly</td><td>detachable</td></tr>
   <tr><td>Setup time</td><td>&lt; 5 min</td></tr>
   <tr><td>Colour (pre-order batch)</td><td>Navy</td></tr>
  </table>

  <h2 class="sec">4 · Gallery</h2>
  {S.carousel()}

  <h2 class="sec">5 · Comparison — ground system</h2>
  <table class="cmp">
   <tr><td>2P tent + pad + footprint + hardware</td><td>$450 · 6 lb 8 oz</td></tr>
   <tr><td>Hawk Nest V.3 complete kit</td><td class="win">$159 · 3–4 lb</td></tr>
   <tr><td>Difference</td><td class="win">−$291 · −2.5 lb</td></tr>
  </table>
  <div class="callout"><b>Note on the pad.</b> A ground system needs an insulated pad because the
  earth conducts heat out of you all night. Suspended, there is nothing beneath you to conduct to.</div>

  <h2 class="sec">6 · Field results</h2>
  <figure class="band rv"><img src="{r3['pic']}" alt="Customer field photo — {r3['name']}" loading="lazy">
   <figcaption>Verified buyer photo · {r3['name']}</figcaption></figure>
  <p style="font-size:.93rem">“{r3['body'][:250]}”</p>
  <table>
   <tr><td>Units shipped</td><td>{L.UNITS}</td></tr>
   <tr><td>Verified reviews</td><td>{L.REVIEWS}</td></tr>
   <tr><td>Mean rating</td><td>{L.RATING} / 5</td></tr>
   <tr><td>Warranty</td><td>lifetime, hammock body</td></tr>
  </table>

  <h2 class="sec">7 · Delivery schedule</h2>
  {S.timeline()}

  <div class="price">
   <div class="t" style="font-family:'IBM Plex Mono';font-size:.64rem;letter-spacing:.16em;opacity:.7">8 · PRE-ORDER TERMS</div>
   <div class="row" style="margin-top:7px"><b>$159</b><s>$429</s><em>save 63%</em></div>
   <ul>{"".join(f'<li><span>{n}</span><i>{v}</i></li>' for n,v in L.INCLUDES)}</ul>
   <a class="cta" href="{L.CHECKOUT}">Reserve unit — $159<small>Pay over time · ships 15 Sep</small></a>
   <div class="fine">SHIPPED FROM SOUTH CAROLINA · DUTIES INCLUDED · NOTHING OWED ON DELIVERY</div>
  </div>

  <h2 class="sec">9 · Frequently asked</h2>
  {S.faq()}
 </div>
 <footer>HAWK NEST HAMMOCKS · DESIGNED IN CANADA · {L.UNITS} UNITS SHIPPED · {L.RATING}/5 FROM {L.REVIEWS} VERIFIED REVIEWS</footer>
</div>
{S.CORE_JS}
</body></html>"""
pathlib.Path("us-spec.html").write_text(SPEC)
print("us-spec.html", len(SPEC))
