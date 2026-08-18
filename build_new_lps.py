# Builds three NEW US pre-order landing pages. Same brand system as the winner
# (max-value-long-gift.html), three different persuasion mechanics.
import pathlib

import lp_parts as L

# These three pages had their OWN copy of the cart link, which is how they missed the
# multi-buy picker the first time round. One source of truth now.
CHECKOUT = L.CHECKOUT

HEAD = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--earth:#3b2f1e;--bark:#5c4a32;--sand:#e8dcc8;--cream:#f5f0e6;--parchment:#faf7f0;
--rust:#b45309;--rust-dark:#92400e;--forest:#1a3a1a;--slate:#374151;--muted:#6b7280;
--serif:'Crimson Pro',Georgia,serif;--sans:'DM Sans',-apple-system,sans-serif}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--sans);background:var(--parchment);color:var(--slate);
 -webkit-font-smoothing:antialiased;line-height:1.6}
.wrap{max-width:680px;margin:0 auto;padding:0 22px}
.eyebrow{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--rust);font-weight:700}
h1{font-family:var(--serif);font-size:clamp(2.1rem,7vw,3.3rem);line-height:1.08;color:var(--earth);
 font-weight:700;letter-spacing:-.02em;text-wrap:balance}
h2{font-family:var(--serif);font-size:clamp(1.6rem,5vw,2.2rem);line-height:1.15;color:var(--earth);
 font-weight:700;margin-bottom:14px;text-wrap:balance}
h3{font-family:var(--serif);font-size:1.25rem;color:var(--earth);font-weight:700;margin-bottom:6px}
p{margin-bottom:16px;font-size:1.04rem}
p.lead{font-size:1.18rem;color:var(--bark)}
section{padding:52px 0;border-bottom:1px solid rgba(92,74,50,.13)}
.hero{padding:56px 0 44px;background:linear-gradient(180deg,var(--cream),var(--parchment))}
/* offer */
.offer{background:var(--earth);color:var(--cream);border-radius:14px;padding:30px 26px;margin:26px 0}
.offer h3{color:var(--cream);font-size:1.5rem}
.price-row{display:flex;align-items:baseline;gap:12px;margin:14px 0 4px}
.price{font-family:var(--serif);font-size:3rem;font-weight:700;color:#fff;line-height:1}
.was{font-size:1.05rem;color:#c9bda6;text-decoration:line-through}
.save{display:inline-block;background:var(--rust);color:#fff;font-size:.74rem;font-weight:700;
 letter-spacing:.09em;text-transform:uppercase;padding:5px 11px;border-radius:99px;margin-left:4px}
.incl{list-style:none;margin:18px 0 0}
.incl li{padding:9px 0;border-top:1px solid rgba(232,220,200,.16);display:flex;
 justify-content:space-between;gap:14px;font-size:.95rem}
.incl li span:last-child{color:#9fb98c;font-weight:600;white-space:nowrap}
.cta{display:block;background:linear-gradient(180deg,#c2620a,var(--rust-dark));color:#fff;
 text-align:center;font-weight:700;font-size:1.12rem;padding:19px;border-radius:11px;
 text-decoration:none;margin-top:22px;box-shadow:0 6px 18px rgba(146,64,14,.32)}
.cta small{display:block;font-weight:500;font-size:.8rem;opacity:.9;margin-top:4px}
.trust{text-align:center;font-size:.84rem;color:var(--muted);margin-top:14px}
.ship{background:#fff8e8;border:1px solid #f0dfae;border-radius:11px;padding:16px 18px;margin:22px 0;
 font-size:.93rem}
.ship b{color:var(--earth)}
/* comparison table */
table{width:100%;border-collapse:collapse;margin:18px 0;font-size:.95rem}
th,td{padding:11px 8px;text-align:left;border-bottom:1px solid rgba(92,74,50,.14)}
th{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr.total td{font-weight:700;color:var(--earth);border-top:2px solid var(--earth);border-bottom:none}
/* objection blocks */
.obj{border-left:3px solid var(--rust);padding:4px 0 4px 18px;margin:26px 0}
.obj .q{font-family:var(--serif);font-size:1.28rem;color:var(--earth);font-weight:700;margin-bottom:8px}
/* misc */
.stat{display:flex;gap:26px;flex-wrap:wrap;margin:22px 0}
.stat div{flex:1;min-width:120px}
.stat b{display:block;font-family:var(--serif);font-size:2rem;color:var(--earth);line-height:1}
.stat span{font-size:.82rem;color:var(--muted)}
.note{background:var(--cream);border-radius:10px;padding:16px 18px;font-size:.93rem;margin:20px 0}
footer{padding:38px 0 60px;text-align:center;font-size:.8rem;color:var(--muted)}
blockquote{font-family:var(--serif);font-size:1.3rem;font-style:italic;color:var(--bark);
 border-left:3px solid var(--sand);padding-left:18px;margin:22px 0}
</style></head><body>
"""

def offer_block(kicker="The pre-order"):
    return f"""
<div class="offer">
  <div class="eyebrow" style="color:#e0b678">{kicker}</div>
  <h3>Hawk Nest V.3 — Complete Kit</h3>
  <div class="price-row"><span class="price">$159</span><span class="was">$429</span>
    <span class="save">Save 63%</span></div>
  <ul class="incl">
    <li><span>Hawk Nest V.3 all-season hammock&#8209;tent</span><span>Included</span></li>
    <li><span>Waterproof bottom upgrade</span><span>$39 → free</span></li>
    <li><span>Waterproof carrying bag</span><span>$19 → free</span></li>
    <li><span>Lifetime warranty</span><span>$59 → free</span></li>
    <li><span>Gridless app — 1 year</span><span>Included</span></li>
    <li><span>Free US shipping &amp; free returns</span><span>Included</span></li>
  </ul>
  <a class="cta" href="{CHECKOUT}">Reserve mine — $159
    <small>Pay over time available · Ships Sept 15</small></a>
  <div class="trust" style="color:#c9bda6">Ships from South Carolina · duties included · nothing to pay on delivery</div>
</div>
<div class="ship"><b>Batch status:</b> pre-orders ship <b>Sept 15</b>, in time for fall and
well before the holidays. Pre-order batches ship in <b>Navy</b>. You're charged today and
your place in the batch is held in the order it was taken.</div>
"""

QTY_CSS = """
<style>
.qtyp{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;margin:0 0 14px}
.qtyp-l{font-size:.78rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.qtyp-b{display:inline-flex;gap:6px}
.qtyp-b button{min-width:46px;padding:9px 12px;border-radius:9px;cursor:pointer;font:inherit;
 font-weight:700;font-size:.95rem;line-height:1;background:#fff;color:var(--earth);
 border:1.5px solid rgba(92,74,50,.28);transition:.14s}
.qtyp-b button:hover{border-color:var(--rust)}
.qtyp-b button.on{background:var(--rust);border-color:var(--rust);color:#fff}
.qtyp-n{font-size:.76rem;color:var(--muted);flex-basis:100%;text-align:center}
.offer .qtyp-l,.offer .qtyp-n{color:#c9bda6}
.offer .qtyp-b button{background:rgba(255,255,255,.08);color:var(--cream);border-color:rgba(255,255,255,.28)}
.offer .qtyp-b button.on{background:var(--rust);border-color:var(--rust);color:#fff}
</style>"""

# Shopify's checkout has no quantity control and the permalink skips the cart, so without
# this a customer who wants two complete kits has no way to say so. The automatic discount
# already scales per unit — this just has to move all six variant IDs together.
QTY_JS = r"""
<script>
(function(){
 var RE=/\/cart\/([0-9]+(?::[0-9]+)?(?:,[0-9]+(?::[0-9]+)?)*)/;
 function links(){return Array.prototype.filter.call(
   document.querySelectorAll('a[href*="/cart/"]'),
   function(a){return RE.test(a.getAttribute('href')||'')});}
 function setQty(q){
   links().forEach(function(a){
     a.href=a.getAttribute('href').replace(RE,function(m,list){
       return '/cart/'+list.split(',').map(function(x){return x.split(':')[0]+':'+q}).join(',');
     });
   });
   document.querySelectorAll('.qtyp-b button').forEach(function(b){
     b.classList.toggle('on',b.getAttribute('data-q')===String(q));});
 }
 var ls=links(); if(!ls.length)return;
 ls.forEach(function(a){
   var w=document.createElement('div'); w.className='qtyp';
   w.innerHTML='<span class="qtyp-l">How many?</span><span class="qtyp-b">'+
     [1,2,3].map(function(n){return '<button type="button" data-q="'+n+'"'+
       (n===1?' class="on"':'')+'>'+n+'</button>'}).join('')+'</span>'+
     '<span class="qtyp-n">Each one is a complete kit — hammock plus all six upgrades.</span>';
   a.parentNode.insertBefore(w,a);
 });
 document.addEventListener('click',function(e){
   var b=e.target.closest?e.target.closest('.qtyp-b button'):null;
   if(!b)return; e.preventDefault();
   setQty(parseInt(b.getAttribute('data-q'),10)||1);
 });
})();
</script>"""

FOOT = QTY_CSS + """
<footer><div class="wrap">Hawk Nest Hammocks · Built in Canada · Shipped from South Carolina<br>
4.8 out of 5 from 400+ verified reviews</div></footer>
""" + QTY_JS + """
</body></html>"""

pathlib.Path("_lp_common.py").write_text("")
print("common ready")

# ══════════════ A. THE COLD MATH — for the analytical buyer ══════════════
A = HEAD.replace("__TITLE__","The Cheapest Way to Sleep Outside Is Not a Tent | Hawk Nest")\
        .replace("__DESC__","We priced out a full ground-sleeping system against one hammock-tent. The numbers weren't close.") + f"""
<div class="hero"><div class="wrap">
  <div class="eyebrow">US pre-order · ships Sept 15</div>
  <h1>We Priced Out Every Way to Sleep Outside. The Tent Lost.</h1>
  <p class="lead">Not an opinion. A spreadsheet. Here's what a real ground-sleeping
  setup actually costs you in dollars, in pounds, and in mornings.</p>
</div></div>

<section><div class="wrap">
  <h2>What sleeping on the ground really costs</h2>
  <p>Everyone budgets for the tent. Almost nobody budgets for the rest of it — and the rest
  of it is where the money goes. This is a mid-range setup, the kind most people actually
  end up owning after two or three seasons of upgrading.</p>
  <table>
    <tr><th>The ground system</th><th class="num">Cost</th><th class="num">Weight</th></tr>
    <tr><td>2-person backpacking tent</td><td class="num">$220</td><td class="num">4 lb 6 oz</td></tr>
    <tr><td>Sleeping pad (R-4, insulated)</td><td class="num">$150</td><td class="num">1 lb 2 oz</td></tr>
    <tr><td>Footprint / groundsheet</td><td class="num">$45</td><td class="num">7 oz</td></tr>
    <tr><td>Stakes, guylines, repair kit</td><td class="num">$35</td><td class="num">9 oz</td></tr>
    <tr class="total"><td>Total</td><td class="num">$450</td><td class="num">6 lb 8 oz</td></tr>
  </table>
  <p>And you still wake up on a root. You still hunt for twenty minutes for ground flat enough
  and dry enough to pitch on. You still find the puddle at 2am, because water runs downhill and
  you are downhill.</p>
</div></section>

<section><div class="wrap">
  <h2>The same night, off the ground</h2>
  <p>A hammock-tent removes the two line items that cost the most and weigh the most: the
  footprint you're sleeping on, and the pad you need because the ground steals your heat.
  You're not insulating yourself from the earth, because you're not touching it.</p>
  <table>
    <tr><th>Hawk Nest V.3</th><th class="num">Cost</th><th class="num">Weight</th></tr>
    <tr><td>All-season hammock-tent, bug net, rain fly</td><td class="num">$159</td><td class="num">3–4 lb</td></tr>
    <tr><td>Waterproof bottom</td><td class="num">free</td><td class="num">incl.</td></tr>
    <tr><td>Waterproof carry bag</td><td class="num">free</td><td class="num">incl.</td></tr>
    <tr><td>Footprint</td><td class="num">not needed</td><td class="num">0</td></tr>
    <tr><td>Sleeping pad</td><td class="num">optional</td><td class="num">0</td></tr>
    <tr class="total"><td>Total</td><td class="num">$159</td><td class="num">3–4 lb</td></tr>
  </table>
  <div class="stat">
    <div><b>$291</b><span>less than the ground setup</span></div>
    <div><b>2.5 lb</b><span>off your back</span></div>
    <div><b>0</b><span>minutes spent finding flat ground</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Where the money actually went</h2>
  <p>Fair question: how is it $159 when the parts alone are worth more than that?</p>
  <p>Because this is a <b>pre-order</b>. You're buying from the production batch before it
  lands, which means we're not paying to warehouse it, not paying to float inventory, and not
  paying a retailer's margin. That saving goes to you instead, and in exchange you wait until
  September 15.</p>
  <p>That's the whole trade. Not a discount, not a gimmick — you're early, so it's cheaper.</p>
  <blockquote>The pad you don't buy is the cheapest pad you'll ever own.</blockquote>
</div></section>

<section><div class="wrap">
  <h2>Reserve yours</h2>
  {offer_block()}
  <div class="note"><b>Why the price won't be this again.</b> Once this batch lands and
  goes to general stock, it carries warehousing, and the extras stop being free. The $159
  is the pre-order number, not the retail number.</div>
</div></section>
""" + FOOT
pathlib.Path("us-math.html").write_text(A)
print("wrote us-math.html", len(A))

# ══════════════ B. THE FIRST NIGHT — sensory long-form, single-night arc ══════════════
B = HEAD.replace("__TITLE__","The First Night You Sleep Off the Ground | Hawk Nest")\
        .replace("__DESC__","Most people remember it. Here's what actually happens, hour by hour, the first night you don't sleep on the ground.") + f"""
<div class="hero"><div class="wrap">
  <div class="eyebrow">US pre-order · ships Sept 15</div>
  <h1>Nobody Forgets the First Night They Sleep Off&nbsp;the&nbsp;Ground</h1>
  <p class="lead">Not because it's dramatic. Because nothing goes wrong. Here's that night,
  hour by hour.</p>
</div></div>

<section><div class="wrap">
  <div class="eyebrow">6:40 pm</div>
  <h2>You stop looking for flat ground</h2>
  <p>This is the part people underestimate. On the ground, you spend the last twenty minutes
  of daylight walking in circles, testing for the spot that isn't sloped, isn't rocky, isn't
  a drainage line. You settle for the least-bad one.</p>
  <p>Off the ground, you need two trees. That's the whole search. The slope stops mattering.
  The rocks stop mattering. The site you'd have walked past becomes the site you take.</p>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">7:15 pm</div>
  <h2>It's up before the light goes</h2>
  <p>Straps around two trunks, hammock clipped in, fly over the ridgeline, bug net zipped.
  There are no stakes to lose, no poles to thread in the dark, no corner to peg out on a
  root that won't take it.</p>
  <p>You're finished while there's still light to cook by. That alone changes the shape of
  the evening.</p>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">10:30 pm</div>
  <h2>The cold doesn't come up at you</h2>
  <p>On the ground, the earth is a heat sink. It pulls warmth out of you all night, which is
  the entire reason an insulated pad exists. Off the ground, there's nothing beneath you to
  pull it — the V.3's pad pocket takes a pad up to 25 inches wide if you want one for deep
  cold, and most of the year you won't reach for it.</p>
  <p>You notice this as an absence. Nothing is leaching heat out of your back.</p>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">2:00 am</div>
  <h2>It rains, and it doesn't matter</h2>
  <p>This is the moment that converts people. On the ground, rain means water finding the
  low point, and you are the low point. Off the ground, water runs under you and away.</p>
  <p>The detachable rain fly sheds it. The bug net keeps everything else out. You hear it,
  and then you go back to sleep, and that's the whole event.</p>
  <blockquote>The first time it rains and you don't get up to check anything — that's when
  you stop being a tent person.</blockquote>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">6:20 am</div>
  <h2>You wake up without the inventory</h2>
  <p>You know the ground-sleeping wake-up: the mental list of what hurts. Hip, shoulder,
  lower back, neck. You run it before you open your eyes.</p>
  <p>Off the ground, laid slightly diagonal, your spine is flat and your weight is spread
  across the whole surface instead of pressed into four contact points. There's no list to
  run. You just wake up.</p>
  <p>Then you unclip, stuff it in the bag, and you're walking in about four minutes — because
  there's nothing to dry out, nothing to shake dirt off, and no stakes to dig out of wet ground.</p>
</div></section>

<section><div class="wrap">
  <h2>Take the first night</h2>
  <p>400+ people have now done it and left us 4.8 out of 5. The pre-order is the cheapest
  it will be, because you're buying before the batch lands.</p>
  {offer_block()}
  <div class="note"><b>If it isn't for you, send it back.</b> Free returns, both ways, and a
  lifetime warranty on the hammock itself. The risk of trying it is the shipping time, and
  we cover that too.</div>
</div></section>
""" + FOOT
pathlib.Path("us-firstnight.html").write_text(B)
print("wrote us-firstnight.html", len(B))

# ══════════════ C. THE OBJECTION PAGE — answers the doubt, in order ══════════════
OBJ = [
 ("“I'll be cold. Hammocks are freezing.”",
  "That's true of a bare summer hammock and it's the single most common reason people bounce "
  "off the idea. The V.3 is built as an all-season shelter, not a backyard hammock: enclosed "
  "body, full bug net, detachable rain fly, and a pad pocket that takes a pad up to 25 inches "
  "wide for genuine winter use. Most of the year you won't need the pad. In deep cold you will, "
  "same as any shelter."),
 ("“What happens when it rains?”",
  "Water runs downhill, and off the ground you're not at the bottom of the hill any more. "
  "The rain fly sheds it, the waterproof bottom panel is included free with this pre-order, "
  "and there's no groundsheet for a puddle to pool on. Rain is the thing hammock sleepers "
  "worry about least, which surprises people."),
 ("“My back is bad. Won't I be folded in half?”",
  "That's the banana-shape problem, and it comes from lying straight down the middle. Lie "
  "slightly diagonal and the fabric flattens out under you. Your weight spreads over the "
  "whole surface instead of pressing into hip, shoulder and heel. A lot of our reviews are "
  "from people who came to it because the ground was hurting them."),
 ("“What if there are no trees?”",
  "Then it's the wrong shelter for that trip, and we'd rather say so. Above the treeline, on "
  "open desert or on beach sand, take a tent. Everywhere with two anchor points about 10 to "
  "15 feet apart, this is faster and more comfortable. Most people aren't camping above the "
  "treeline most weekends."),
 ("“How long does it take to set up?”",
  "Under five minutes once you've done it twice, and the first time is mostly reading. Two "
  "straps, clip in, fly over the ridgeline, zip the net. No poles to thread, no stakes to "
  "lose, nothing to peg into ground that won't hold a stake."),
 ("“Why is it $159 when it looks like it should be $400?”",
  "Because it's a pre-order. You're buying from the September batch before it lands, so we're "
  "not paying to warehouse it or float the inventory, and there's no retailer margin in the "
  "middle. That saving is the discount. What you give up is time — it ships September 15."),
 ("“Is this a real company or a dropship?”",
  "Real company, and the reason to believe it is the volume: over a thousand units shipped, "
  "400+ verified reviews averaging 4.8, a lifetime warranty we actually honour, and a support "
  "inbox we answer. Designed in Canada, and your order ships from South Carolina with duties "
  "already covered."),
 ("“What if I hate it?”",
  "Send it back, free, both directions. We'd rather eat the shipping than have it sit in your "
  "garage. The hammock carries a lifetime warranty on top of that."),
]
objs = "".join(f'<div class="obj"><div class="q">{q}</div><p>{a}</p></div>' for q,a in OBJ)

C = HEAD.replace("__TITLE__","Everything You're Worried About, Answered | Hawk Nest V.3")\
        .replace("__DESC__","The eight real objections to sleeping in a hammock-tent, answered straight — including the ones where the honest answer is buy a tent instead.") + f"""
<div class="hero"><div class="wrap">
  <div class="eyebrow">US pre-order · ships Sept 15</div>
  <h1>You're Not Sold Yet. Good — Here's Every Objection, Answered.</h1>
  <p class="lead">We've read a few thousand comments. The same eight doubts come up every
  time. Two of them are completely right, and we'll tell you which.</p>
</div></div>

<section><div class="wrap">
  {objs}
</div></section>

<section><div class="wrap">
  <h2>The two we agree with</h2>
  <p>If you camp above the treeline, or on open sand, this isn't your shelter and no amount
  of copy changes that. Buy a tent.</p>
  <p>And if you need it in your hands next week, this is the wrong purchase — it's a
  pre-order and it ships September 15. If either of those is you, we'd genuinely rather you
  didn't order.</p>
  <p>For everyone else, the honest pitch is simple: it's faster to pitch, it doesn't need
  flat ground, it doesn't need a pad most of the year, and it costs less than the tent
  system it replaces.</p>
</div></section>

<section><div class="wrap">
  <h2>If none of that put you off</h2>
  {offer_block()}
  <div class="stat">
    <div><b>1,000+</b><span>units shipped</span></div>
    <div><b>4.8/5</b><span>from 400+ reviews</span></div>
    <div><b>Lifetime</b><span>warranty on the hammock</span></div>
  </div>
</div></section>
""" + FOOT
pathlib.Path("us-objections.html").write_text(C)
print("wrote us-objections.html", len(C))
