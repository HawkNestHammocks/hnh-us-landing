# Shared facts for the Batch 4 US pre-order pages. Every number here is taken from the
# existing max-value-batch4.html offer block or Shopify — do not invent or round these.
CART=("https://hawknesthammocks.ca/cart/53200326557993:1,53198306312489:1,53198306345257:1,"
      "46948621254953:1,46948623810857:1,47874384953641:1?country=US")
PRICE="159"; WAS="429"; KEEP="270"; AFTER="229"
SHIP="October 15"; BATCH="4"; UNITS="1,500"
BUNDLE=[("Hawk Nest&trade; V.3 All-Season Hammock Tent","229",False),
        ("Gridless Survival App &mdash; 1 year Premium","79",True),
        ("Lifetime Warranty Upgrade","59",True),
        ("Waterproof Bottom Fabric upgrade","39",True),
        ("Waterproof Carrying Bag upgrade","19",True),
        ("Free Returns","4.99",True)]
FAQ=[("When does it actually arrive?",
  "Batch 4 lands October 15 and ships in the order it was reserved. You get tracking the moment yours leaves the warehouse."),
 ("Why is it a pre-order?",
  "We build in limited runs and don&rsquo;t overbuild. Batches 1, 2 and 3 all sold out before they landed. Reserving from the next run is the only way to guarantee one."),
 ("What happens after Batch 4?",
  "The price goes to $229 and the free upgrades end. No restock date is set beyond that."),
 ("What color do I get?","Navy. It&rsquo;s the only color on the current production run."),
 ("Where does it ship from?","South Carolina, with duties included. No customs bill on arrival."),
 ("Can I order more than one?",
  "Yes. The bundle applies per hammock, so a second one is the same $159 with its own full set of upgrades."),
 ("What if it doesn&rsquo;t work for me?",
  "30 days, full refund, no questions. Anything defective is replaced under the lifetime warranty.")]
# US units throughout — this is a United States page
SPECS=[("Trail weight","About 4 lbs"),("Packed size","16.5 x 5.5 in"),
 ("Capacity","500 lb"),("Pad pocket","Fits pads to 78 x 28 x 3 in"),
 ("Setup","About 5 minutes, two trees"),("Color","Navy")]
TEMP_COLD="50&deg;F"      # below this, bare hammocks get cold underneath
TEMP_TESTED="&minus;22&deg;F"   # -30C, converted for a US audience
SHIPPED="9,000+"
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" '
 'href="https://fonts.gstatic.com" crossorigin>')
def cta(label,cls="cta"):
    return f'<a class="{cls}" href="{CART}" rel="nofollow">{label}</a>'
# Real verified review titles + names, exactly as they appear on the live review widget.
# We only hold titles locally, so no review bodies are written anywhere — nothing invented.
REVIEWS=[("Algonquin Park, Ontario true Hawknest test","Pat Christie"),
 ("Best sleep in the backcountry in a long time","Jordan Danchuk"),
 ("The ultimate backcountry sleep system!","Cooper Mercer"),
 ("A great system for moto-camping","Brandon Williams"),
 ("Most comfortable hammock","MR MOUNTAIN"),
 ("Very spacious!","Jesse Stanley"),
 ("Amazing Hammock!","Andrew Kryshak"),
 ("The best product","Hailey Kusche")]
INSTEAD=[("A tent","and flat ground to put it on"),("A hammock","for when there isn't any"),
 ("A tarp","strung over the top, in the dark"),("A bug net","that snags and tears"),
 ("An underquilt","or a cold back all night"),("A footprint tarp","for the wet under the floor")]
STEPS=[("You reserve it","Card is charged now, which is what funds the run."),
 ("We build it",f"Batch {BATCH} is {UNITS} units, made in one go."),
 ("It ships",f"From South Carolina on {SHIP}, duties already paid."),
 ("You get 30 days","If it's not for you, full refund. No questions.")]

INBOX=[("Rain fly","Full-coverage waterproof cover, detachable"),
 ("Hammock body","With the bug net and pad pocket sewn in"),
 ("Carrying case","Waterproof, the whole thing packs into it"),
 ("Stakes","Two, for the guy lines"),
 ("Tree straps","Two, no knots to learn"),
 ("Guy lines","Two, to pull the fly taut"),
 ("Rigid support poles","Patent-pending design. Holds the fly and net up and off you")]
# Never describe this as a flat-lay hammock — it is not one. Diagonal lie helps, but the
# claim to make is about interior space and headroom from the rigid poles.
BUNDLE_IMG=["product-thumb.jpg","bonus-4-sm.jpg","bonus-3-sm.jpg","bonus-1-sm.jpg","bonus-2-sm.jpg","bonus-6-sm.jpg"]

# Heat-loss explainer, shared by all three pages.
COLD_SVG='''<svg viewBox="0 0 560 250" role="img" aria-label="Cross-section: a bare hammock loses heat underneath, a pad in the pocket blocks it">
<defs><linearGradient id="cold" x1="0" y1="1" x2="0" y2="0">
 <stop offset="0" stop-color="#8FB6DA" stop-opacity=".0"/><stop offset="1" stop-color="#5E93C4" stop-opacity=".55"/></linearGradient>
<linearGradient id="warm" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#F0733A" stop-opacity=".5"/><stop offset="1" stop-color="#F0733A" stop-opacity="0"/></linearGradient></defs>
<text x="140" y="22" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="15" font-weight="700" fill="#0F1B2A">A bare hammock</text>
<text x="420" y="22" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="15" font-weight="700" fill="#0F1B2A">Pad in the pocket</text>
<path d="M40 70 C90 130 190 130 240 70" stroke="#20406B" stroke-width="7" fill="none" stroke-linecap="round"/>
<ellipse cx="140" cy="88" rx="52" ry="15" fill="#0E2440" opacity=".22"/>
<g stroke="#5E93C4" stroke-width="3" stroke-linecap="round">
 <path d="M80 190v-38M110 200v-42M140 205v-46M170 200v-42M200 190v-38"/></g>
<g fill="#5E93C4"><path d="M76 148l4-8 4 8zM106 154l4-8 4 8zM136 158l4-8 4 8zM166 154l4-8 4 8zM196 148l4-8 4 8z"/></g>
<rect x="40" y="196" width="200" height="34" rx="9" fill="url(#cold)"/>
<text x="140" y="222" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#2C5C8C">Moving air takes your heat</text>
<path d="M320 70 C370 130 470 130 520 70" stroke="#20406B" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M334 92 C376 124 464 124 506 92" stroke="#F0733A" stroke-width="11" fill="none" stroke-linecap="round" opacity=".92"/>
<ellipse cx="420" cy="80" rx="52" ry="14" fill="#0E2440" opacity=".22"/>
<rect x="320" y="40" width="200" height="30" rx="9" fill="url(#warm)"/>
<g stroke="#B9C6D4" stroke-width="3" stroke-linecap="round" opacity=".6">
 <path d="M360 196v-30M390 202v-32M420 206v-34M450 202v-32M480 196v-30"/></g>
<text x="420" y="222" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#1E7A52">Pad blocks it, heat stays in</text>
</svg>'''

# Real customer letter, verbatim: ~/projects/hnh-assets/ugc-reviews/2026-07-06_ken_sutherland_v3_review.docx
# Do NOT paraphrase these into new claims, and do not invent additional customer narratives.
KEN_NAME="Ken Sutherland"
KEN_TRIP="Winnipeg, Manitoba to Vancouver Island, by motorcycle. Three weeks."
KEN=[
 "No level ground, no room for a tent, no trees&hellip; no problem! The Hawk Nest Hammock does it all!",
 "I have just returned from a 3 week motorcycle/salmon fishing trip on Vancouver Island BC. I travelled from Winnipeg MB. All but a couple nights were spent in my Hawk Nest Hammock using the Hawk Nest inflatable sleeping pad. I&rsquo;m extremely pleased with comfort and performance of both products.",
 "Temperatures were between 5&deg;C (40&deg;F) and 22&deg;C (72&deg;F) with 3 nights of rain which was a complete non-issue, absolutely zero leaks or drips in the hammock.",
 "I bought an extra set of hammock straps because one strap often won&rsquo;t make it around some of the huge trees in the Pacific Northwest. Set up takes about 5 minutes once you&rsquo;ve done it a few times.",
 "3 nights were spent either on the beach or in areas where trees were too small to support a hammock. Setup on the ground was again, quick and easy. Not much clearance above when pitched on the ground but enough room to read or roll over.",
 "When it looked like my Hawk Nest inflatable sleeping pad would not arrive in time for my departure, Lukas offered to send one ahead to my sons place in Victoria BC at no charge, so it would be there when I arrived. That&rsquo;s above and beyond good customer service.",
 "I&rsquo;m looking forward to many enjoyable sleeps in my Hawk Nest Hammock on future motorcycle, kayaking, hiking and canoeing adventures. Hawk Nest&rsquo;s hammock and sleeping pad are well thought out, quality products at a very reasonable price."]

REV_COUNT="539"; REV_RATING="4.87"
REV_URL="https://hawknesthammocks.ca/products/hawk-nest-all-season-hammock-tent-v-3"
