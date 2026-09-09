exec(open("_b4.py").read())
# Real, verified review titles + names as they appear on the current page. We only hold the
# titles locally, so no review bodies are written here — nothing invented.
REVIEWS=[("Algonquin Park, Ontario true Hawknest test","Pat Christie"),
 ("Best sleep in the backcountry in a long time","Jordan Danchuk"),
 ("The ultimate backcountry sleep system!","Cooper Mercer"),
 ("A great system for moto-camping","Brandon Williams"),
 ("Most comfortable hammock","MR MOUNTAIN"),
 ("Very spacious!","Jesse Stanley")]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#17211C;--mut:#4E5B54;--soft:#7C8A83;--line:#E1E3DC;--paper:#FBFAF6;
 --grn:#1E3A2B;--grn2:#2A5340;--org:#E05F18;--org2:#B8460D;--gold:#C79A3E;
 --s1:0 1px 2px rgba(23,33,28,.05),0 6px 14px rgba(23,33,28,.06);
 --s2:0 3px 8px rgba(23,33,28,.07),0 18px 40px rgba(23,33,28,.12)}
html{-webkit-text-size-adjust:100%}
body{background:var(--paper);color:var(--ink);
 font:400 19px/1.68 "Crimson Pro",Georgia,serif;-webkit-font-smoothing:antialiased}
.w{max-width:660px;margin:0 auto;padding:0 22px}
.n{font-family:"DM Sans",system-ui,sans-serif}
h1{font-size:clamp(33px,7.4vw,50px);line-height:1.1;font-weight:600;letter-spacing:-.015em}
h2{font-size:clamp(25px,5vw,34px);line-height:1.16;font-weight:600;margin:0 0 12px;letter-spacing:-.01em}
h3{font:700 20px/1.3 "DM Sans",sans-serif;margin-bottom:7px}
p{margin:0 0 19px}
p.big{font-size:21px}
header{text-align:center;padding:24px 0 4px}
header img{height:42px;width:auto}
.kick{display:inline-block;font:700 11.5px/1 "DM Sans",sans-serif;letter-spacing:.18em;
 text-transform:uppercase;color:var(--org2);background:#FDEDE3;border:1px solid #F6CFB6;
 border-radius:99px;padding:8px 14px;box-shadow:var(--s1)}
.ch{font:700 11.5px/1 "DM Sans",sans-serif;letter-spacing:.2em;text-transform:uppercase;
 color:var(--soft);margin:0 0 10px}
section{padding:34px 0}
figure{margin:26px 0}
figure img{width:100%;height:auto;display:block;border-radius:14px;box-shadow:var(--s2)}
figcaption{font:14.5px/1.5 "DM Sans",sans-serif;color:var(--soft);margin-top:9px;text-align:center}
.bleed{margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw);max-width:100vw}
.bleed img{border-radius:0}
.pull{border-left:3px solid var(--org);padding:4px 0 4px 18px;margin:26px 0;
 font-size:23px;line-height:1.42;color:var(--grn)}
.detail{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;margin:26px 0;
 box-shadow:var(--s1)}
.detail .ch{color:var(--org2)}
.detail ul{margin:0;padding-left:19px;font:16px/1.6 "DM Sans",sans-serif;color:var(--mut)}
.detail li{margin-bottom:6px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:26px 0}
.two img{width:100%;height:100%;object-fit:cover;border-radius:12px;box-shadow:var(--s1);aspect-ratio:3/4}
.revs{display:grid;gap:9px;margin:22px 0}
.rv{background:#fff;border:1px solid var(--line);border-radius:12px;padding:13px 15px;box-shadow:var(--s1)}
.rv .st{color:var(--gold);font-size:14px;letter-spacing:.08em}
.rv .ti{font:600 16.5px/1.35 "DM Sans",sans-serif;margin:4px 0 3px}
.rv .by{font:13px/1 "DM Sans",sans-serif;color:var(--soft)}
.rv .by b{color:var(--grn2);font-weight:600}
.batch{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:22px 0}
.bc{border:1px solid var(--line);background:#fff;border-radius:11px;padding:12px 4px;text-align:center;
 box-shadow:var(--s1)}
.bc .a{font:700 11px/1 "DM Sans",sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--soft)}
.bc .b{font:700 12.5px/1 "DM Sans",sans-serif;margin-top:7px;color:var(--soft)}
.bc.now{background:linear-gradient(180deg,#FFF4EC,#FCE6D8);border-color:#F2C3A5}
.bc.now .a,.bc.now .b{color:var(--org2)}
.offer{background:linear-gradient(180deg,#FFFFFF,#F6F7F2);border:1px solid var(--line);
 border-radius:20px;padding:24px 20px;box-shadow:var(--s2);margin:26px 0}
.bi{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:11px 0;
 border-bottom:1px solid var(--line);font:16px/1.4 "DM Sans",sans-serif}
.bi:last-of-type{border-bottom:0}
.bi s{color:var(--soft);font-size:14px}
.tag{font:800 10.5px/1 "DM Sans",sans-serif;letter-spacing:.1em;color:#fff;background:var(--grn2);
 border-radius:6px;padding:5px 8px}
.tot{display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid var(--ink);
 margin-top:13px;padding-top:15px}
.tot .l{font:600 14.5px/1.3 "DM Sans",sans-serif;color:var(--mut)}
.tot .p{font-size:42px;font-weight:600;line-height:1}
.tot .p s{font-size:19px;color:var(--soft);margin-right:7px}
.keep{text-align:center;font:700 15px/1 "DM Sans",sans-serif;color:var(--grn2);margin:12px 0 2px}
.cta{display:block;text-align:center;text-decoration:none;color:#fff;
 font:700 18px/1 "DM Sans",sans-serif;padding:19px 18px;border-radius:13px;margin-top:16px;
 background:linear-gradient(180deg,var(--org),var(--org2));
 box-shadow:0 1px 0 rgba(255,255,255,.35) inset,0 10px 24px rgba(184,70,13,.3),var(--s1);
 transition:transform .16s,box-shadow .16s}
.cta:hover{transform:translateY(-1px)}
.cta:active{transform:translateY(1px)}
.fine{font:14px/1.55 "DM Sans",sans-serif;color:var(--soft);text-align:center;margin-top:10px}
details{background:#fff;border:1px solid var(--line);border-radius:12px;margin-bottom:8px;box-shadow:var(--s1)}
summary{cursor:pointer;padding:15px 17px;font:700 16.5px/1.35 "DM Sans",sans-serif;list-style:none;
 display:flex;justify-content:space-between;gap:12px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--org2);font-size:21px;font-weight:400;line-height:1}
details[open] summary::after{content:"\\2013"}
details p{padding:0 17px 16px;margin:0;font:15.5px/1.6 "DM Sans",sans-serif;color:var(--mut)}
footer{padding:32px 0 54px;text-align:center;color:var(--soft);font:14px/1.6 "DM Sans",sans-serif}

.inline{background:linear-gradient(180deg,#FFFFFF,#F7F6F1);border:1px solid var(--line);
 border-radius:18px;padding:20px;margin:30px 0;box-shadow:var(--s2);text-align:center}
.inline .h{font:700 17px/1.35 "DM Sans",sans-serif;color:var(--ink);margin-bottom:4px}
.inline .s{font:14.5px/1.5 "DM Sans",sans-serif;color:var(--soft);margin-bottom:2px}
.sci{background:#fff;border:1px solid var(--line);border-left:4px solid var(--grn2);
 border-radius:14px;padding:19px 20px;margin:26px 0;box-shadow:var(--s1)}
.sci .lb{font:700 11px/1 "DM Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;
 color:var(--grn2);margin-bottom:9px}
.sci p{font:16px/1.6 "DM Sans",sans-serif;margin:0 0 11px}
.sci .cite{font:13px/1.5 "DM Sans",sans-serif;color:var(--soft);margin:0}
.sci .cite a{color:var(--grn2)}
.stat{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:24px 0}
.sn{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 15px;
 box-shadow:var(--s1);text-align:center}
.sn b{display:block;font-family:"Crimson Pro",serif;font-size:32px;font-weight:600;line-height:1;color:var(--grn)}
.sn span{display:block;font:13.5px/1.4 "DM Sans",sans-serif;color:var(--soft);margin-top:7px}
.r{opacity:0;transform:translateY(15px)}
.r.in{opacity:1;transform:none;transition:opacity .65s cubic-bezier(.2,.7,.3,1),transform .65s cubic-bezier(.2,.7,.3,1)}
@media (prefers-reduced-motion:reduce){.r,.r.in{opacity:1;transform:none;transition:none}}
"""
def fig(src,w,h,alt,cap,cls=""):
    return (f'<figure class="r {cls}"><img loading="lazy" decoding="async" src="{src}" width="{w}" '
            f'height="{h}" alt="{alt}"><figcaption>{cap}</figcaption></figure>')
def inline(h,sub):
    return (f'<div class="inline r"><div class="h">{h}</div><div class="s">{sub}</div>'
            + cta("Reserve yours &mdash; $"+PRICE) +
            f'<p class="fine">Free shipping &middot; duties included &middot; 30-day refund</p></div>')
revs="".join(f'<div class="rv"><div class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
 f'<div class="ti">{t}</div><div class="by"><b>{n}</b> &middot; Verified buyer</div></div>'
 for t,n in REVIEWS)
bundle="".join(f'<div class="bi"><span>{n}</span><span>'
 f'{"<s>$"+v+"</s> <span class=tag>FREE</span>" if free else "$"+v}</span></div>'
 for n,v,free in BUNDLE)
batch="".join(f'<div class="bc{" now" if i==3 else ""}"><div class="a">Batch {i+1}</div>'
 f'<div class="b">{"Open now" if i==3 else "Sold out"}</div></div>' for i in range(4))
faq="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)
inbox="".join(f'<li><b>{a}</b> &mdash; {b}</li>' for a,b in INBOX)

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>200 Nights Off The Ground &mdash; Hawk Nest V.3, Batch {BATCH}</title>
<meta name="description" content="The story behind the Hawk Nest All-Season Hammock Tent, and why Batch {BATCH} is the last run of 2026. ${PRICE} with every upgrade included, arriving {SHIP}.">
<link rel="icon" href="favicon-192.png">
{FONTS}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;600;700;800&display=swap">
<style>{CSS}</style></head><body>
<header><img src="hnh-logo-sm.webp" alt="Hawk Nest Hammocks" width="340" height="266" fetchpriority="high"></header>

<div class="w">
 <div style="text-align:center;padding:8px 0 4px">
  <span class="kick">Batch {BATCH} &middot; the last run of 2026</span>
  <h1 style="margin:16px 0 14px">I spent three years<br>trying to fix<br>one bad night.</h1>
 </div>
 <p class="big">You know the night. You hiked all day, found the flattest ground there was &mdash; which wasn&rsquo;t flat &mdash; and lay down on it. A root found your hip. The cold came up through the floor. At two in the morning you were still turning over, doing the arithmetic on how many hours were left until it got light.</p>
 <p>Everyone who camps has had that night. Most of us decided it was the price of admission.</p>
</div>

{fig("story-camp.jpg",1000,1000,"A Hawk Nest hammock tent pitched between two trees with someone inside and a friend cooking beside it","Batch 3, in the woods. Same thing you would get.","bleed")}

<div class="w">
 <div class="ch">Chapter one &middot; the problem</div>
 <h2 class="r">It was never one bad night.</h2>
 <p>That was the part I kept getting wrong. I treated each terrible night as bad luck &mdash; wrong site, wrong weather, wrong day. Then I started keeping track, and it was most of them. Four nights out, one of them decent. That is a hobby you slowly stop booking.</p>
 <p>What actually happens on the ground is not complicated. You are lying on a cold, hard, uneven surface that pulls heat out of you all night, and there is a limit to how much foam you can put between you and it before you are carrying a mattress up a mountain.</p>
 <div class="pull r">I was not sleeping badly because I was doing it wrong. I was sleeping badly because I was on the ground.</div>
</div>

<div class="w">
 <div class="ch">Chapter two &middot; the failures</div>
 <h2 class="r">Everything I tried first.</h2>
 <p><b>A thicker pad.</b> Three inches of air, and a pack that no longer closed. It helped with the roots. It did nothing about the slope, and I still woke up cold at four.</p>
 <p><b>A better tent.</b> Lighter, more expensive, same floor, same ground under it. I had bought a nicer container for the same problem.</p>
 <p><b>Better sites.</b> An hour of daylight burned every evening hunting for flat, dry, clear ground. In real terrain that spot is often not there, and you pitch on the least bad option and pay for it at 2am.</p>
 <p><b>Sleeping pills, earplugs, a nightcap.</b> All the things people quietly try. They make you unconscious. They do not make you rested.</p>
 <p>Three seasons of this. I remember lying awake on a slope in the rain, water tracking under the groundsheet, thinking the thought a lot of people think and nobody says out loud: <em>maybe I am getting too old to enjoy this.</em></p>
</div>

{inline("Skip to the part where it works.","Batch "+BATCH+" arrives "+SHIP+".")}

<div class="w">
 <div class="ch">Chapter three &middot; the idea</div>
 <h2 class="r">Two trees, and no ground at all.</h2>
 <p>The realisation was almost annoying in how obvious it was. The problem was not my pad, my tent or my technique. It was the insistence on lying on the ground when there were two trees right there.</p>
 <p>So I bought a hammock. And I want to be straight with you, because this is where most people give up on the idea: <b>a plain hammock made it worse.</b></p>
 <p>No bug net, so the first warm night was unusable. No cover, so the first wet night was worse. And below about {TEMP_COLD}, the air moving underneath strips heat off your back faster than the ground ever did, because your sleeping bag is squashed flat beneath you and the insulation in it does nothing at all.</p>
</div>

<div class="w">{fig("story-inside.jpg",1000,1333,"Someone lying inside the hammock tent reading a book","Inside, on a wet afternoon. Net zipped, fly on.")}</div>

<div class="w">
 <div class="ch">Chapter four &middot; the frankenstein</div>
 <h2 class="r">Four separate things, in the dark, in the rain.</h2>
 <p>The hammock people solve this with a kit list: hammock, tarp, bug net, underquilt, plus the cord and stakes to rig it. It works. I did it for two seasons.</p>
 <p>It is also four things to pitch in the dark, four things to pack wet, and four things to forget. The night I put the tarp up backwards and spent twenty minutes in the rain undoing it was the night I decided somebody should just sew the whole thing together.</p>
 <p>Nobody had, in the way I wanted it. So that became the project.</p>
</div>

<div class="w">
 <div class="ch">Chapter five &middot; three years of prototypes</div>
 <h2 class="r">Most of them were bad.</h2>
 <p>The first had the net too close to your face. The second pooled water where the fly met the body. The third was warm and weighed as much as a tent, which defeated the point. Every material choice in the current version came from something failing on an earlier one, usually at an inconvenient hour.</p>
 <p>The version that finally worked did one thing the others did not: it put the sleeping pad <em>inside</em> a pocket under your back, so it cannot slide out from under you at 2am. That is the fix for the cold. Everything else is weatherproofing.</p>
 <div class="detail r">
  <div class="ch">What comes in the box</div>
  <ul>{inbox}</ul>
 </div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-rain.jpg" width="1000" height="1000" alt="Rain beading on the waterproof fly fabric">
 <img loading="lazy" decoding="async" src="story-pack.jpg" width="900" height="1200" alt="The hammock tent being unpacked">
</div></div>

<div class="w">
 <div class="ch">Chapter six &middot; the skepticism</div>
 <h2 class="r">The three things everybody says.</h2>
 <p><b>&ldquo;I&rsquo;ll be cold.&rdquo;</b> You will be, in a bare hammock. With a pad held under your back you are insulated from the moving air, which is the entire mechanism. This is not a claim about fabric, it is where the heat is actually going.</p>
 <p><b>&ldquo;I&rsquo;ll sleep folded like a banana.&rdquo;</b> Only if you lie straight down the middle. You lie diagonally, which flattens it out. It takes one night to learn and then you stop thinking about it.</p>
 <p><b>&ldquo;There won&rsquo;t be trees.&rdquo;</b> Sometimes there won&rsquo;t. Above the treeline this is the wrong shelter and I am not going to pretend otherwise. Below it, two trees are easier to find than flat, dry, rock-free ground.</p>
</div>

<div class="w">
 <div class="ch">Chapter seven &middot; the evidence</div>
 <h2 class="r">Why hanging actually sleeps better.</h2>
 <p>Two things are going on, and one of them is genuinely well studied.</p>
 <p>The first is heat. Lying on the ground you lose warmth by conduction into a very large, very cold object. Off the ground that path is gone, and the remaining problem &mdash; moving air underneath &mdash; is what the pad pocket exists to solve.</p>
 <p>The second is the gentle movement, and there is real research on it.</p>
 <div class="sci r">
  <div class="lb">What the research found</div>
  <p>In a 2019 study published in <em>Current Biology</em>, researchers had healthy adults sleep one night on a still bed and one on an identical bed rocking gently side to side. On the rocking bed they fell into deep sleep about <b>6.5 minutes faster</b>, spent <b>around 5% more of the night</b> in those deeper stages, and scored slightly better on a memory test the next morning.</p>
  <p class="cite">Perrault et al., &ldquo;Whole-Night Continuous Rocking Entrains Spontaneous Neural Oscillations with Benefits for Sleep and Memory,&rdquo; <em>Current Biology</em>, 2019. Worth saying plainly: that was 18 young adults on a motorised bed, not a hammock in a forest. It is evidence that gentle motion helps people sleep deeper, not proof about this product.</p>
 </div>
 <p>Which matches what people report, and what I found after the first hundred nights: you drop off faster, and you stop waking up to turn over, because there is nothing to turn away from.</p>
</div>

{fig("story-winter.jpg",1000,750,"The hammock tent pitched in deep snow with someone inside","A customer&rsquo;s photo. February, and he stayed out in it.","bleed")}

{inline("Batch "+BATCH+" is the last run of 2026.","{UNITS} units, arriving {SHIP}.".format(UNITS=UNITS,SHIP=SHIP))}

<div class="w">
 <div class="ch">Chapter eight &middot; the owners</div>
 <h2 class="r">{SHIPPED} of them are out there now.</h2>
 <p>These are real review titles from verified buyers, their words rather than ours.</p>
 <div class="stat r">
  <div class="sn"><b>{SHIPPED}</b><span>shipped since we started</span></div>
  <div class="sn"><b>3</b><span>runs, all sold out</span></div>
  <div class="sn"><b>30</b><span>days to change your mind</span></div>
 </div>
 <div class="revs r">{revs}</div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-ugc-setup.jpg" width="760" height="1351" alt="A customer setting up their Hawk Nest hammock in a field">
 <img loading="lazy" decoding="async" src="story-open.jpg" width="1000" height="1333" alt="A Hawk Nest hammock tent open with someone inside, mountains behind">
</div>
<p class="fine" style="margin-top:-12px">Left: a customer&rsquo;s own footage, setting one up.</p></div>

<div class="w">
 <div class="ch">Chapter nine &middot; why you have to wait</div>
 <h2 class="r">We build these in runs.</h2>
 <p>We do not hold a warehouse full of stock. We commit to a production run, sell it, and build the next one. Batches 1, 2 and 3 all sold out before they landed. Batch {BATCH} is {UNITS} units and it is the last run of 2026.</p>
 <div class="batch r">{batch}</div>
 <p>That is the honest reason it is a pre-order rather than a buy button, and it is also why the price is what it is. Reserving funds the run. When Batch {BATCH} is gone the price goes to ${AFTER} and the free upgrades end, and there is no restock date after that.</p>
</div>

<div class="w">
 <h2 class="r" style="text-align:center">Everything, one price.</h2>
 <p style="text-align:center">The upgrades people normally add are included while this run lasts.</p>
 <div class="offer r">
  {bundle}
  <div class="tot"><div class="l">Buy it all<br>separately</div><div class="p"><s>${WAS}</s>${PRICE}</div></div>
  <div class="keep">You keep ${KEEP}</div>
  {cta("Reserve yours &mdash; $"+PRICE)}
  <p class="fine">Free shipping &middot; duties included &middot; 30-day refund<br>Ships from South Carolina, arriving {SHIP}</p>
 </div>
</div>

<div class="w">
 <h2 class="r" style="text-align:center;margin-bottom:16px">Straight answers.</h2>
 <div class="r">{faq}</div>
</div>

<div class="w" style="text-align:center;padding-bottom:10px">
 <div class="ch" style="text-align:center">The end of it</div>
 <h2 class="r">Stop sleeping on the ground.</h2>
 <p>I built this because I was tired of lying awake on a slope in the rain working out how many hours were left. If that sentence landed, you already know whether this is for you.</p>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">30 days to change your mind. Full refund, no questions.</p>
 <p style="margin-top:22px;font-style:italic">&mdash; Lukas, Hawk Nest Hammocks</p>
</div>

<footer>Hawk Nest Hammocks &middot; Built in Canada &middot; Shipped from South Carolina, duties included</footer>
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{rootMargin:'0px 0px -6% 0px'}});
document.querySelectorAll('.r').forEach(el=>io.observe(el));
</script>
</body></html>"""
open("b4-story.html","w").write(HTML)
print("b4-story.html",len(HTML)//1024,"KB")
