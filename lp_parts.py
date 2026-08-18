"""Shared content for all six US pre-order pages.
Every page pulls the SAME facts from here, so a correction lands everywhere at once —
which is how the 'no trees = buy a tent' error got into three pages before."""
import json

CHECKOUT = ("https://hawknesthammocks.ca/cart/53200326557993:1,53198306312489:1,"
            "53198306345257:1,46948621254953:1,46948623810857:1,47874384953641:1?country=US")

UNITS       = "9,000+"
REVIEWS     = "1,200+"        # 1,212 published on Judge.me
RATING      = "4.8"           # published mean is 4.85
LOGO_COLOR  = "hnh-logo.png"          # the real sun-mountain mark
LOGO_ALT    = "hnh-logo.png"
LOGO_LIGHT  = "hnh-logo-light.png"   # colour mark, light text — for dark grounds
WARRANTY    = "https://cdn.shopify.com/s/files/1/0815/8498/0265/files/lifetime_warranty_badge.png?v=1779393862"

P = json.load(open("/tmp/us_product_imgs.json"))
IMG = {
 "kit":     P[0],   # everything laid out
 "trees":   P[1],   # hanging in forest
 "pocket":  P[2],   # mattress pocket detail
 "fly":     P[3],   # rain fly / build detail
 "packed":  P[4],   # packed size vs a hand
 "ground":  P[5],   # EASY SET-UP ON THE GROUND  <-- the one that fixes the trees claim
 "forest":  P[6],
 "inside":  P[7],
 "camp":    P[8],
 "dusk":    P[9],
}

CAROUSEL = [
 (IMG["kit"],    "Everything in the box",  "Hammock-tent, bug net, detachable rain fly, straps and hardware."),
 (IMG["ground"], "No trees? Pitch it on the ground",
                 "The V.3 sets up as a ground tent. Two poles, same shelter — you're never stuck."),
 (IMG["pocket"], "Integrated pad pocket",  "Holds a pad up to 25in wide so it can't slide out from under you."),
 (IMG["fly"],    "210T ripstop, 500lb rated","Heavy stitching, sealed seams, and a fly that detaches when you don't want it."),
 (IMG["packed"], "Packs to 5.5 x 5.5 x 16in","4.5–5 lb packed — 5 lb with the waterproof upgrades on."),
 (IMG["inside"], "Room to actually sleep",  "Lie diagonal and the fabric flattens out — no banana shape."),
]

TIMELINE = [
 ("Today",        "You reserve",       "Your place in the September batch is held in the order it was taken."),
 ("Now → Sept",   "Batch production",  "The run is already in production. You're buying from it before it lands."),
 ("Sept 15",      "Ships from South Carolina", "Duties included. Nothing to pay on delivery."),
 ("2–5 days",     "On your doorstep",  "Standard US ground. Free, both ways if you send it back."),
]

FAQ = [
 ("What if there are no trees?",
  "Then you pitch it on the ground. The V.3 sets up as a ground tent using poles — same shelter, "
  "same fly, same bug net. It's the reason people take it above the treeline and onto beaches, and "
  "it's the feature most competitors don't have."),
 ("Will I be cold in it?",
  "It's built as an all-season shelter — enclosed body, full bug net, detachable rain fly, and a "
  "pad pocket that takes a pad up to 25in for genuine winter use. Most of the year you won't reach "
  "for the pad. In deep cold you will, the same as in any shelter."),
 ("What happens when it rains?",
  "Water runs downhill and, hanging, you're not at the bottom of it. The fly sheds it and the "
  "waterproof floor panel is included free with this pre-order. Our reviews are full of ten-hour "
  "storms with people staying dry."),
 ("My back is bad — won't I be folded in half?",
  "That's from lying straight down the middle. Lie slightly diagonal and the fabric flattens under "
  "you, spreading your weight instead of pressing it into hip and shoulder. A lot of our buyers "
  "came to it because the ground was hurting them."),
 ("How long does setup take?",
  "Under five minutes once you've done it twice. Two straps, clip in, fly over the ridgeline, zip "
  "the net. No poles to thread, no stakes to lose."),
 ("Why is it $159 when it looks like $400?",
  "Because it's a pre-order. You're buying from the September batch before it lands, so there's no "
  "warehousing, no inventory float and no retailer margin. What you give up is time — it ships Sept 15."),
 ("Is this a real company?",
  f"{UNITS} units shipped, {REVIEWS} verified reviews averaging {RATING}, a lifetime warranty we "
  "honour and a support inbox we answer. Designed in Canada, shipped to you from South Carolina."),
 ("What if I don't like it?",
  "Send it back, free, both directions, and the hammock carries a lifetime warranty on top."),
]

INCLUDES = [
 ("Hawk Nest V.3 all-season hammock-tent", "included"),
 ("Waterproof bottom upgrade", "$39 → free"),
 ("Waterproof carrying bag", "$19 → free"),
 ("Lifetime warranty", "$59 → free"),
 ("Gridless app — 1 year", "included"),
 ("Free US shipping &amp; returns", "included"),
]
