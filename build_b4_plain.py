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
@media(max-width:420px){h1{font-size:27px}body{font-size:16px}}
"""
rows="".join(
 f'<div class="rowi"><span>{n}</span>'
 f'<span>{"<s>$"+v+"</s> <b>FREE</b>" if free else "$"+v}</span></div>'
 for n,v,free in BUNDLE)
faq="".join(f'<div class="q"><b>{q}</b><p>{a}</p></div>' for q,a in FAQ)
specs="".join(f"<li><b>{k}:</b> {v}</li>" for k,v in SPECS)

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Batch 4 &mdash; Hawk Nest Hammock Tent Pre-Order ($159)</title>
<meta name="description" content="Batch 4 is the last run of 2026. 1,500 units, arriving October 15. $159 with every upgrade included. Ships from South Carolina, duties paid.">
<link rel="icon" href="favicon-192.png">
<style>{CSS}</style></head><body>
<div class="w">
 <div class="top"><span>Hawk Nest Hammocks</span><span><b>Batch {BATCH}</b> &middot; ships {SHIP}</span></div>

 <h1 class="up">I&rsquo;m going to be honest with you about this pre-order.</h1>
 <p class="lede up">We build these in runs of a thousand or so. Batches 1, 2 and 3 all sold out before they landed. Batch {BATCH} is {UNITS} units and it&rsquo;s the last run of 2026.</p>
 <p class="up">That&rsquo;s the whole pitch. No countdown timer, no fake stock bar. Just a small Canadian company that makes one thing and can only make so many of them at a time.</p>

 <figure class="tilt"><img loading="lazy" src="story-camp.jpg" width="1000" height="667"
  alt="A Hawk Nest hammock tent pitched between two trees at a forest camp">
  <figcaption>Batch 3, somewhere in the Rockies. Same thing you&rsquo;d get.</figcaption></figure>

 <h2>What it actually is</h2>
 <p>A hammock and a tent in one. Bug net sewn in, rain fly over the top, waterproof floor underneath, and a pocket that takes a sleeping pad up to <span class="hl">25 inches wide</span> so your back isn&rsquo;t cold.</p>
 <p class="note">A regular hammock isn&rsquo;t the same thing. No net, no cover, and below about {TEMP_COLD} the air moving underneath makes it a wind tunnel. That&rsquo;s a nap, not a night&rsquo;s sleep.</p>
 <ul>{specs}</ul>
 <p>Goes up in about four minutes once you&rsquo;ve done it twice. Tested in Canadian winters down to {TEMP_TESTED}.</p>

 <h2>What you pay, and what you get</h2>
 <div class="box">
  <h3>The Batch {BATCH} pre-order</h3>
  {rows}
  <div class="tot"><span>Buy it all separately</span><span><s>${WAS}</s> ${PRICE}</span></div>
  <p class="sm" style="text-align:left;margin:10px 0 0">You keep ${KEEP}. When Batch {BATCH} is gone the price goes to ${AFTER} and the upgrades stop being free.</p>
  {cta("Reserve yours &mdash; $"+PRICE)}
  <p class="sm">Free shipping &middot; duties included &middot; 30-day refund<br>Ships from South Carolina on {SHIP}</p>
 </div>

 <figure class="tilt2"><img loading="lazy" src="story-winter.jpg" width="1000" height="750"
  alt="The hammock tent set up in deep snow with someone inside">
  <figcaption>Not a studio shot. That&rsquo;s a customer, in February.</figcaption></figure>

 <h2>Why it&rsquo;s a pre-order and not a buy button</h2>
 <p>Because we&rsquo;d rather build {UNITS} and sell them than build five thousand and eat the rest. It means you wait, and it means we don&rsquo;t raise the price to cover guesswork. <span class="hl">{SHIPPED} shipped so far.</span></p>
 <p><span class="stamp">Batches 1&ndash;3 sold out</span></p>

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
