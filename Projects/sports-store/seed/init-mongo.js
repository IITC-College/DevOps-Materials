// Idempotent seed data for the sports-store demo (fictional Stryda brand).
// Runs automatically via /docker-entrypoint-initdb.d on first mongo init
// (only when /data/db is empty).

const now = new Date();

const PRODUCT_IMAGES = {
  "velocity-runner": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1200&q=85",
  "velocity-runner-w": "https://images.unsplash.com/photo-1496579538151-212636d0b01c?auto=format&fit=crop&w=1200&q=85",
  "court-master-pro": "https://images.unsplash.com/photo-1558004282-e2b2587e3e47?auto=format&fit=crop&w=1200&q=85",
  "trailblazer-gtx": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=1200&q=85",
  "sprint-lite": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=1200&q=85",
  "stryda-team-hoodie": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=1200&q=85",
  "flex-training-tee": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=1200&q=85",
  "aero-running-shorts": "https://images.unsplash.com/photo-1554139844-af2fc8ad3a3a?auto=format&fit=crop&w=1200&q=85",
  "endurance-crew-socks": "https://images.unsplash.com/photo-1597843797221-e34b4a320b97?auto=format&fit=crop&w=1200&q=85",
  "pro-gym-duffel": "https://images.unsplash.com/photo-1708622833152-924c6e364138?auto=format&fit=crop&w=1200&q=85",
  "apex-cross-trainer": "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=1200&q=85",
  "cloudstrike-runner": "https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=1200&q=85",
  "pivot-low": "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=1200&q=85",
  "core-zip-hoodie": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=1200&q=85",
  "motion-support-bra": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=1200&q=85",
  "tempo-7-8-leggings": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=1200&q=85",
  "everyday-recovery-joggers": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?auto=format&fit=crop&w=1200&q=85",
  "grip-training-gloves": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=1200&q=85",
  "steel-flow-bottle": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=1200&q=85",
  "restore-foam-roller": "https://images.unsplash.com/photo-1599058917212-d750089bc07e?auto=format&fit=crop&w=1200&q=85",
};

const CATEGORY_FEATURES = {
  "running-shoes": ["Responsive foam cushioning", "Breathable engineered upper", "High-traction rubber outsole"],
  "basketball-shoes": ["Court-gripping multidirectional tread", "Reinforced lateral support", "Impact-absorbing heel cushioning"],
  "training-shoes": ["Stable platform for lifting", "Flexible forefoot for agility", "Abrasion-resistant upper"],
  "hoodies": ["Soft heavyweight performance fleece", "Relaxed athletic fit", "Machine washable construction"],
  "sportswear": ["Sweat-wicking technical fabric", "Four-way stretch", "Flat seams reduce distraction"],
  "accessories": ["Built for daily training", "Durable easy-care materials", "Designed to travel"],
};

function product(name, slug, description, category, gender, basePrice, tags, variants) {
  return {
    name, slug, description,
    brand: "Stryda",
    category, gender, tags,
    image_url: PRODUCT_IMAGES[slug] || "",
    rating: Number((4.5 + (slug.length % 5) * 0.1).toFixed(1)),
    review_count: 18 + slug.length * 7,
    features: CATEGORY_FEATURES[category] || CATEGORY_FEATURES.accessories,
    base_price: basePrice,
    variants,
    is_active: true,
    created_at: now,
  };
}

function variant(sku, color, size, price, stock) {
  return { sku, color, size, price, stock_quantity: stock };
}

const products = [
  product(
    "Velocity Runner", "velocity-runner",
    "A lightweight everyday road shoe with responsive cushioning, breathable support and a smooth transition for daily miles or weekend tempo sessions.",
    "running-shoes", "men", 129.99, ["running", "lightweight", "new"],
    [
      variant("VR-BLK-42", "Black", "42", 129.99, 15),
      variant("VR-BLK-43", "Black", "43", 129.99, 12),
      variant("VR-WHT-42", "White", "42", 134.99, 8),
      variant("VR-WHT-44", "White", "44", 134.99, 5),
    ],
  ),
  product(
    "Velocity Runner W", "velocity-runner-w",
    "The women's Velocity pairs a secure, lower-volume fit with soft responsive foam for comfortable everyday runs, walks and busy training weeks.",
    "running-shoes", "women", 129.99, ["running", "lightweight"],
    [
      variant("VRW-PNK-38", "Pink", "38", 129.99, 10),
      variant("VRW-BLK-39", "Black", "39", 129.99, 14),
    ],
  ),
  product(
    "Court Master Pro", "court-master-pro",
    "A supportive high-top basketball shoe built for explosive first steps, confident landings and controlled cuts through every quarter.",
    "basketball-shoes", "men", 149.99, ["basketball", "pro"],
    [
      variant("CM-WHT-43", "White", "43", 149.99, 10),
      variant("CM-RED-44", "Red", "44", 154.99, 7),
      variant("CM-BLK-45", "Black", "45", 149.99, 9),
    ],
  ),
  product(
    "Trailblazer GTX", "trailblazer-gtx",
    "A waterproof trail runner with protective overlays and aggressive all-terrain grip for wet climbs, loose descents and unpredictable weather.",
    "running-shoes", "unisex", 159.99, ["trail", "waterproof"],
    [
      variant("TB-GRN-41", "Green", "41", 159.99, 6),
      variant("TB-GRY-42", "Grey", "42", 159.99, 11),
    ],
  ),
  product(
    "Sprint Lite", "sprint-lite",
    "A stripped-back racing flat with energetic foam and a featherweight upper for track repeats, fast tempo work and your next start line.",
    "running-shoes", "unisex", 99.99, ["running", "racing"],
    [
      variant("SL-YLW-42", "Yellow", "42", 99.99, 20),
      variant("SL-BLU-43", "Blue", "43", 99.99, 18),
    ],
  ),
  product(
    "Stryda Team Hoodie", "stryda-team-hoodie",
    "A heavyweight brushed-fleece hoodie with a structured hood, relaxed athletic cut and understated embroidery for warm-ups and recovery days.",
    "hoodies", "unisex", 69.99, ["casual", "fleece"],
    [
      variant("TH-GRY-M", "Grey", "M", 69.99, 25),
      variant("TH-GRY-L", "Grey", "L", 69.99, 22),
      variant("TH-BLK-M", "Black", "M", 69.99, 16),
    ],
  ),
  product(
    "Flex Training Tee", "flex-training-tee",
    "A breathable quick-dry training tee that moves sweat away from the skin and stays comfortable through strength work, circuits and cooldowns.",
    "sportswear", "men", 29.99, ["training", "quick-dry"],
    [
      variant("FT-WHT-M", "White", "M", 29.99, 40),
      variant("FT-NVY-L", "Navy", "L", 29.99, 35),
    ],
  ),
  product(
    "Aero Running Shorts", "aero-running-shorts",
    "Featherweight running shorts with a supportive built-in liner, secure key pocket and side split for a natural, unrestricted stride.",
    "sportswear", "women", 39.99, ["running", "summer"],
    [
      variant("AR-BLK-S", "Black", "S", 39.99, 30),
      variant("AR-TEAL-M", "Teal", "M", 39.99, 27),
    ],
  ),
  product(
    "Endurance Crew Socks", "endurance-crew-socks",
    "Three pairs of technical crew socks with targeted cushioning, breathable mesh zones and arch support for training days and daily wear.",
    "accessories", "unisex", 14.99, ["socks", "3-pack"],
    [
      variant("EC-WHT-ONE", "White", "One Size", 14.99, 60),
      variant("EC-BLK-ONE", "Black", "One Size", 14.99, 55),
    ],
  ),
  product(
    "Pro Gym Duffel", "pro-gym-duffel",
    "A water-resistant 40-litre training duffel with a ventilated shoe compartment, padded shoulder strap and organized pockets for daily essentials.",
    "accessories", "unisex", 59.99, ["gym", "bag"],
    [
      variant("GD-BLK-ONE", "Black", "One Size", 59.99, 12),
    ],
  ),
  product(
    "Apex Cross Trainer", "apex-cross-trainer",
    "A stable, low-profile training shoe that transitions from heavy lifts to fast conditioning intervals without missing a beat.",
    "training-shoes", "unisex", 119.99, ["training", "lifting", "new"],
    [variant("AX-BLK-41", "Black", "41", 119.99, 18), variant("AX-BLK-43", "Black", "43", 119.99, 21), variant("AX-SND-42", "Sand", "42", 124.99, 12)],
  ),
  product(
    "Cloudstrike Runner", "cloudstrike-runner",
    "Maximum-cushion road runner with a sculpted rocker that makes long recovery miles feel noticeably smoother.",
    "running-shoes", "women", 144.99, ["running", "cushioned", "new"],
    [variant("CS-LIL-38", "Lilac", "38", 144.99, 16), variant("CS-LIL-39", "Lilac", "39", 144.99, 14), variant("CS-WHT-40", "White", "40", 149.99, 9)],
  ),
  product(
    "Pivot Low", "pivot-low",
    "A quick, responsive low-top made for guards who create space, change direction and play at full speed.",
    "basketball-shoes", "unisex", 139.99, ["basketball", "court", "lightweight"],
    [variant("PV-BLU-42", "Royal Blue", "42", 139.99, 11), variant("PV-BLU-44", "Royal Blue", "44", 139.99, 8), variant("PV-CRM-43", "Cream", "43", 144.99, 10)],
  ),
  product(
    "Core Zip Hoodie", "core-zip-hoodie",
    "A clean full-zip layer with structured fleece, secure pockets and enough stretch for warm-ups or the commute home.",
    "hoodies", "unisex", 79.99, ["fleece", "layering", "everyday"],
    [variant("CZ-OLV-M", "Olive", "M", 79.99, 20), variant("CZ-OLV-L", "Olive", "L", 79.99, 17), variant("CZ-BLK-XL", "Black", "XL", 79.99, 13)],
  ),
  product(
    "Motion Support Bra", "motion-support-bra",
    "Medium-support training bra with a smooth underband and breathable racerback for running, circuits and studio sessions.",
    "sportswear", "women", 44.99, ["training", "support", "quick-dry"],
    [variant("MSB-BLK-S", "Black", "S", 44.99, 24), variant("MSB-BLK-M", "Black", "M", 44.99, 28), variant("MSB-BLU-L", "Ocean", "L", 44.99, 16)],
  ),
  product(
    "Tempo 7/8 Leggings", "tempo-7-8-leggings",
    "High-rise performance leggings with compressive stretch, a stay-put waistband and a discreet phone pocket.",
    "sportswear", "women", 64.99, ["running", "training", "pockets"],
    [variant("TL-TEAL-S", "Teal", "S", 64.99, 22), variant("TL-TEAL-M", "Teal", "M", 64.99, 20), variant("TL-BLK-L", "Black", "L", 64.99, 25)],
  ),
  product(
    "Everyday Recovery Joggers", "everyday-recovery-joggers",
    "Tapered recovery pants in soft double-knit fabric, designed for rest days, travel and low-intensity warm-ups.",
    "sportswear", "men", 59.99, ["recovery", "casual", "travel"],
    [variant("ERJ-GRY-M", "Graphite", "M", 59.99, 19), variant("ERJ-GRY-L", "Graphite", "L", 59.99, 23), variant("ERJ-NVY-XL", "Navy", "XL", 59.99, 14)],
  ),
  product(
    "Grip Training Gloves", "grip-training-gloves",
    "Low-bulk lifting gloves with a reinforced synthetic palm and breathable mesh across the back of the hand.",
    "accessories", "unisex", 24.99, ["lifting", "grip", "gym"],
    [variant("GTG-BLK-S", "Black", "S", 24.99, 31), variant("GTG-BLK-M", "Black", "M", 24.99, 38), variant("GTG-BLK-L", "Black", "L", 24.99, 29)],
  ),
  product(
    "Steel Flow Bottle", "steel-flow-bottle",
    "A vacuum-insulated 750ml training bottle that keeps water cold and slips securely into standard gym-bag pockets.",
    "accessories", "unisex", 27.99, ["hydration", "insulated", "bpa-free"],
    [variant("SFB-BLK-750", "Black", "750ml", 27.99, 45), variant("SFB-LIM-750", "Volt", "750ml", 27.99, 32)],
  ),
  product(
    "Restore Foam Roller", "restore-foam-roller",
    "A medium-density textured roller for post-training mobility, targeted release and better recovery between sessions.",
    "accessories", "unisex", 34.99, ["recovery", "mobility", "home-gym"],
    [variant("RFR-BLK-ONE", "Black", "One Size", 34.99, 26), variant("RFR-BLU-ONE", "Blue", "One Size", 34.99, 18)],
  ),
];

// bcrypt hash of "Admin1234!" — precomputed since mongosh has no bcrypt lib.
const ADMIN_USER = {
  email: "admin@stryda-sports.com",
  full_name: "Store Admin",
  role: "admin",
  password_hash: "$2b$12$eWLYbyjFiQ8r8KswdIAp3ODYlksrypqkO1AolG33xBwSo3qZY350W",
};

const catalogDb = db.getSiblingDB("catalog_db");
let inserted = 0;
for (const doc of products) {
  const result = catalogDb.products.updateOne(
    { slug: doc.slug },
    { $setOnInsert: doc },
    { upsert: true },
  );
  catalogDb.products.updateOne(
    { slug: doc.slug },
    { $set: {
      name: doc.name,
      description: doc.description,
      image_url: doc.image_url,
      rating: doc.rating,
      review_count: doc.review_count,
      features: doc.features,
      tags: doc.tags,
    } },
  );
  if (result.upsertedId) inserted++;
}
print(`Seed complete: ${inserted} new products inserted, ${catalogDb.products.countDocuments({})} total.`);

const authDb = db.getSiblingDB("auth_db");
const adminExists = authDb.users.findOne({ email: ADMIN_USER.email });
if (!adminExists) {
  authDb.users.insertOne({ ...ADMIN_USER, created_at: now });
  print(`Admin user created: ${ADMIN_USER.email}`);
} else {
  print(`Admin user already present: ${ADMIN_USER.email}`);
}
