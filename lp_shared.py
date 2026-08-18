"""Shared markup + one CSS/JS core used by all six pages.
Palette comes from each page's own CSS variables, so the same components take on
each page's look instead of six pages converging on one design."""
import lp_parts as L

CORE_CSS = """
/* ── shared component core; colours come from each page's :root ── */
.lp-sec{padding:52px 0}
.lp-h{font-size:clamp(1.5rem,5vw,2.1rem);line-height:1.12;margin-bottom:8px;color:var(--h);
 font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--hls);text-wrap:balance}
.lp-p{color:var(--b);margin-bottom:14px}
/* reveal on scroll */
.rv{opacity:0;transform:translateY(22px);transition:opacity .7s cubic-bezier(.22,1,.36,1),
 transform .7s cubic-bezier(.22,1,.36,1)}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}}
/* carousel */
.car{position:relative;margin:20px 0}
.car-track{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;
 -webkit-overflow-scrolling:touch;padding-bottom:10px;scrollbar-width:none}
.car-track::-webkit-scrollbar{display:none}
.car-item{flex:0 0 84%;scroll-snap-align:center;border-radius:var(--r);overflow:hidden;
 background:var(--card);border:1px solid var(--line)}
@media(min-width:640px){.car-item{flex:0 0 46%}}
.car-item img{width:100%;display:block;aspect-ratio:1/1;object-fit:cover;background:#fff}
.car-cap{padding:13px 15px}
.car-cap b{display:block;color:var(--h);font-size:1rem;margin-bottom:4px}
.car-cap span{font-size:.86rem;color:var(--b);line-height:1.45}
.car-dots{display:flex;gap:6px;justify-content:center;margin-top:10px}
.car-dots i{width:6px;height:6px;border-radius:50%;background:var(--line);transition:.25s}
.car-dots i.on{background:var(--accent);width:20px;border-radius:3px}
/* photo band between copy */
.band{margin:26px 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--line)}
.band img{width:100%;display:block}
.band figcaption{padding:11px 14px;font-size:.84rem;color:var(--b);background:var(--card)}
/* timeline */
.tl{margin:18px 0}
.tl-row{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid var(--line)}
.tl-row:last-child{border-bottom:none}
.tl-when{flex:0 0 92px;font-size:.78rem;font-weight:700;color:var(--accent);letter-spacing:.04em;
 padding-top:2px}
.tl-what b{display:block;color:var(--h);font-size:1rem;margin-bottom:3px}
.tl-what span{font-size:.9rem;color:var(--b)}
/* faq */
.faq details{border-bottom:1px solid var(--line)}
.faq summary{padding:15px 30px 15px 0;cursor:pointer;list-style:none;position:relative;
 color:var(--h);font-weight:600;font-size:1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:4px;top:13px;font-size:1.4rem;
 color:var(--accent);transition:transform .25s}
.faq details[open] summary:after{transform:rotate(45deg)}
.faq p{padding:0 0 16px;font-size:.94rem;color:var(--b);line-height:1.6}
/* urgency strip */
.urg{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:center;
 padding:12px 14px;border-radius:var(--r);background:var(--card);border:1px solid var(--line);
 font-size:.84rem;color:var(--b);margin:18px 0}
.urg b{color:var(--h)}
.dot{width:7px;height:7px;border-radius:50%;background:#3fbf6a;display:inline-block;
 margin-right:5px;animation:pl 2s ease-in-out infinite}
@keyframes pl{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.82)}}
/* sticky urgency bar */
.sticky{position:fixed;left:0;right:0;bottom:0;z-index:60;transform:translateY(110%);
 transition:transform .35s cubic-bezier(.22,1,.36,1);
 background:var(--stickybg,#12160f);color:#fff;
 box-shadow:0 -6px 26px rgba(0,0,0,.35);padding:10px 14px calc(10px + env(safe-area-inset-bottom))}
.sticky.up{transform:none}
.sticky-in{max-width:720px;margin:0 auto;display:flex;align-items:center;gap:12px}
.sticky-txt{flex:1;min-width:0;line-height:1.25}
.sticky-txt b{display:block;font-size:.94rem}
.sticky-txt span{font-size:.76rem;opacity:.82;display:block;margin-top:1px}
.sticky-cta{flex:0 0 auto;background:var(--accent);color:#fff;text-decoration:none;font-weight:700;
 font-size:.92rem;padding:12px 18px;border-radius:8px;white-space:nowrap}
.sticky-dot{width:7px;height:7px;border-radius:50%;background:#4ade80;display:inline-block;
 margin-right:6px;animation:pl 2s ease-in-out infinite;vertical-align:middle}
@media(max-width:380px){.sticky-txt span{display:none}}
/* logo strip */
.lg{display:flex;align-items:center;justify-content:center;gap:14px;padding:18px 0}
.lg img{height:54px;width:auto}
.lg .badge{height:58px}
.lg.center{justify-content:center}
"""

CORE_JS = """
<script>
(function(){
 var io=new IntersectionObserver(function(es){es.forEach(function(e){
   if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
 document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});
 document.querySelectorAll('.car').forEach(function(car){
   var t=car.querySelector('.car-track'),dots=car.querySelectorAll('.car-dots i');
   if(!t||!dots.length)return;
   t.addEventListener('scroll',function(){
     var i=Math.round(t.scrollLeft/(t.scrollWidth/dots.length));
     dots.forEach(function(d,j){d.classList.toggle('on',j===Math.min(i,dots.length-1))});
   },{passive:true});
 });
 var sb=document.getElementById('stickyBar');
 if(sb){
   var foot=document.querySelector('footer');
   var onScroll=function(){
     var past=window.scrollY>420;
     var atEnd=foot&&foot.getBoundingClientRect().top<window.innerHeight+40;
     sb.classList.toggle('up',past&&!atEnd);
   };
   window.addEventListener('scroll',onScroll,{passive:true});onScroll();
 }
})();
</script>
"""

def logos(badge=False, light=False, center=False, h=None):
    src = L.LOGO_LIGHT if light else L.LOGO_COLOR
    b = f'<img class="badge" src="{L.WARRANTY}" alt="Lifetime warranty" loading="lazy">' if badge else ""
    cls = "lg rv center" if center else "lg rv"
    st = f' style="height:{h}px"' if h else ""
    return f'<div class="{cls}"><img src="{src}"{st} alt="Hawk Nest Hammocks" loading="lazy">{b}</div>'

def band(key, cap):
    return f'<figure class="band rv"><img src="{L.IMG[key]}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'

def carousel():
    items="".join(f'<div class="car-item"><img src="{u}" alt="{t}" loading="lazy">'
                  f'<div class="car-cap"><b>{t}</b><span>{d}</span></div></div>'
                  for u,t,d in L.CAROUSEL)
    dots="".join('<i class="on"></i>' if i==0 else '<i></i>' for i in range(len(L.CAROUSEL)))
    return f'<div class="car rv"><div class="car-track">{items}</div><div class="car-dots">{dots}</div></div>'

def timeline():
    rows="".join(f'<div class="tl-row"><div class="tl-when">{w}</div>'
                 f'<div class="tl-what"><b>{t}</b><span>{d}</span></div></div>'
                 for w,t,d in L.TIMELINE)
    return f'<div class="tl rv">{rows}</div>'

def faq():
    items="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in L.FAQ)
    return f'<div class="faq rv">{items}</div>'

def urgency():
    return (f'<div class="urg rv"><span><span class="dot"></span><b>{L.UNITS}</b> shipped</span>'
            f'<span>·</span><span><b>{L.RATING}</b> from {L.REVIEWS} reviews</span>'
            f'<span>·</span><span>Batch closes when it\'s full — <b>ships Sept 15</b></span></div>')

def sticky(bg="#12160f"):
    return (f'<div class="sticky" id="stickyBar" style="--stickybg:{bg}"><div class="sticky-in">'
            f'<div class="sticky-txt"><b><span class="sticky-dot"></span>$159 &nbsp;·&nbsp; ships Sept 15</b>'
            f'<span>{L.UNITS} shipped · batch closes when full</span></div>'
            f'<a class="sticky-cta" href="{L.CHECKOUT}">Reserve</a></div></div>')

def includes_rows(cls_row="", cls_val=""):
    return "".join(f'<li class="{cls_row}"><span>{n}</span><i class="{cls_val}">{v}</i></li>'
                   for n,v in L.INCLUDES)
