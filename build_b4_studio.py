exec(open("_b4.py").read())

BONUS=[("bonus-1.jpg","Waterproof &amp; Windproof Fabric","39"),
 ("bonus-2.jpg","Waterproof Carrying Bag","19"),
 ("bonus-3.jpg","Lifetime Warranty","59"),
 ("bonus-4.jpg","1 Year Gridless Premium","79"),
 ("bonus-5.jpg","Free U.S. Shipping","&mdash;"),
 ("bonus-6.jpg","Hassle-Free Returns","4.99")]
# callout positions are read off product-v3-main.jpg (fly on top, body centre, kit along the base)
CALL=[(50,13,"1"),(50,41,"2"),(14,79,"3"),(26,79,"4"),(43,77,"5"),(62,77,"6"),(81,85,"7")]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0F1B2A;--mut:#55657A;--soft:#8695A6;--line:#E4E9EF;--bg:#FBFCFD;
 --nav:#153761;--nav2:#0C2340;--org:#F0733A;--org2:#D9541C;--grn:#1E7A52;
 --s1:0 1px 2px rgba(15,27,42,.06),0 6px 16px rgba(15,27,42,.06);
 --s2:0 2px 4px rgba(15,27,42,.05),0 14px 34px rgba(15,27,42,.10);
 --s3:0 4px 8px rgba(15,27,42,.06),0 28px 60px rgba(15,27,42,.14)}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font:400 17px/1.62 "DM Sans",system-ui,sans-serif;
 -webkit-font-smoothing:antialiased}
.w{max-width:780px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:600;letter-spacing:-.015em;line-height:1.1}
h1{font-size:clamp(33px,7.2vw,52px)}
h2{font-size:clamp(25px,5vw,35px);margin-bottom:10px}
h3{font-size:19px}
p{color:var(--mut)}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font:700 12px/1 "DM Sans",sans-serif;
 letter-spacing:.16em;text-transform:uppercase;color:var(--org2);
 background:linear-gradient(180deg,#FFF3EC,#FFE7DA);border:1px solid #FBD3BE;border-radius:99px;
 padding:9px 15px;box-shadow:var(--s1)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--org);box-shadow:0 0 0 3px rgba(240,115,58,.22)}
header{padding:20px 0 4px;text-align:center}
header img{height:42px;width:auto}
.hero{text-align:center;padding:12px 0 4px}
.hero p.sub{font-size:19px;margin:15px auto 0;max-width:34em}
.shot{margin:20px 0 4px;border-radius:20px;overflow:hidden;box-shadow:var(--s3);position:relative}
.shot img{width:100%;height:auto;display:block}
.cta{display:block;text-align:center;text-decoration:none;color:#fff;font:700 18px/1 "DM Sans",sans-serif;
 padding:19px 20px;border-radius:14px;background:linear-gradient(180deg,var(--org),var(--org2));
 box-shadow:0 1px 0 rgba(255,255,255,.4) inset,0 10px 24px rgba(217,84,28,.32),var(--s2);
 transition:transform .16s,box-shadow .16s;margin-top:18px}
.cta:hover{transform:translateY(-1px)}.cta:active{transform:translateY(1px)}
.fine{font-size:14px;color:var(--soft);text-align:center;margin-top:11px;line-height:1.55}
.trust{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:18px}
.trust span{font:600 13px/1 "DM Sans",sans-serif;color:var(--mut);background:#fff;border:1px solid var(--line);
 border-radius:99px;padding:9px 13px;box-shadow:var(--s1)}
section{padding:44px 0}
.lead{max-width:36em;margin:0 auto 24px;text-align:center}
/* anatomy */
.anat{position:relative;background:#fff;border:1px solid var(--line);border-radius:20px;
 padding:10px;box-shadow:var(--s2)}
.anat img{width:100%;height:auto;display:block;border-radius:13px}
.pin{position:absolute;width:27px;height:27px;border-radius:50%;transform:translate(-50%,-50%);
 background:linear-gradient(180deg,var(--org),var(--org2));color:#fff;
 font:800 13px/27px "DM Sans",sans-serif;text-align:center;
 box-shadow:0 0 0 3px rgba(255,255,255,.9),0 4px 10px rgba(15,27,42,.3)}
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(238px,1fr));gap:9px;margin-top:14px}
.lg{display:flex;gap:11px;background:#fff;border:1px solid var(--line);border-radius:12px;
 padding:12px 13px;box-shadow:var(--s1)}
.lg b{flex:none;width:23px;height:23px;border-radius:50%;background:#EEF3F9;color:var(--nav);
 font:800 12px/23px "DM Sans",sans-serif;text-align:center}
.lg .t{font-weight:600;font-size:15.5px}
.lg .d{font-size:13.5px;color:var(--soft);line-height:1.45}
/* diagram: where cold comes from */
.diag{background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px;box-shadow:var(--s2)}
.diag svg{width:100%;height:auto;display:block}
.dcap{font-size:14.5px;color:var(--soft);text-align:center;margin-top:12px}
/* pack size to scale */
.scale{display:flex;align-items:flex-end;justify-content:center;gap:26px;padding:8px 0 2px}
.scale figure{text-align:center;margin:0}
.scale .bar{background:linear-gradient(180deg,#20406B,#0E2440);border-radius:8px;
 box-shadow:var(--s2);position:relative}
.scale .btl{background:linear-gradient(180deg,#CFE0EF,#A9C3DC);border-radius:7px 7px 10px 10px;position:relative}
.scale .btl::before{content:"";position:absolute;left:50%;top:-16px;transform:translateX(-50%);
 width:16px;height:16px;background:#8FAEC9;border-radius:3px 3px 0 0}
.scale figcaption{font:600 13px/1.4 "DM Sans",sans-serif;color:var(--mut);margin-top:10px}
.scale figcaption b{display:block;color:var(--ink);font-size:15px}
/* steps */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:11px}
.st{background:#fff;border:1px solid var(--line);border-radius:15px;padding:17px 16px;box-shadow:var(--s1)}
.st .n{width:28px;height:28px;border-radius:9px;background:linear-gradient(180deg,#F2F6FB,#E2EBF5);
 border:1px solid #D8E3F0;color:var(--nav);font:800 13px/26px "DM Sans",sans-serif;text-align:center;
 margin-bottom:10px}
.st b{display:block;font-size:15.5px;margin-bottom:3px}
.st span{font-size:14px;color:var(--soft);line-height:1.5}
/* feature cards with photos */
.feats{display:grid;grid-template-columns:repeat(auto-fit,minmax(238px,1fr));gap:14px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;box-shadow:var(--s1);
 transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-2px);box-shadow:var(--s2)}
.card .ph{display:block;aspect-ratio:4/3;overflow:hidden}
.card .ph img{width:100%;height:100%;object-fit:cover;display:block}
.card .bd{padding:16px 17px 18px}
.card h3{margin-bottom:5px}
.card p{font-size:15px}
/* timeline */
.tl{position:relative;padding:6px 0 0}
.tl .track{position:absolute;left:22px;right:22px;top:32px;height:4px;border-radius:3px;
 background:linear-gradient(90deg,var(--grn) 0%,var(--grn) 72%,var(--org) 72%,#E4E9EF 72%,#E4E9EF 100%)}
.tl .row{display:grid;grid-template-columns:repeat(4,1fr);position:relative}
.tl .c{text-align:center;padding-top:0}
.tl .k{width:20px;height:20px;border-radius:50%;margin:22px auto 12px;background:var(--grn);
 box-shadow:0 0 0 4px #fff,0 0 0 6px rgba(30,122,82,.22)}
.tl .c.now .k{background:var(--org);box-shadow:0 0 0 4px #fff,0 0 0 6px rgba(240,115,58,.28)}
.tl .c.now .b{color:var(--org2)}
.tl .a{font:800 11px/1 "DM Sans",sans-serif;letter-spacing:.11em;text-transform:uppercase;color:var(--soft)}
.tl .b{font:700 13.5px/1.3 "DM Sans",sans-serif;margin-top:6px;color:var(--grn)}
.tl .u{font:13px/1.3 "DM Sans",sans-serif;color:var(--soft);margin-top:4px}
/* bonuses with photos */
.bon{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.bx{background:#fff;border:1px solid var(--line);border-radius:15px;overflow:hidden;box-shadow:var(--s1);
 position:relative}
.bx img{width:100%;aspect-ratio:1;object-fit:cover;display:block}
.bx .tag{position:absolute;top:8px;right:8px;font:800 10px/1 "DM Sans",sans-serif;letter-spacing:.1em;
 color:#fff;background:var(--grn);border-radius:6px;padding:5px 7px;box-shadow:0 2px 6px rgba(30,122,82,.35)}
.bx .bd{padding:11px 12px 13px}
.bx .t{font:600 14px/1.32 "DM Sans",sans-serif}
.bx .v{font:13px/1 "DM Sans",sans-serif;color:var(--soft);margin-top:5px}
.bx .v s{margin-right:5px}
/* bundle */
.bundle{background:linear-gradient(180deg,#FFFFFF,#F7FAFD);border:1px solid var(--line);border-radius:22px;
 padding:26px 22px;box-shadow:var(--s3)}
.bi{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:11px 0;
 border-bottom:1px solid var(--line);font-size:15.5px}
.bn{display:flex;align-items:center;gap:11px;min-width:0}
.bn img{width:42px;height:42px;flex:none;border-radius:9px;object-fit:cover;background:#fff;
 border:1px solid var(--line);box-shadow:var(--s1)}
.bv{flex:none;white-space:nowrap}
.bi:last-of-type{border-bottom:0}
.bi s{color:var(--soft);font-size:14px}
.tag2{font:800 11px/1 "DM Sans",sans-serif;letter-spacing:.1em;color:#fff;background:var(--grn);
 border-radius:6px;padding:5px 8px;box-shadow:0 2px 6px rgba(30,122,82,.3)}
.tot{display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid var(--ink);
 margin-top:14px;padding-top:16px}
.tot .l{font:600 15px/1.3 "DM Sans",sans-serif;color:var(--mut)}
.tot .p{font-family:Fraunces,serif;font-size:44px;font-weight:600;line-height:1}
.tot .p s{font-size:20px;color:var(--soft);margin-right:8px;font-family:"DM Sans",sans-serif}
.keep{text-align:center;margin:14px 0 4px;font:700 15px/1 "DM Sans",sans-serif;color:var(--grn)}
/* specs + reviews + faq */
.specs{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:10px}
.sp{background:#fff;border:1px solid var(--line);border-radius:13px;padding:14px 15px;box-shadow:var(--s1)}
.sp .k{font:700 11px/1 "DM Sans",sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
.sp .v{margin-top:7px;font-weight:500}
.revs{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:10px}
.rv{padding:4px 2px 14px;border-bottom:1px solid var(--line)}
.rv .hd{display:flex;align-items:center;gap:9px;margin-bottom:6px}
.rv .st{color:#D9A21B;font-size:14.5px;letter-spacing:.09em;line-height:1}
.rv .vb{display:inline-flex;align-items:center;gap:5px;font:700 10.5px/1 "DM Sans",sans-serif;
 letter-spacing:.09em;text-transform:uppercase;color:var(--grn);background:#E9F6EF;
 border:1px solid #BFE3D2;border-radius:99px;padding:4px 8px 4px 6px}
.rv .vb svg{width:12px;height:12px;flex:none}
.rv .ti{font-weight:600;font-size:16px;line-height:1.35;color:var(--ink)}
.rv .by{font-size:13.5px;color:var(--soft);margin-top:3px}
details{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:9px;box-shadow:var(--s1);
 overflow:hidden}
summary{cursor:pointer;padding:16px 18px;font-weight:700;list-style:none;display:flex;
 justify-content:space-between;gap:12px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--org2);font-size:22px;line-height:1;font-weight:400}
details[open] summary::after{content:"\\2013"}
details p{padding:0 18px 17px;font-size:15.5px}
footer{padding:32px 0 54px;text-align:center;color:var(--soft);font-size:14px}
.r{opacity:0;transform:translateY(16px)}
.r.in{opacity:1;transform:none;transition:opacity .6s cubic-bezier(.2,.7,.3,1),transform .6s cubic-bezier(.2,.7,.3,1)}
@media (prefers-reduced-motion:reduce){.r,.r.in{opacity:1;transform:none;transition:none}}
"""

COLD = COLD_SVG

pins="".join(f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>' for x,y,n in CALL)
legend="".join(f'<div class="lg"><b>{i+1}</b><div><div class="t">{t}</div><div class="d">{d}</div></div></div>'
 for i,(t,d) in enumerate(INBOX))
steps="".join(f'<div class="st"><div class="n">{i+1}</div><b>{a}</b><span>{b}</span></div>'
 for i,(a,b) in enumerate([("Two straps","Round each tree, no knots."),
  ("Clip and spread","Body hooks on, poles push the net up."),
  ("Fly over the top","Guy it out with the two stakes."),
  ("Pad in the pocket","Slide it under your back and get in.")]))
FEATS=[("story-rain.jpg","Rain runs off, not through","A full-coverage fly over the top and a waterproof floor beneath. Both, not one or the other."),
 ("story-inside.jpg","Room to sit up in","The rigid support poles hold the fly and net up and off you, which is what gives it the interior space and headroom a bare hammock has none of."),
 ("story-winter.jpg","Built for the cold end","Three years of prototypes tested through Canadian winters, down to "+TEMP_TESTED+".")]
DIMS={'story-rain.jpg': (1000, 1000), 'story-inside.jpg': (1000, 1333), 'story-winter.jpg': (1000, 750)}
feats="".join(f'<div class="card r"><span class="ph"><img loading="lazy" src="{s}" '
 f'width="{DIMS[s][0]}" height="{DIMS[s][1]}" alt="{t}"></span>'
 f'<div class="bd"><h3>{t}</h3><p>{d}</p></div></div>' for s,t,d in FEATS)
TL=[("Batch 1","Sold out","1,000 units"),("Batch 2","Sold out","1,000 units"),
    ("Batch 3","Sold out","1,500 units"),("Batch 4","Open now",UNITS+" units &middot; "+SHIP)]
tl="".join(f'<div class="c{" now" if i==3 else ""}"><div class="a">{a}</div><div class="k"></div>'
 f'<div class="b">{b}</div><div class="u">{u}</div></div>' for i,(a,b,u) in enumerate(TL))
bon="".join(f'<div class="bx r"><img loading="lazy" src="{s}" width="420" height="420" alt="{t}">'
 f'<span class="tag">FREE</span><div class="bd"><div class="t">{t}</div>'
 f'<div class="v">{"" if v=="&mdash;" else "<s>$"+v+"</s>"}included</div></div></div>' for s,t,v in BONUS)
bundle="".join(
 f'<div class="bi"><span class="bn"><img loading="lazy" src="{BUNDLE_IMG[i]}" width="160" height="160" alt="">'
 f'<span>{n}</span></span><span class="bv">'
 f'{"<s>$"+v+"</s> <span class=tag2>FREE</span>" if free else "$"+v}</span></div>'
 for i,(n,v,free) in enumerate(BUNDLE))
specs="".join(f'<div class="sp"><div class="k">{k}</div><div class="v">{v}</div></div>' for k,v in SPECS)
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="#1E7A52" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5l5.2 5.2L20 7"/></svg>'
revs="".join(f'<div class="rv"><div class="hd"><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
 f'<span class="vb">{CHECK}Verified</span></div>'
 f'<div class="ti">{t}</div><div class="by">{n}</div></div>' for t,n in REVIEWS[:6])
faq="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hawk Nest V.3 &mdash; Batch {BATCH} Pre-Order, ${PRICE}</title>
<meta name="description" content="Batch {BATCH} is the last run of 2026 &mdash; {UNITS} units, arriving {SHIP}. ${PRICE} with every upgrade included. Ships from South Carolina, duties paid.">
<link rel="icon" href="favicon-192.png">
{FONTS}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=DM+Sans:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style></head><body>
<header><img src="hnh-logo-sm.webp" alt="Hawk Nest Hammocks" width="340" height="266" fetchpriority="high"></header>

<div class="w"><div class="hero">
 <span class="eyebrow"><span class="dot"></span>Batch {BATCH} &middot; the last run of 2026</span>
 <h1 style="margin-top:15px">A tent that hangs,<br>so the ground stops<br>mattering.</h1>
 <p class="sub">Rain fly, bug net, waterproof floor and a sleeping-pad pocket, in one shelter you sling between two trees.</p>
 <div class="shot"><img src="story-camp.jpg" width="1000" height="1000" fetchpriority="high"
  alt="A Hawk Nest hammock tent pitched between two trees with someone inside"></div>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">Free shipping &middot; duties included &middot; 30-day refund<br>{UNITS} units, arriving {SHIP}</p>
 <div class="trust"><span>{SHIPPED} shipped</span><span>Lifetime warranty</span><span>Ships from South Carolina</span></div>
</div></div>

<section><div class="w">
 <div class="lead r"><h2>Everything in the box.</h2>
  <p>One order. Nothing else to buy before your first night out.</p></div>
 <div class="anat r"><img loading="lazy" src="product-v3-main.jpg" width="820" height="820"
   alt="The Hawk Nest V.3 laid out: rain fly, hammock body with bug net, stuff sack, stakes, straps, guy lines and spreader poles">{pins}</div>
 <div class="legend r">{legend}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Where the cold actually comes from.</h2>
  <p>Rain is the easy part. Below {TEMP_COLD} it&rsquo;s the moving air underneath that ruins the night, because your sleeping bag is squashed flat beneath you and does nothing.</p></div>
 <div class="diag r">{COLD}<div class="dcap">The pad pocket holds your pad under your back, where the heat is being lost.</div></div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Up in about five minutes.</h2></div>
 <div class="steps r">{steps}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>It packs down to this.</h2></div>
 <div class="diag r"><div class="scale">
  <figure><div class="bar" style="width:74px;height:148px"></div>
   <figcaption><b>The Hawk Nest</b>5.5 &times; 5.5 &times; 16 in<br>about 4 lbs</figcaption></figure>
  <figure><div class="btl" style="width:52px;height:112px"></div>
   <figcaption><b>A 1-liter bottle</b>for scale<br>&nbsp;</figcaption></figure>
 </div><div class="dcap">Drawn to scale. It rides inside a pack, not strapped to the outside.</div></div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>What it does that a hammock doesn&rsquo;t.</h2></div>
 <div class="feats">{feats}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Three runs, three sell-outs.</h2>
  <p>We build in limited batches and don&rsquo;t overbuild. Batch {BATCH} is the last of the year.</p></div>
 <div class="diag r"><div class="tl"><div class="track"></div><div class="row">{tl}</div></div></div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Everything, one price.</h2></div>
 <div class="bundle r">
  {bundle}
  <div class="tot"><div class="l">Buy it all<br>separately</div><div class="p"><s>${WAS}</s>${PRICE}</div></div>
  <div class="keep">You keep ${KEEP}</div>
  {cta("Reserve yours &mdash; $"+PRICE)}
  <p class="fine">After Batch {BATCH} the price goes to ${AFTER} and the upgrades end.</p>
 </div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>The numbers.</h2></div>
 <div class="specs r">{specs}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>{SHIPPED} shipped.</h2><p>Real review titles from verified buyers.</p></div>
 <div class="revs r">{revs}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Straight answers.</h2></div>
 <div class="r">{faq}</div>
</div></section>

<section><div class="w r" style="text-align:center">
 <h2>Batch {BATCH} arrives {SHIP}.</h2>
 <p>Reserved in the order they come in.</p>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">30 days to change your mind. Full refund, no questions.</p>
</div></section>

<footer>Hawk Nest Hammocks &middot; Built in Canada &middot; Shipped from South Carolina</footer>
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{rootMargin:'0px 0px -7% 0px'}});
document.querySelectorAll('.r').forEach((el,i)=>{{el.style.transitionDelay=(i%4*55)+'ms';io.observe(el)}});
</script>
</body></html>"""
open("b4-studio.html","w").write(HTML)
print("b4-studio.html",len(HTML)//1024,"KB")
