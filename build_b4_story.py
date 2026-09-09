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
.diag{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;margin:26px 0;box-shadow:var(--s1)}
.diag svg{width:100%;height:auto;display:block}
.dcap{font:14.5px/1.55 "DM Sans",sans-serif;color:var(--soft);text-align:center;margin-top:12px}

.letter{background:linear-gradient(180deg,#FFFFFF,#FCFBF6);border:1px solid var(--line);
 border-radius:18px;padding:24px 22px;margin:26px 0;box-shadow:var(--s2);position:relative}
.letter::before{content:"\201C";position:absolute;top:2px;left:16px;font:600 72px/1 "Crimson Pro",serif;
 color:var(--org);opacity:.24}
.letter .lh{font:700 11px/1 "DM Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;
 color:var(--org2);margin-bottom:14px}
.letter p{font-size:18px;line-height:1.66;color:var(--ink);margin:0 0 14px}
.letter p:last-of-type{margin-bottom:0}
.letter .sig{display:flex;align-items:center;gap:11px;border-top:1px solid var(--line);
 margin-top:18px;padding-top:15px}
.letter .av{width:40px;height:40px;border-radius:50%;flex:none;
 background:linear-gradient(180deg,#2A5340,#1E3A2B);color:#fff;
 font:700 15px/40px "DM Sans",sans-serif;text-align:center}
.letter .who b{display:block;font:600 16px/1.3 "DM Sans",sans-serif;color:var(--ink)}
.letter .who span{font:13.5px/1.4 "DM Sans",sans-serif;color:var(--soft)}
.vb{display:inline-flex;align-items:center;gap:5px;font:700 10.5px/1 "DM Sans",sans-serif;
 letter-spacing:.09em;text-transform:uppercase;color:var(--grn2);background:#E9F5EF;
 border:1px solid #BFE0CF;border-radius:99px;padding:4px 8px 4px 6px;margin-left:auto;flex:none}
.vb svg{width:12px;height:12px}
.said{background:#FFF9F4;border:1px solid #F6D8C4;border-radius:13px;padding:15px 17px;margin:20px 0}
.said .q{font:600 17px/1.55 "Crimson Pro",serif;color:var(--ink);margin:0 0 7px}
.said .a{font:13.5px/1.5 "DM Sans",sans-serif;color:var(--soft);margin:0}
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
CHK=('<svg viewBox="0 0 24 24" fill="none" stroke="#1E7A52" stroke-width="3.2" stroke-linecap="round" '
     'stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5l5.2 5.2L20 7"/></svg>')
def said(q,a):
    return f'<div class="said r"><p class="q">&ldquo;{q}&rdquo;</p><p class="a">{a}</p></div>'
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
letter="".join(f'<p>{k}</p>' for k in KEN)

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>No Level Ground, No Trees, No Problem &mdash; Hawk Nest V.3, Batch {BATCH}</title>
<meta name="description" content="A real customer&rsquo;s account of three weeks in a Hawk Nest hammock tent, and why Batch {BATCH} is the last run of 2026. ${PRICE} with every upgrade included, arriving {SHIP}.">
<link rel="icon" href="favicon-192.png">
{FONTS}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;600;700;800&display=swap">
<style>{CSS}</style></head><body>
<header><img src="hnh-logo-sm.webp" alt="Hawk Nest Hammocks" width="340" height="266" fetchpriority="high"></header>

<div class="w">
 <div style="text-align:center;padding:8px 0 4px">
  <span class="kick">Batch {BATCH} &middot; the last run of 2026</span>
  <h1 style="margin:16px 0 14px">&ldquo;No level ground,<br>no room for a tent,<br>no trees&hellip; no problem.&rdquo;</h1>
  <p class="fine" style="margin-bottom:6px">{KEN_NAME}, after three weeks on the road</p>
 </div>
 <p class="big">You know the night this is about. You hiked all day, found the flattest ground there was &mdash; which wasn&rsquo;t flat &mdash; and lay down on it. A root found your hip. The cold came up through the floor. At two in the morning you were still turning over, doing the arithmetic on how many hours were left until it got light.</p>
 <p>Everyone who sleeps outside has had that night. Most people decide it&rsquo;s the price of admission. This page is about the people who stopped accepting that, and one of them in particular.</p>
</div>

{fig("story-camp.jpg",1000,1000,"A Hawk Nest hammock tent pitched between two trees with someone inside and a friend cooking beside it","Batch 3, in the woods.","bleed")}

<div class="w">
 <div class="ch">Chapter one &middot; the problem</div>
 <h2 class="r">It is never one bad night.</h2>
 <p>That is the part most people get wrong about it. You treat each terrible night as bad luck &mdash; wrong site, wrong weather, wrong day. Then you start counting, and it is most of them. Four nights out, one of them decent. That is a hobby you quietly stop booking.</p>
 <p>What actually happens on the ground is not complicated. You are lying on a cold, hard, uneven surface that pulls heat out of you all night, and there is a limit to how much foam you can carry up a mountain before the cure is worse than the disease.</p>
 <div class="pull r">You are not sleeping badly because you are doing it wrong. You are sleeping badly because you are on the ground.</div>
</div>

<div class="w">
 <div class="ch">Chapter two &middot; what people try first</div>
 <h2 class="r">The things that don&rsquo;t fix it.</h2>
 <p><b>A thicker pad.</b> Three inches of air, and a pack that no longer closes. It helps with the roots. It does nothing about the slope, and you still wake up cold at four.</p>
 <p><b>A better tent.</b> Lighter, more expensive, same floor, same ground underneath it. A nicer container for the same problem.</p>
 <p><b>Better sites.</b> An hour of daylight burned every evening hunting for flat, dry, clear ground. In real terrain that spot is often not there, so you pitch on the least bad option and pay for it at 2am.</p>
 <p><b>Pills, earplugs, a nightcap.</b> The things people quietly try. They make you unconscious. They do not make you rested.</p>
 <p>Somewhere in that list is the evening most people have had: lying awake on a slope in the rain, water tracking under the groundsheet, thinking the thought nobody says out loud &mdash; <em>maybe I am getting too old to enjoy this.</em></p>
</div>

{inline("Skip to the part where it works.","Batch "+BATCH+" arrives "+SHIP+".")}

<div class="w">
 <div class="ch">Chapter three &middot; the obvious idea</div>
 <h2 class="r">Two trees, and no ground at all.</h2>
 <p>The realisation is almost annoying in how obvious it is. The problem was never the pad, the tent or the technique. It was the insistence on lying on the ground when there were two trees standing right there.</p>
 <p>So people buy a hammock. And here is the honest bit, the one most hammock evangelists skip: <b>a plain hammock usually makes it worse.</b></p>
 <p>No bug net, so the first warm night is unusable. No cover, so the first wet night is worse. And below about {TEMP_COLD} the air moving underneath strips heat off your back faster than the ground ever did, because your sleeping bag is squashed flat beneath you and the insulation in it does nothing at all.</p>
 <div class="diag r">{COLD_SVG}<div class="dcap">Off the ground you stop losing heat into it. What is left is the moving air underneath &mdash; which is what the pad pocket exists to stop.</div></div>
</div>

<div class="w">
 <div class="ch">Chapter four &middot; the kit list problem</div>
 <h2 class="r">Four separate things, in the dark, in the rain.</h2>
 <p>The usual answer is to build a system: hammock, tarp, bug net, underquilt, plus the cord and stakes to rig it all. It works. Plenty of people camp that way for years.</p>
 <p>It is also four things to pitch in the dark, four things to pack away wet, and four things to forget. Anyone who has put a tarp up backwards in the rain and spent twenty minutes undoing it knows exactly why somebody eventually sewed the whole thing into one shelter.</p>
</div>

<div class="w">{fig("story-inside.jpg",1000,1333,"Someone lying inside the hammock tent reading a book","Net zipped, fly on, raining outside.")}</div>

<div class="w">
 <div class="ch">Chapter five &middot; a real one</div>
 <h2 class="r">Winnipeg to Vancouver Island, on a motorcycle.</h2>
 <p>This is where we stop generalising. {KEN_NAME} rode from Manitoba to the west coast and back, three weeks, sleeping in a Hawk Nest nearly every night. He wrote to us afterwards. This is his letter, unedited.</p>
 <div class="letter r">
  <div class="lh">Letter from a customer</div>
  {letter}
  <div class="sig"><span class="av">KS</span>
   <span class="who"><b>{KEN_NAME}</b><span>{KEN_TRIP}</span></span>
   <span class="vb">{CHK}Verified</span></div>
 </div>
</div>

{fig("story-winter.jpg",1000,750,"The hammock tent pitched in deep snow with someone inside","A different customer&rsquo;s photo. February.","bleed")}

<div class="w">
 <div class="ch">Chapter six &middot; the objections</div>
 <h2 class="r">The three things everybody says.</h2>

 <p><b>&ldquo;I&rsquo;ll be cold in it.&rdquo;</b> You would be, in a bare hammock. With a pad held in the pocket under your back you are insulated from the moving air, which is the whole mechanism. Ken slept in it down to {TEMP_COLD} on that trip and had nothing to say about the cold at all &mdash; the thing he singled out was the rain.</p>
 {said("Temperatures were between 5&deg;C (40&deg;F) and 22&deg;C (72&deg;F) with 3 nights of rain which was a complete non-issue, absolutely zero leaks or drips in the hammock.","{KEN_NAME}, on three weeks of west coast weather".format(KEN_NAME=KEN_NAME))}

 <p><b>&ldquo;I&rsquo;ll be folded up inside it.&rdquo;</b> This is what the rigid support poles are for. They hold the fly and the net up and off you, so there is genuine interior space and headroom above your face instead of fabric resting on it. Lying at a slight angle rather than straight down the middle helps as well, and takes one night to get used to.</p>

 <p><b>&ldquo;There won&rsquo;t always be trees.&rdquo;</b> Sometimes there won&rsquo;t &mdash; on a beach, above the treeline, or where the trees are too small to take the load. <b>It pitches on the ground as well.</b> You lose the height and most of the clearance, but it still works as a shelter, and that is not a theoretical answer. Three of Ken&rsquo;s nights were exactly that.</p>
 {said("3 nights were spent either on the beach or in areas where trees were too small to support a hammock. Setup on the ground was again, quick and easy. Not much clearance above when pitched on the ground but enough room to read or roll over.","{KEN_NAME}, on the nights with nothing to hang from".format(KEN_NAME=KEN_NAME))}
 <figure class="r" style="margin:18px 0 6px"><img loading="lazy" decoding="async" src="ground-setup.jpg"
  width="900" height="900" alt="The Hawk Nest hammock tent pitched directly on the ground in snow"></figure>

 <p>One more thing worth repeating from his letter, because it is the question everybody actually has: <em>how long does it take to put up?</em></p>
 {said("Set up takes about 5 minutes once you&rsquo;ve done it a few times.","{KEN_NAME}. Your first go will be slower.".format(KEN_NAME=KEN_NAME))}
</div>

{inline("Batch "+BATCH+" is the last run of 2026.",UNITS+" units, arriving "+SHIP+".")}

<div class="w">
 <div class="ch">Chapter seven &middot; the evidence</div>
 <h2 class="r">Why hanging actually sleeps better.</h2>
 <p>Two things are going on, and one of them is genuinely well studied.</p>
 <p>The first is heat, which is the diagram further up. Lying on the ground you lose warmth by conduction into a very large, very cold object. Off the ground that path is gone.</p>
 <p>The second is the gentle movement, and there is real research on it.</p>
 <div class="sci r">
  <div class="lb">What the research found</div>
  <p>In a 2019 study published in <em>Current Biology</em>, researchers had healthy adults sleep one night on a still bed and one on an identical bed rocking gently side to side. On the rocking bed they fell into deep sleep about <b>6.5 minutes faster</b>, spent <b>around 5% more of the night</b> in those deeper stages, and scored slightly better on a memory test the next morning.</p>
  <p class="cite">Perrault et al., &ldquo;Whole-Night Continuous Rocking Entrains Spontaneous Neural Oscillations with Benefits for Sleep and Memory,&rdquo; <em>Current Biology</em>, 2019. Worth saying plainly: that was 18 young adults on a motorised bed, not a hammock in a forest. It is evidence that gentle motion helps people sleep deeper &mdash; not proof about this product.</p>
 </div>
</div>

<div class="w">
 <div class="ch">Chapter eight &middot; what you get</div>
 <h2 class="r">What&rsquo;s actually in the bag.</h2>
 <div class="detail r"><div class="ch">In the box</div><ul>{inbox}</ul></div>
 <div class="stat r">
  <div class="sn"><b>{SHIPPED}</b><span>shipped since we started</span></div>
  <div class="sn"><b>3</b><span>runs, all sold out</span></div>
  <div class="sn"><b>30</b><span>days to change your mind</span></div>
 </div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-rain.jpg" width="1000" height="1000" alt="Rain beading on the waterproof fly fabric">
 <img loading="lazy" decoding="async" src="story-pack.jpg" width="900" height="1200" alt="The hammock tent being unpacked">
</div></div>

<div class="w">
 <div class="ch">Chapter nine &middot; the others</div>
 <h2 class="r">Ken is not the only one.</h2>
 <p>Real review titles from verified buyers, newest first.</p>
 <div class="revs r">{revs}</div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-ugc-setup.jpg" width="760" height="1351" alt="A customer setting up their Hawk Nest hammock in a field">
 <img loading="lazy" decoding="async" src="story-open.jpg" width="1000" height="1333" alt="A Hawk Nest hammock tent open with someone inside, mountains behind">
</div>
<p class="fine" style="margin-top:-12px">Left: a customer&rsquo;s own footage, setting one up.</p></div>

<div class="w">
 <div class="ch">Chapter ten &middot; why you have to wait</div>
 <h2 class="r">These are built in runs.</h2>
 <p>There is no warehouse full of stock. A production run gets committed, sold, and then the next one gets built. Batches 1, 2 and 3 all sold out before they landed. Batch {BATCH} is {UNITS} units and it is the last run of 2026.</p>
 <div class="batch r">{batch}</div>
 <p>That is the honest reason it is a pre-order rather than a buy button. Reserving funds the run. When Batch {BATCH} is gone the price goes to ${AFTER} and the free upgrades end, and there is no restock date after that.</p>
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
 <p>Ken put it better than any of our copy ever has: no level ground, no room for a tent, no trees, no problem. If that sounds like the trip you have been putting up with, Batch {BATCH} is the one you can still get on.</p>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">30 days to change your mind. Full refund, no questions.</p>
</div>

<footer>Hawk Nest Hammocks &middot; Built in Canada &middot; Shipped from South Carolina, duties included</footer>
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{rootMargin:'0px 0px -6% 0px'}});
document.querySelectorAll('.r').forEach(el=>io.observe(el));
</script>
</body></html>"""
open("b4-story.html","w").write(HTML)
print("b4-story.html",len(HTML)//1024,"KB")
