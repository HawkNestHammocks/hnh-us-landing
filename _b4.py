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
SPECS=[("Trail weight","About 4 lbs"),("Packed size","5.5 x 5.5 x 16 in"),
 ("Capacity","500 lb"),("Pad pocket","Fits pads up to 25 in wide"),
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
 ("Spreader poles","Four sections, hold the net off your face"),
 ("Tree straps","Two, no knots to learn"),
 ("Guy lines","Two, to pull the fly taut"),
 ("Stakes","Two, for the guy lines"),
 ("Stuff sack","Waterproof, the whole thing packs into it")]
