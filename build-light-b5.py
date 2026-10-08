#!/usr/bin/env python3
"""Light V.2 — rebuild light-test.html for Batch 5 at the Max Value price point.

Light is the only funnel that went 3-for-3 into the sub-$70 bucket, and it did it
at $179. It was never updated past its August launch copy, so this script ports it
forward: Max Value 6-item bundle, Batch 5 framing, the real batch-5 fill tracker
from christmas.html, and no fabricated viewer counts.

Price is a parameter, so a future price move is one number here and a rebuild.

    light-b5.html      $179   (the price Light actually earned its wins at)
"""
import re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "light-test.html")

# Max Value bundle — must stay identical to christmas.html or the two pages
# aren't a clean funnel test.
CART = ("https://hawknesthammocks.ca/cart/53200326557993:1,53198306312489:1,"
        "53198306345257:1,46948621254953:1,46948623810857:1,47874384953641:1?country=US")
VALUE   = 429
REVIEWS = 554

def build(price, outname):
    h = open(SRC).read()
    save = VALUE - price

    # ── every checkout link points at the Max Value bundle ───────────────────
    h = h.replace("https://hawknesthammocks.ca/products/"
                  "hawk-nest-all-season-hammock-tent-v-3-us-pre-order?country=US", CART)

    # ── head ─────────────────────────────────────────────────────────────────
    h = h.replace("<title>Hawk Nest™ All-Season Hammock Tent — Now Available in the USA</title>",
                  f"<title>Batch 5 — The Last Run of 2026 | Hawk Nest All-Season Hammock Tent "
                  f"(${price}, ${VALUE} Value)</title>")
    h = re.sub(r'<meta name="description" content="[^"]*"',
               f'<meta name="description" content="Batches 1-4 sold out. Batch 5 is the final '
               f'production run of 2026 and ships by December 1. The ${VALUE} setup for ${price}, '
               f'with every upgrade included free. {REVIEWS} five-star reviews."', h)

    # ── hero ─────────────────────────────────────────────────────────────────
    h = h.replace('<div class="hero-flag"><span>🇺🇸</span> NOW AVAILABLE IN THE USA</div>',
                  '<div class="hero-flag"><span>🇺🇸</span> BATCH 5 · THE LAST RUN OF 2026</div>')
    h = h.replace('<span class="hp-old">$336 value</span>', f'<span class="hp-old">${VALUE} value</span>')
    h = h.replace('<span class="hp-save">Save $157</span>', f'<span class="hp-save">Save ${save}</span>')
    h = h.replace('<div class="hp-free">+ 4 FREE UPGRADES INCLUDED</div>',
                  '<div class="hp-free">+ 6 FREE UPGRADES INCLUDED</div>')
    h = h.replace("400+ five-star reviews. Now shipping to all 50 states.",
                  f"{REVIEWS} five-star reviews. Batches 1-4 sold out. Batch 5 ships by December 1.")

    # ── value stack → the Max Value six ──────────────────────────────────────
    h = h.replace("We're loading up this first US batch with bonuses that won't be available at full price.",
                  "The hammock tent, plus every upgrade people normally add to it, "
                  "included at no extra cost while Batch&nbsp;5 lasts.")
    h = h.replace("5-Year Extended Warranty", "Lifetime Warranty Upgrade")
    h = h.replace("3 Months Gridless Premium", "1 Year Gridless Premium")
    h = h.replace("'$29 Value — FREE'", "'$59 Value — FREE'", 1)          # warranty popup
    h = h.replace("'$30 Value — FREE'", "'$79 Value — FREE'")             # gridless popup
    h = h.replace("Your 3-month Premium subscription", "Your 1-year Premium subscription")
    h = h.replace("Full coverage for 5 years.", "Covered for as long as you own it.")
    h = h.replace("<s style=\"color:#94a3b8\">$29</s> FREE</span>\n  </div>\n  <div class=\"stack-row free\" onclick=\"showPopup('gridless')\"",
                  "<s style=\"color:#94a3b8\">$59</s> FREE</span>\n  </div>\n  <div class=\"stack-row free\" onclick=\"showPopup('gridless')\"")
    h = h.replace('<s style="color:#94a3b8">$30</s> FREE', f'<s style="color:#94a3b8">$79</s> FREE')
    h = h.replace('<s style="color:#94a3b8">$29</s> FREE', '<s style="color:#94a3b8">$39</s> FREE')
    h = h.replace("Waterproof Bottom Upgrade", "Waterproof Bottom Fabric Upgrade")
    # add the sixth line (free returns) just above the total row
    h = h.replace('  <div class="stack-row free">\n    <span class="stack-label">Standard US Shipping</span>',
                  '  <div class="stack-row free">\n'
                  '    <span class="stack-label">Hassle-Free Returns</span>\n'
                  '    <span class="stack-val"><s style="color:#94a3b8">$4.99</s> FREE</span>\n'
                  '  </div>\n'
                  '  <div class="stack-row free">\n    <span class="stack-label">Standard US Shipping</span>')
    h = h.replace('Save $157 · Free shipping · 30-day guarantee',
                  f'Save ${save} · Free shipping · 30-day guarantee')
    h = h.replace("Includes free bonuses worth $157", f"Includes free bonuses worth ${save}")

    # ── urgency section → Batch 5, with the real fill tracker ────────────────
    h = h.replace('<div class="section-eyebrow">Limited First Batch</div>',
                  '<div class="section-eyebrow">Batch 5 · Final Run</div>')
    h = h.replace("<h2 class=\"section-title\">This Is Our First-Ever US Launch. Stock Is Limited.</h2>",
                  "<h2 class=\"section-title\">Four Batches Sold Out. This Is The Last One Of 2026.</h2>")
    h = h.replace("We're a Canadian company that spent 3 years perfecting this hammock for the "
                  "harsh Canadian wilderness. Now we're finally bringing it south of the border "
                  "— but this first batch is limited.",
                  "We build in batches and we don't overbuild. Four have sold out in a row. "
                  "Batch&nbsp;5 is the final production run of the year and the last one that "
                  "still lands before the holidays. Reservations close November 15 so the run "
                  "can ship by December 1.")

    old_tl = re.search(r'<div class="timeline fade-in">.*?</div>\n  </div>\n  <div style="text-align:center',
                       h, re.S)
    new_tl = f'''<div class="batch-wrap fade-in">
    <div class="batch-head">Batch 5 · The Last Run Of 2026</div>
    <div class="bar-outer"><div class="bar-inner" id="bar"></div></div>
    <div class="bar-stats"><strong id="pctLabel">&mdash;</strong> of Batch 5 reserved</div>
    <div class="bar-rate" id="rate"></div>
    <div id="today" class="bar-today"></div>
  </div>
  <div class="timeline fade-in">
    <div class="tl-item active">
      <div class="tl-dot"></div>
      <div class="tl-label">Now — Reserve Your Place In Batch 5</div>
      <div class="tl-desc">${price} locked in, all six upgrades included</div>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-label">November 15 — Reservations Close</div>
      <div class="tl-desc">Last day to make the December 1 run</div>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-label">December 1 — Batch 5 Ships</div>
      <div class="tl-desc">Free US shipping, duties included, orders ship in the order they were reserved</div>
    </div>
    <div class="tl-item red">
      <div class="tl-dot"></div>
      <div class="tl-label">After Batch 5 — $229. Upgrades Gone.</div>
      <div class="tl-desc">No further production runs in 2026</div>
    </div>
  </div>
  <div style="text-align:center'''
    if not old_tl:
        sys.exit("timeline block not found — light-test.html changed shape")
    h = h[:old_tl.start()] + new_tl + h[old_tl.end():]

    # ── reviews / social proof ───────────────────────────────────────────────
    h = h.replace("529", str(REVIEWS)).replace("400+ Campers", f"{REVIEWS} Campers")
    h = h.replace("400+ five-star reviews", f"{REVIEWS} five-star reviews")

    # ── FAQ ship dates ───────────────────────────────────────────────────────
    h = h.replace("Pre-orders ship in early July. Standard shipping (free) arrives around "
                  "July 30. Priority shipping ($15–20) arrives around July 15.",
                  "Batch 5 ships from our South Carolina warehouse on December 1. Shipping is "
                  "free and duties are included. Reserve by November 15 to make that run.")

    # ── final CTA ────────────────────────────────────────────────────────────
    h = h.replace("Now available in the USA for the first time ever.",
                  "Batch 5 is the final run of 2026. Ships December 1.")
    h = h.replace('<span class="price-old" style="color:#94a3b8">$336 value</span>',
                  f'<span class="price-old" style="color:#94a3b8">${VALUE} value</span>')
    h = h.replace("30-Day Money-Back Guarantee · Lifetime Warranty Upgrade Included",
                  "30-Day Money-Back Guarantee · Lifetime Warranty Included")

    # ── sticky bar: real 24h number, not a made-up viewer count ──────────────
    h = h.replace('<span class="sticky-bar-text"><span class="price-old">$336</span>',
                  f'<span class="sticky-bar-text"><span class="price-old">${VALUE}</span>')
    h = h.replace('<div class="sticky-bar-urgency"><span class="dot"></span> '
                  '<span id="viewerCount">47</span> people viewing this right now</div>',
                  '<div class="sticky-bar-urgency" id="fbLive" hidden><span class="dot"></span> '
                  '<strong id="fbNum">0</strong> reserved in the last 24 hours</div>\n'
                  '  <div class="sticky-bar-urgency" id="fbSub"></div>')
    h = h.replace('<span class="viewing-badge"><span class="dot" style="width:6px;height:6px;'
                  'background:#4ade80;border-radius:50%;display:inline-block;'
                  'animation:pulse-dot 1.5s infinite;margin-right:4px"></span>'
                  '<span id="viewerCountTop">47</span> people viewing now</span>', '')
    h = re.sub(r'\nconst vc=document\.getElementById\(.viewerCount.\);.*?setInterval\(updateViewers,8000\);',
               '\n/* viewer counter removed — the only live number on this page now comes from '
               'Shopify via batch5-status.json */', h, flags=re.S)

    # ── remaining prices last, so nothing above re-breaks ────────────────────
    h = h.replace("$336", f"${VALUE}").replace("$179", f"${price}")

    # ── tracker styles + the batch-5 feed, ported from christmas.html ────────
    css = """
<style>
/* Batch 5 fill tracker — same source of truth as christmas.html */
.batch-wrap{max-width:620px;margin:26px auto 34px;background:var(--white);
 border:1px solid #e5e7eb;border-radius:14px;padding:20px 22px;
 box-shadow:0 6px 24px rgba(0,0,0,.07)}
.batch-head{font-weight:800;font-size:.88rem;letter-spacing:.09em;text-transform:uppercase;
 color:var(--navy);text-align:center;margin-bottom:12px}
.bar-outer{height:14px;border-radius:999px;background:#e9edf2;overflow:hidden}
.bar-inner{height:100%;width:0;border-radius:999px;
 background:linear-gradient(90deg,#f59e0b,#ea580c);transition:width .9s ease}
.bar-stats{text-align:center;margin-top:10px;font-size:.92rem;color:#4b5563}
.bar-stats strong{color:var(--navy);font-weight:800;font-size:1.15rem}
.bar-rate{text-align:center;margin-top:5px;font-size:.83rem;color:#6b7280}
.bar-today{text-align:center;font-size:.83rem;color:#4b5563;margin-top:7px}
.sticky-bar-urgency[hidden]{display:none}
</style>
<script>
/* Batch 5 fill curve — Lukas's call 2026-09-25: the bar shows how far through the
   reservation window the run is, walking 60%→96% between Sep 26 and Nov 15, and
   real sales override it whenever they're ahead. The only hard number on the page
   is the 24-hour reservation count, which comes straight from Shopify. */
var BATCH={curveFrom:'2026-09-26',curveTo:'2026-11-15',curveStart:60,curveEnd:96,
 releaseSize:1500,sold:0,last24:0,all24:0,shipDate:'December 1'};
function b5render(){
  var t0=new Date(BATCH.curveFrom+'T00:00:00').getTime(),
      t1=new Date(BATCH.curveTo+'T00:00:00').getTime(),
      t=Math.min(Math.max((Date.now()-t0)/(t1-t0),0),1),
      pct=Math.max(BATCH.curveStart+(BATCH.curveEnd-BATCH.curveStart)*t,
                   Math.min(BATCH.sold/BATCH.releaseSize*100,100));
  var lbl=document.getElementById('pctLabel'); if(lbl)lbl.textContent=Math.round(pct)+'%';
  var bar=document.getElementById('bar'); if(bar)bar.style.width=pct.toFixed(1)+'%';
  var dLeft=Math.ceil((t1-Date.now())/864e5);
  var r=document.getElementById('rate');
  if(r)r.textContent=dLeft>1?'Reservations close November 15 \\u2014 '+dLeft+' days left'
    :(dLeft===1?'Last day to reserve':'Reservations have closed');
  var n24=BATCH.last24>0?BATCH.last24:BATCH.all24;
  var td=document.getElementById('today'),fb=document.getElementById('fbNum'),
      fl=document.getElementById('fbLive'),fs=document.getElementById('fbSub');
  if(n24>0){
    if(td)td.innerHTML='\\uD83D\\uDD25 <strong>'+n24+'</strong> reserved in the last 24 hours';
    if(fb)fb.textContent=n24; if(fl)fl.hidden=false;
  } else if(fl){ fl.hidden=true; }   /* never render a hardcoded 0 */
  if(fs)fs.innerHTML=dLeft>1?'Order by Nov 15 \\u00b7 <b>'+dLeft+' days left</b>'
    :(dLeft===1?'<b>Last day</b> to reserve':'Reservations closed');
}
b5render();
fetch('batch5-status.json?t='+Date.now()).then(function(r){return r.json()})
  .then(function(d){
    if(typeof d.sold==='number')BATCH.sold=d.sold;
    if(typeof d.last24==='number')BATCH.last24=d.last24;
    if(typeof d.all24==='number')BATCH.all24=d.all24;
    b5render();
  }).catch(function(){});
</script>
</body>"""
    h = h.replace("</body>", css, 1)

    out = os.path.join(HERE, outname)
    open(out, "w").write(h)
    stale = [s for s in ("$336", "$179" if price != 179 else "\x00", "529",
                         "July 15", "July 30", "First-Ever", "viewerCount") if s in h]
    print(f"  {outname:<22} ${price}  {len(h)//1024}KB  "
          + ("stale: " + ", ".join(stale) if stale else "clean"))

# 2026-10-08: Lukas moved all US pre-order variants to $179, so $159 no longer
# exists anywhere. One canonical page, one price. The $159 build is retired.
build(179, "light-b5.html")
