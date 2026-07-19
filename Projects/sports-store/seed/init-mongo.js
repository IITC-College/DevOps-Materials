// Idempotent seed data for the sports-store demo (fictional Stryda brand).
// Runs automatically via /docker-entrypoint-initdb.d on first mongo init
// (only when /data/db is empty).

const now = new Date();

function product(name, slug, description, category, gender, basePrice, tags, variants) {
  return {
    name, slug, description,
    brand: "Stryda",
    category, gender, tags,
    image_url: "",
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
    "Lightweight everyday running shoe with responsive cushioning.",
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
    "Women's edition of the Velocity Runner with a narrower fit.",
    "running-shoes", "women", 129.99, ["running", "lightweight"],
    [
      variant("VRW-PNK-38", "Pink", "38", 129.99, 10),
      variant("VRW-BLK-39", "Black", "39", 129.99, 14),
    ],
  ),
  product(
    "Court Master Pro", "court-master-pro",
    "High-top basketball shoe built for explosive court moves.",
    "basketball-shoes", "men", 149.99, ["basketball", "pro"],
    [
      variant("CM-WHT-43", "White", "43", 149.99, 10),
      variant("CM-RED-44", "Red", "44", 154.99, 7),
      variant("CM-BLK-45", "Black", "45", 149.99, 9),
    ],
  ),
  product(
    "Trailblazer GTX", "trailblazer-gtx",
    "Waterproof trail running shoe with aggressive grip.",
    "running-shoes", "unisex", 159.99, ["trail", "waterproof"],
    [
      variant("TB-GRN-41", "Green", "41", 159.99, 6),
      variant("TB-GRY-42", "Grey", "42", 159.99, 11),
    ],
  ),
  product(
    "Sprint Lite", "sprint-lite",
    "Minimal racing flat for tempo days and race day.",
    "running-shoes", "unisex", 99.99, ["running", "racing"],
    [
      variant("SL-YLW-42", "Yellow", "42", 99.99, 20),
      variant("SL-BLU-43", "Blue", "43", 99.99, 18),
    ],
  ),
  product(
    "Stryda Team Hoodie", "stryda-team-hoodie",
    "Heavyweight fleece hoodie with embroidered logo.",
    "hoodies", "unisex", 69.99, ["casual", "fleece"],
    [
      variant("TH-GRY-M", "Grey", "M", 69.99, 25),
      variant("TH-GRY-L", "Grey", "L", 69.99, 22),
      variant("TH-BLK-M", "Black", "M", 69.99, 16),
    ],
  ),
  product(
    "Flex Training Tee", "flex-training-tee",
    "Breathable quick-dry training t-shirt.",
    "sportswear", "men", 29.99, ["training", "quick-dry"],
    [
      variant("FT-WHT-M", "White", "M", 29.99, 40),
      variant("FT-NVY-L", "Navy", "L", 29.99, 35),
    ],
  ),
  product(
    "Aero Running Shorts", "aero-running-shorts",
    "Featherweight shorts with built-in liner.",
    "sportswear", "women", 39.99, ["running", "summer"],
    [
      variant("AR-BLK-S", "Black", "S", 39.99, 30),
      variant("AR-TEAL-M", "Teal", "M", 39.99, 27),
    ],
  ),
  product(
    "Endurance Crew Socks", "endurance-crew-socks",
    "Cushioned crew socks, 3-pack.",
    "accessories", "unisex", 14.99, ["socks", "3-pack"],
    [
      variant("EC-WHT-ONE", "White", "One Size", 14.99, 60),
      variant("EC-BLK-ONE", "Black", "One Size", 14.99, 55),
    ],
  ),
  product(
    "Pro Gym Duffel", "pro-gym-duffel",
    "40L water-resistant duffel with shoe compartment.",
    "accessories", "unisex", 59.99, ["gym", "bag"],
    [
      variant("GD-BLK-ONE", "Black", "One Size", 59.99, 12),
    ],
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
