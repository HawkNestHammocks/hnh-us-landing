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
.r{opacity:0;transform:translateY(15px)}
.r.in{opacity:1;transform:none;transition:opacity .65s cubic-bezier(.2,.7,.3,1),transform .65s cubic-bezier(.2,.7,.3,1)}
@media (prefers-reduced-motion:reduce){.r,.r.in{opacity:1;transform:none;transition:none}}
"""
def fig(src,w,h,alt,cap,cls=""):
    return (f'<figure class="r {cls}"><img loading="lazy" decoding="async" src="{src}" width="{w}" '
            f'height="{h}" alt="{alt}"><figcaption>{cap}</figcaption></figure>')
revs="".join(f'<div class="rv"><div class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
 f'<div class="ti">{t}</div><div class="by"><b>{n}</b> &middot; Verified buyer</div></div>'
 for t,n in REVIEWS)
bundle="".join(f'<div class="bi"><span>{n}</span><span>'
 f'{"<s>$"+v+"</s> <span class=tag>FREE</span>" if free else "$"+v}</span></div>'
 for n,v,free in BUNDLE)
batch="".join(f'<div class="bc{" now" if i==3 else ""}"><div class="a">Batch {i+1}</div>'
 f'<div class="b">{"Open now" if i==3 else "Sold out"}</div></div>' for i in range(4))
faq="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)

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
 <p class="big">You know the night. You hiked all day, found the flattest ground there was &mdash; which wasn&rsquo;t flat &mdash; and lay down on it. A root found your hip. The cold came up through the floor. At two in the morning you were still turning over, doing the arithmetic on how many hours were left.</p>
 <p>Everyone who camps has had that night. Most of us decided it was the price of admission.</p>
</div>

{fig("story-camp.jpg",1000,667,"A Hawk Nest hammock tent pitched between two trees at a forest camp","Batch 3, in the Rockies.","bleed")}

<div class="w">
 <div class="ch">Chapter one</div>
 <h2 class="r">The ground was never the problem.</h2>
 <p>The problem was insisting on sleeping on it. Two trees will hold you off it entirely &mdash; no rocks, no roots, no puddle forming under your shoulder at 3am.</p>
 <p>So I tried a hammock. And a hammock, on its own, is worse.</p>
 <div class="pull r">No bug net. No cover when it rains. And below {TEMP_COLD}, the air moving underneath turns it into a wind tunnel. It&rsquo;s a nap, not a night&rsquo;s sleep.</div>
 <p>Which is how you end up carrying a hammock <em>and</em> a tarp <em>and</em> a net <em>and</em> an underquilt, and pitching four separate things in the dark.</p>
</div>

<div class="w">{fig("story-inside.jpg",1000,1333,"Someone lying inside the hammock tent reading a book","Inside, on a rainy afternoon. Net zipped, fly on.")}</div>

<div class="w">
 <div class="ch">Chapter two</div>
 <h2 class="r">So we sewed them together.</h2>
 <p>One shelter. The net is part of it. The rain fly goes over the top. The floor underneath is waterproof, and there&rsquo;s a pocket in it that takes a sleeping pad up to 25 inches wide &mdash; which is the actual fix for the cold, because it puts insulation between you and the moving air.</p>
 <div class="detail r">
  <div class="ch">The numbers</div>
  <ul><li>About 4 lbs on the trail</li><li>Packs to 5.5 x 5.5 x 16 in</li>
   <li>Holds 500 lb</li><li>Pad pocket fits up to 25 in wide</li>
   <li>Up in about four minutes, two trees, no poles or stakes</li><li>Navy, this run only</li></ul>
 </div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-rain.jpg" width="1000" height="1000" alt="Rain beading on the waterproof fly fabric">
 <img loading="lazy" decoding="async" src="story-open.jpg" width="1000" height="1333" alt="The hammock tent open with someone inside">
</div></div>

<div class="w">
 <div class="ch">Chapter three</div>
 <h2 class="r">Three years of getting it wrong first.</h2>
 <p>Prototypes were built and slept in through Canadian winters &mdash; the kind that hit {TEMP_TESTED} &mdash; and through summer storms that arrive without warning. Every material choice in the current version came from something failing on an earlier one.</p>
</div>

{fig("story-winter.jpg",1000,750,"The hammock tent pitched in deep snow with someone inside","A customer's photo. February, and he stayed in it.","bleed")}

<div class="w">
 <div class="ch">Chapter four</div>
 <h2 class="r">{SHIPPED} people have one now.</h2>
 <p>These are their words, not ours &mdash; real titles from verified buyers.</p>
 <div class="revs r">{revs}</div>
</div>

<div class="w"><div class="two r">
 <img loading="lazy" decoding="async" src="story-ugc-setup.jpg" width="760" height="1351" alt="A customer setting up their Hawk Nest hammock in a field">
 <img loading="lazy" decoding="async" src="story-ugc-net.jpg" width="760" height="1351" alt="Inside the bug net of a customer's Hawk Nest hammock">
</div>
<p class="fine" style="margin-top:-12px">Customer footage. Setup, start to finish.</p></div>

<div class="w">
 <div class="ch">Chapter five</div>
 <h2 class="r">Why you have to wait for one.</h2>
 <p>We build in limited runs and don&rsquo;t overbuild. Batches 1, 2 and 3 all sold out before they landed. Batch {BATCH} is {UNITS} units and it is the last run of 2026.</p>
 <div class="batch r">{batch}</div>
 <p>Reserving is the only way to guarantee one. After this run the price goes to ${AFTER} and the free upgrades end.</p>
</div>

<div class="w">
 <h2 class="r" style="text-align:center">Everything, one price.</h2>
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
 <h2 class="r">Stop sleeping on the ground.</h2>
 <p>Batch {BATCH} arrives {SHIP}, in the order it was reserved.</p>
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
