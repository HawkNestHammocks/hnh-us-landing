exec(open("_b4.py").read())
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#1b1a17;--mut:#4a4740;--line:#d8d2c4;--hl:#ffe98a;--red:#b3401d;--grn:#2f5d3f}
html{-webkit-text-size-adjust:100%}
body{background:#fbf8f0;color:var(--ink);
 font:17px/1.62 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
 background-image:radial-gradient(circle at 12% 8%,rgba(0,0,0,.022) 0 1px,transparent 1px),
  radial-gradient(circle at 78% 42%,rgba(0,0,0,.02) 0 1px,transparent 1px);
 background-size:26px 26px,34px 34px}
.w{max-width:640px;margin:0 auto;padding:26px 20px 60px}
.top{font:600 13px/1.4 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
 letter-spacing:.06em;text-transform:uppercase;color:var(--mut);border-bottom:2px solid var(--ink);
 padding-bottom:10px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
.top b{color:var(--red)}
h1{font-size:31px;line-height:1.24;margin:26px 0 14px;font-weight:700;letter-spacing:-.01em}
h2{font-size:22px;line-height:1.3;margin:34px 0 10px;font-weight:700}
p{margin:0 0 15px}
.lede{font-size:19px}
.hl{background:linear-gradient(180deg,transparent 58%,var(--hl) 58%,var(--hl) 94%,transparent 94%);
 padding:0 2px}
.note{font:italic 16px/1.55 inherit;color:var(--mut);border-left:3px solid var(--line);
 padding:2px 0 2px 14px;margin:0 0 16px}
ul{margin:0 0 16px 20px}li{margin-bottom:7px}
.box{border:2px solid var(--ink);background:#fffdf7;padding:18px 16px;margin:22px 0;
 box-shadow:5px 5px 0 rgba(27,26,23,.14)}
.box h3{font:700 19px/1.3 inherit;margin-bottom:10px}
.rowi{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-bottom:1px dotted var(--line);
 font-size:16px}
.rowi:last-of-type{border-bottom:0}
.rowi s{color:#8a8579}
.rowi b{color:var(--grn);font:700 13px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.08em;
 align-self:center;white-space:nowrap}
.tot{display:flex;justify-content:space-between;border-top:2px solid var(--ink);margin-top:10px;
 padding-top:11px;font-weight:700;font-size:19px}
.cta{display:block;text-align:center;background:var(--red);color:#fff;text-decoration:none;
 font:700 19px/1 ui-sans-serif,system-ui,sans-serif;padding:17px 14px;margin:18px 0 8px;
 border:2px solid #7d2a11;box-shadow:4px 4px 0 rgba(27,26,23,.3);letter-spacing:.01em}
.cta:active{transform:translate(2px,2px);box-shadow:2px 2px 0 rgba(27,26,23,.3)}
.sm{font:14px/1.5 ui-sans-serif,system-ui,sans-serif;color:var(--mut);text-align:center}
figure{margin:20px 0}
figure img{width:100%;height:auto;display:block;border:1px solid var(--line);
 box-shadow:4px 4px 0 rgba(27,26,23,.1)}
figcaption{font:14px/1.45 ui-sans-serif,system-ui,sans-serif;color:var(--mut);margin-top:7px}
.tilt{transform:rotate(-.7deg)}.tilt2{transform:rotate(.6deg)}
.q{border-top:1px solid var(--line);padding:13px 0}
.q b{display:block;margin-bottom:4px}
.q p{font-size:16px;color:var(--mut);margin:0}
.sig{font:italic 18px/1.5 inherit;margin-top:8px}
.stamp{display:inline-block;border:2px solid var(--red);color:var(--red);
 font:700 12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;padding:6px 9px;
 transform:rotate(-3deg);text-transform:uppercase}
.up{opacity:0;transform:translateY(10px);animation:u .55s ease forwards}
.up:nth-of-type(2){animation-delay:.06s}.up:nth-of-type(3){animation-delay:.12s}
@keyframes u{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.up{animation:none;opacity:1;transform:none}}

.diag{border:2px solid var(--ink);background:#fffdf7;padding:16px 14px;margin:22px 0;
 box-shadow:4px 4px 0 rgba(27,26,23,.12)}
.diag svg{width:100%;height:auto;display:block}
.dcap{font:14px/1.5 ui-sans-serif,system-ui,sans-serif;color:var(--mut);text-align:center;margin-top:10px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0}
.cols img{width:100%;height:100%;object-fit:cover;aspect-ratio:3/4;border:1px solid var(--line);
 box-shadow:3px 3px 0 rgba(27,26,23,.1)}
.inst{margin:16px 0}
.inst div{display:flex;gap:10px;padding:9px 0;border-bottom:1px dotted var(--line);font-size:16px}
.inst div:last-child{border-bottom:0}
.inst b{min-width:120px}
.inst span{color:var(--mut)}
.revs{margin:16px 0}
.rv{border-left:3px solid var(--line);padding:3px 0 3px 14px;margin-bottom:15px}
.rv .st{color:#c08a26;font-size:14px;letter-spacing:.1em}
.rv .ti{font-weight:700;margin:2px 0 1px}
.rv .by{font:13.5px/1.4 ui-sans-serif,system-ui,sans-serif;color:var(--mut)}
.steps{counter-reset:s;margin:18px 0}
.steps div{counter-increment:s;position:relative;padding:10px 0 10px 40px;border-bottom:1px dotted var(--line)}
.steps div:last-child{border-bottom:0}
.steps div::before{content:counter(s);position:absolute;left:0;top:11px;width:26px;height:26px;
 border:2px solid var(--ink);border-radius:50%;display:grid;place-items:center;
 font:700 14px/1 ui-sans-serif,system-ui,sans-serif}
.steps b{display:block}
.steps span{color:var(--mut);font-size:16px}
.bstrip{display:flex;gap:6px;margin:16px 0}
.bstrip div{flex:1;border:1.5px solid var(--line);padding:9px 4px;text-align:center;
 font:700 12px/1.3 ui-sans-serif,system-ui,sans-serif;color:var(--mut);background:#fffdf7}
.bstrip div.now{border-color:var(--red);color:var(--red);background:#fff4ef}
.bstrip div i{display:block;font-style:normal;font-size:10.5px;letter-spacing:.06em;margin-top:3px;font-weight:600}
@media(max-width:420px){h1{font-size:27px}body{font-size:16px}}
"""
rows="".join(
 f'<div class="rowi"><span>{n}</span>'
 f'<span>{"<s>$"+v+"</s> <b>FREE</b>" if free else "$"+v}</span></div>'
 for n,v,free in BUNDLE)
faq="".join(f'<div class="q"><b>{q}</b><p>{a}</p></div>' for q,a in FAQ)
specs="".join(f"<li><b>{k}:</b> {v}</li>" for k,v in SPECS)
instead="".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in INSTEAD)
revs="".join(f'<div class="rv"><div class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
 f'<div class="ti">{t}</div><div class="by">{n} &middot; verified buyer</div></div>' for t,n in REVIEWS)
steps="".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in STEPS)
bstrip="".join(f'<div class="{"now" if i==3 else ""}">Batch {i+1}<i>{"OPEN" if i==3 else "SOLD OUT"}</i></div>'
 for i in range(4))

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Batch 4 &mdash; Hawk Nest Hammock Tent Pre-Order (${PRICE})</title>
<meta name="description" content="Batch 4 is the last run of 2026. {UNITS} units, arriving {SHIP}. ${PRICE} with every upgrade included. Ships from South Carolina, duties paid.">
<link rel="icon" href="favicon-192.png">
<style>{CSS}</style></head><body>
<div class="w">
 <div class="top"><span>Hawk Nest Hammocks</span><span><b>Batch {BATCH}</b> &middot; ships {SHIP}</span></div>

 <h1 class="up">I&rsquo;m going to be honest with you about this pre-order.</h1>
 <p class="lede up">We build these in runs of a thousand or so. Batches 1, 2 and 3 all sold out before they landed. Batch {BATCH} is {UNITS} units and it&rsquo;s the last run of 2026.</p>
 <p class="up">That&rsquo;s the whole pitch. No countdown timer, no fake stock bar. Just a small Canadian company that makes one thing and can only make so many of them at a time.</p>

 <figure class="tilt"><img loading="lazy" src="story-camp.jpg" width="1000" height="1000"
  alt="A Hawk Nest hammock tent pitched between two trees with someone inside and a friend cooking beside it">
  <figcaption>Batch 3. Same thing you&rsquo;d get, minus the friend.</figcaption></figure>

 <h2>What it actually is</h2>
 <p>A hammock and a tent in one. Bug net sewn in, rain fly over the top, waterproof floor underneath, and a pocket that takes a sleeping pad up to <span class="hl">25 inches wide</span> so your back isn&rsquo;t cold.</p>
 <p class="note">A regular hammock isn&rsquo;t the same thing. No net, no cover, and below about {TEMP_COLD} the air moving underneath makes it a wind tunnel. That&rsquo;s a nap, not a night&rsquo;s sleep.</p>
 <ul>{specs}</ul>
 <p>Goes up in about five minutes once you&rsquo;ve done it twice. Tested in Canadian winters down to {TEMP_TESTED}.</p>

 <h2>What you&rsquo;d otherwise be carrying</h2>
 <div class="inst">{instead}</div>
 <p>All of that, replaced by one thing you sling between two trees. That&rsquo;s the entire reason it exists.</p>

 <figure class="tilt2"><img loading="lazy" src="story-rain.jpg" width="1000" height="1000"
  alt="Rain beading on the waterproof fly fabric of a Hawk Nest hammock tent">
  <figcaption>The fly, doing the one job a fly has.</figcaption></figure>

 <h2>The part people get wrong</h2>
 <p>Everyone worries about rain. Rain is the easy part &mdash; that&rsquo;s just fabric. <span class="hl">Cold is what ruins a night in a hammock</span>, and it comes from underneath, where your sleeping bag is squashed flat and does nothing.</p>
 <p>That&rsquo;s what the pad pocket is for. Your pad sits under your back, held in place, instead of sliding off at 2am like it does in a normal hammock.</p>
 <div class="diag">{COLD_SVG}<div class="dcap">Left: nothing under you but moving air. Right: a pad held in the pocket.</div></div>

 <h2>What you pay, and what you get</h2>
 <div class="box">
  <h3>The Batch {BATCH} pre-order</h3>
  {rows}
  <div class="tot"><span>Buy it all separately</span><span><s>${WAS}</s> ${PRICE}</span></div>
  <p class="sm" style="text-align:left;margin:10px 0 0">You keep ${KEEP}. When Batch {BATCH} is gone the price goes to ${AFTER} and the upgrades stop being free.</p>
  {cta("Reserve yours &mdash; $"+PRICE)}
  <p class="sm">Free shipping &middot; duties included &middot; 30-day refund<br>Ships from South Carolina on {SHIP}</p>
 </div>

 <figure class="tilt"><img loading="lazy" src="story-winter.jpg" width="1000" height="750"
  alt="A Hawk Nest hammock tent set up in deep snow with someone inside">
  <figcaption>Not a studio shot. That&rsquo;s a customer, in February.</figcaption></figure>

 <h2>What people who own one say</h2>
 <p>{SHIPPED} shipped so far. These are real review titles from verified buyers &mdash; their words, not ours.</p>
 <div class="revs">{revs}</div>

 <div class="cols">
  <img loading="lazy" src="story-morning.jpg" width="1000" height="663" alt="Someone inside a Hawk Nest hammock tent in the morning">
  <img loading="lazy" src="story-pack.jpg" width="900" height="1200" alt="A Hawk Nest hammock tent being unpacked">
 </div>

 <h2>Why it&rsquo;s a pre-order and not a buy button</h2>
 <p>Because we&rsquo;d rather build {UNITS} and sell them than build five thousand and eat the rest. It means you wait, and it means we don&rsquo;t raise the price to cover guesswork.</p>
 <div class="bstrip">{bstrip}</div>
 <p><span class="stamp">Batches 1&ndash;3 sold out</span></p>

 <h2>What happens after you order</h2>
 <div class="steps">{steps}</div>

 <h2>Who this isn&rsquo;t for</h2>
 <p>If you camp above the treeline, there&rsquo;s nothing to hang it from and you want a tent. If you need it next week, it won&rsquo;t be there. And if you&rsquo;ve never slept in a hammock, know that the first night takes some getting used to &mdash; you lie across it on a diagonal, not straight down the middle.</p>
 <p>Told you it wouldn&rsquo;t be a sales pitch.</p>

 <div class="cols">
  <img loading="lazy" src="story-ugc-setup.jpg" width="760" height="1351" alt="A customer setting up their Hawk Nest hammock">
  <img loading="lazy" src="story-open.jpg" width="1000" height="1333" alt="A Hawk Nest hammock tent open with someone inside, mountains behind">
 </div>
 <p class="sm" style="text-align:left;margin-top:-6px">Left: a customer&rsquo;s own footage, setting one up.</p>

 <h2>Straight answers</h2>
 {faq}

 <h2>That&rsquo;s it</h2>
 <p>If it&rsquo;s not for you, no hard feelings. If it is, get on Batch {BATCH} before it goes the way of the other three.</p>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="sm">30 days to change your mind. Full refund, no questions.</p>
 <p class="sig">&mdash; Lukas, Hawk Nest Hammocks</p>
</div>
</body></html>"""
open("b4-plain.html","w").write(HTML)
print("b4-plain.html", len(HTML)//1024,"KB")
