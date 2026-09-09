exec(open("_b4.py").read())

HAMMOCK = '''<svg viewBox="0 0 520 300" fill="none" aria-hidden="true">
<defs>
 <linearGradient id="fly" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2E5C8A"/><stop offset="1" stop-color="#173B5E"/></linearGradient>
 <linearGradient id="bod" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#20406B"/><stop offset="1" stop-color="#0E2440"/></linearGradient>
 <linearGradient id="gl" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#F58A45" stop-opacity=".0"/>
  <stop offset=".5" stop-color="#F58A45" stop-opacity=".5"/>
  <stop offset="1" stop-color="#F58A45" stop-opacity="0"/></linearGradient>
 <filter id="sh" x="-25%" y="-25%" width="150%" height="160%">
  <feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#0E2440" flood-opacity=".2"/></filter>
</defs>
<path d="M40 44 C40 44 62 150 58 262" stroke="#C9CFD6" stroke-width="7" stroke-linecap="round"/>
<path d="M480 44 C480 44 458 150 462 262" stroke="#C9CFD6" stroke-width="7" stroke-linecap="round"/>
<path d="M52 96 C150 74 370 74 468 96" stroke="#9AA6B2" stroke-width="3" stroke-linecap="round"/>
<g filter="url(#sh)">
 <path d="M60 112 C170 96 350 96 460 112 L436 150 C350 132 170 132 84 150 Z" fill="url(#fly)"/>
 <path d="M84 150 C170 132 350 132 436 150 C424 214 372 246 260 246 C148 246 96 214 84 150 Z" fill="url(#bod)"/>
 <path d="M104 168 C180 154 340 154 416 168 C408 206 360 230 260 230 C160 230 112 206 104 168 Z"
  fill="#0B1D33" opacity=".55"/>
 <ellipse cx="260" cy="196" rx="88" ry="26" fill="url(#gl)"/>
</g>
<path d="M60 112 C170 96 350 96 460 112" stroke="#5C87B5" stroke-width="2.4" opacity=".8"/>
<circle cx="260" cy="120" r="7" fill="#F58A45"/>
</svg>'''

def ICON(p): return ('<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.1" '
 'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>')
I_RAIN=ICON('<path d="M10 20a8 8 0 0 1 15.3-3.2A6 6 0 1 1 28 28H12a6 6 0 0 1-2-8z"/>'
 '<path d="M15 33l1.6-3M21 34l1.6-3M27 33l1.6-3"/>')
I_NET =ICON('<path d="M8 12h24v18a4 4 0 0 1-4 4H12a4 4 0 0 1-4-4z"/><path d="M8 20h24M8 27h24M15 12v22M25 12v22"/>')
I_PAD =ICON('<path d="M7 22c0-4 3-6 7-6h12c4 0 7 2 7 6v4c0 3-2 5-5 5H12c-3 0-5-2-5-5z"/>'
 '<path d="M12 16V12a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v4"/>')
I_CLOCK=ICON('<circle cx="20" cy="21" r="12"/><path d="M20 14v7l5 3M14 6h12"/>')
I_SHIELD=ICON('<path d="M20 6l12 4v10c0 8-6 12-12 14-6-2-12-6-12-14V10z"/><path d="M14 20l4 4 8-8"/>')
I_TRUCK=ICON('<path d="M4 12h18v14H4z"/><path d="M22 17h7l5 5v4h-12z"/><circle cx="11" cy="29" r="3"/><circle cx="28" cy="29" r="3"/>')

FEATS=[(I_RAIN,"A fly, not a tarp","Sewn rain cover over the top and a waterproof floor beneath. Rain runs off both sides instead of pooling on you."),
 (I_NET,"Bug net built in","Zipped netting is part of the shelter, not an accessory you clip on and lose."),
 (I_PAD,"A pocket for your pad","Takes a sleeping pad up to 25 in wide, held under your back where cold air gets in."),
 (I_CLOCK,"Four minutes, two trees","No poles, no stakes, no hunting for flat ground that doesn&rsquo;t exist."),
 (I_SHIELD,"Rated to &minus;22&deg;F","Three years of prototypes tested through Canadian winters before it shipped."),
 (I_TRUCK,"Ships from South Carolina","Duties included. No customs bill waiting on your doorstep.")]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0F1B2A;--mut:#5A6A7D;--soft:#8695A6;--line:#E4E9EF;--bg:#FBFCFD;
 --nav:#153761;--nav2:#0C2340;--org:#F0733A;--org2:#D9541C;--grn:#1E7A52;
 --sh1:0 1px 2px rgba(15,27,42,.06),0 6px 16px rgba(15,27,42,.06);
 --sh2:0 2px 4px rgba(15,27,42,.05),0 14px 34px rgba(15,27,42,.10);
 --sh3:0 4px 8px rgba(15,27,42,.06),0 28px 60px rgba(15,27,42,.14)}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font:400 17px/1.62 "DM Sans",system-ui,-apple-system,sans-serif;
 -webkit-font-smoothing:antialiased}
.w{max-width:760px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:600;letter-spacing:-.015em;line-height:1.1}
h1{font-size:clamp(34px,7.6vw,54px)}
h2{font-size:clamp(26px,5.2vw,36px);margin-bottom:10px}
h3{font-size:20px}
p{color:var(--mut)}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font:700 12px/1 "DM Sans",sans-serif;
 letter-spacing:.16em;text-transform:uppercase;color:var(--org2);
 background:linear-gradient(180deg,#FFF3EC,#FFE7DA);border:1px solid #FBD3BE;
 border-radius:99px;padding:9px 15px;box-shadow:var(--sh1)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--org);box-shadow:0 0 0 3px rgba(240,115,58,.22)}
header{padding:22px 0 6px;text-align:center}
header img{height:44px;width:auto}
.hero{text-align:center;padding:14px 0 8px}
.hero p.sub{font-size:19px;margin:16px auto 0;max-width:34em}
.art{margin:6px auto 4px;max-width:520px}
.art svg{width:100%;height:auto;display:block}
/* buttons */
.cta{display:block;text-align:center;text-decoration:none;color:#fff;font:700 18px/1 "DM Sans",sans-serif;
 letter-spacing:.005em;padding:19px 20px;border-radius:14px;
 background:linear-gradient(180deg,var(--org) 0%,var(--org2) 100%);
 box-shadow:0 1px 0 rgba(255,255,255,.4) inset,0 10px 24px rgba(217,84,28,.32),var(--sh2);
 transition:transform .16s ease,box-shadow .16s ease}
.cta:hover{transform:translateY(-1px);box-shadow:0 1px 0 rgba(255,255,255,.4) inset,0 14px 30px rgba(217,84,28,.38),var(--sh2)}
.cta:active{transform:translateY(1px)}
.fine{font-size:14px;color:var(--soft);text-align:center;margin-top:11px;line-height:1.55}
/* trust strip */
.trust{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:20px}
.trust span{font:600 13px/1 "DM Sans",sans-serif;color:var(--mut);background:#fff;
 border:1px solid var(--line);border-radius:99px;padding:9px 13px;box-shadow:var(--sh1)}
section{padding:46px 0}
.lead{max-width:36em;margin:0 auto 26px;text-align:center}
/* batch */
.batch{display:grid;grid-template-columns:repeat(4,1fr);gap:9px}
.bc{border-radius:13px;padding:14px 6px;text-align:center;background:#fff;border:1px solid var(--line);
 box-shadow:var(--sh1)}
.bc .n{font:700 12px/1 "DM Sans",sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--soft)}
.bc .s{font:700 13px/1 "DM Sans",sans-serif;margin-top:8px;color:var(--soft)}
.bc.now{background:linear-gradient(180deg,#FFF6F1,#FFE9DC);border-color:#F7C4A8;box-shadow:var(--sh2)}
.bc.now .n{color:var(--org2)}.bc.now .s{color:var(--org2)}
/* features */
.feats{display:grid;grid-template-columns:repeat(auto-fit,minmax(232px,1fr));gap:14px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 20px;box-shadow:var(--sh1);
 transition:transform .2s ease,box-shadow .2s ease}
.card:hover{transform:translateY(-2px);box-shadow:var(--sh2)}
.card .ic{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;color:var(--nav);
 background:linear-gradient(180deg,#F2F6FB,#E6EDF6);border:1px solid #DAE4F0;margin-bottom:14px;
 box-shadow:inset 0 1px 0 #fff}
.card .ic svg{width:26px;height:26px}
.card h3{margin-bottom:6px}
.card p{font-size:15.5px}
/* bundle */
.bundle{background:linear-gradient(180deg,#FFFFFF,#F7FAFD);border:1px solid var(--line);
 border-radius:22px;padding:26px 22px;box-shadow:var(--sh3)}
.bi{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0;
 border-bottom:1px solid var(--line);font-size:16px}
.bi:last-of-type{border-bottom:0}
.bi s{color:var(--soft);font-size:14px}
.tag{font:800 11px/1 "DM Sans",sans-serif;letter-spacing:.1em;color:#fff;background:var(--grn);
 border-radius:6px;padding:5px 8px;box-shadow:0 2px 6px rgba(30,122,82,.3)}
.tot{display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid var(--ink);
 margin-top:14px;padding-top:16px}
.tot .l{font:600 15px/1.3 "DM Sans",sans-serif;color:var(--mut)}
.tot .p{font-family:Fraunces,serif;font-size:44px;font-weight:600;line-height:1}
.tot .p s{font-size:20px;color:var(--soft);margin-right:8px;font-family:"DM Sans",sans-serif}
.keep{text-align:center;margin:14px 0 4px;font:700 15px/1 "DM Sans",sans-serif;color:var(--grn)}
/* specs */
.specs{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:10px}
.sp{background:#fff;border:1px solid var(--line);border-radius:13px;padding:14px 15px;box-shadow:var(--sh1)}
.sp .k{font:700 11px/1 "DM Sans",sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
.sp .v{margin-top:7px;font-weight:500}
/* faq */
details{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:9px;
 box-shadow:var(--sh1);overflow:hidden}
summary{cursor:pointer;padding:16px 18px;font-weight:700;list-style:none;display:flex;
 justify-content:space-between;gap:12px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--org2);font-size:22px;line-height:1;font-weight:400}
details[open] summary::after{content:"\\2013"}
details p{padding:0 18px 17px;font-size:15.5px}
footer{padding:34px 0 56px;text-align:center;color:var(--soft);font-size:14px}
/* entrance */
.r{opacity:0;transform:translateY(16px)}
.r.in{opacity:1;transform:none;transition:opacity .6s cubic-bezier(.2,.7,.3,1),transform .6s cubic-bezier(.2,.7,.3,1)}
@media (prefers-reduced-motion:reduce){.r,.r.in{opacity:1;transform:none;transition:none}}
"""

feats="".join(f'<div class="card r"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p></div>'
              for i,t,d in FEATS)
bundle="".join(
 f'<div class="bi"><span>{n}</span><span>'
 f'{"<s>$"+v+"</s> <span class=tag>FREE</span>" if free else "$"+v}</span></div>'
 for n,v,free in BUNDLE)
batch="".join(
 f'<div class="bc{" now" if i==3 else ""}"><div class="n">Batch {i+1}</div>'
 f'<div class="s">{"Open now" if i==3 else "Sold out"}</div></div>' for i in range(4))
specs="".join(f'<div class="sp"><div class="k">{k}</div><div class="v">{v}</div></div>' for k,v in SPECS)
faq="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)

HTML=f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hawk Nest V.3 &mdash; Batch 4 Pre-Order, ${PRICE}</title>
<meta name="description" content="Batch 4 is the last run of 2026 &mdash; {UNITS} units, arriving {SHIP}. ${PRICE} with every upgrade included. Ships from South Carolina, duties paid.">
<link rel="icon" href="favicon-192.png">
{FONTS}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=DM+Sans:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style></head><body>
<header><img src="hnh-logo-sm.webp" alt="Hawk Nest Hammocks" width="340" height="266" fetchpriority="high"></header>

<div class="w">
<div class="hero">
 <span class="eyebrow"><span class="dot"></span>Batch {BATCH} &middot; the last run of 2026</span>
 <h1 style="margin-top:16px">A tent that hangs,<br>so the ground stops<br>mattering.</h1>
 <p class="sub">Rain fly, bug net, waterproof floor and a pad pocket, in one shelter that goes up between two trees in about four minutes.</p>
 <div class="art">{HAMMOCK}</div>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">Free shipping &middot; duties included &middot; 30-day refund<br>{UNITS} units, arriving {SHIP}</p>
 <div class="trust"><span>{SHIPPED} shipped</span><span>Lifetime warranty</span><span>Ships from South Carolina</span></div>
</div>
</div>

<section><div class="w">
 <div class="lead r"><h2>Three runs, three sell-outs.</h2>
  <p>We build in limited batches and don&rsquo;t overbuild. Batch {BATCH} is the last of the year.</p></div>
 <div class="batch r">{batch}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>What makes it a shelter<br>and not a nap.</h2>
  <p>A bare hammock has no cover and no net, and below {TEMP_COLD} the air underneath turns it into a wind tunnel.</p></div>
 <div class="feats">{feats}</div>
</div></section>

<section><div class="w">
 <div class="lead r"><h2>Everything, one price.</h2>
  <p>The upgrades people normally add are included while Batch {BATCH} lasts.</p></div>
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
 <div class="lead r"><h2>Straight answers.</h2></div>
 <div class="r">{faq}</div>
</div></section>

<section><div class="w r">
 <div class="lead"><h2>Batch {BATCH} arrives {SHIP}.</h2>
  <p>Reserved in the order they come in.</p></div>
 {cta("Reserve yours &mdash; $"+PRICE)}
 <p class="fine">30 days to change your mind. Full refund, no questions.</p>
</div></section>

<footer>Hawk Nest Hammocks &middot; Built in Canada &middot; Shipped from South Carolina</footer>
<script>
const io=new IntersectionObserver((es)=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{rootMargin:'0px 0px -8% 0px'}});
document.querySelectorAll('.r').forEach((el,i)=>{{el.style.transitionDelay=(i%4*60)+'ms';io.observe(el)}});
</script>
</body></html>"""
open("b4-studio.html","w").write(HTML)
print("b4-studio.html",len(HTML)//1024,"KB")
