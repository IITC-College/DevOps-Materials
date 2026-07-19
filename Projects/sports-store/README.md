# Sports Store — Python Microservices E-Commerce (MVP)

A teaching project: a sportswear e-commerce platform ("Stryda Athletics" — a
fictional brand) built as five FastAPI microservices with MongoDB, a React
storefront, and an NGINX API gateway, orchestrated with Docker Compose.

## Architecture

```
Browser
   │
   ▼
NGINX Gateway (:8080) ── serves the React build, routes /api/*
   │
   ├── /api/auth/*      → auth-service    (:8001) ── auth_db
   ├── /api/products*   → catalog-service (:8002) ── catalog_db
   ├── /api/internal/*  → catalog-service            (stock endpoints)
   ├── /api/cart*       → cart-service    (:8003) ── cart_db
   ├── /api/orders*     → order-service   (:8004) ── order_db
   └── /api/payments*   → payment-service (:8005) ── payment_db
                                │
                     one MongoDB container,
                     database-per-service pattern
```

Each service owns its database and never reads another service's collections —
services communicate over REST only. The order service orchestrates checkout
synchronously (a simple saga):

```
checkout → read cart → check stock → create pending order
        → charge payment (idempotent) → on success: decrement stock,
          clear cart, mark paid  /  on failure: mark payment_failed (HTTP 402)
```

## Services

| Service | Port | Database | Responsibilities |
|---|---|---|---|
| auth-service | 8001 | `auth_db` | Register, login, JWT issuance, customer/admin roles, bcrypt hashing |
| catalog-service | 8002 | `catalog_db` | Products with embedded variants (SKU/color/size/price/stock), filters, admin CRUD, internal stock check/decrement |
| cart-service | 8003 | `cart_db` | Per-user cart with product snapshots, quantity merge, subtotal |
| order-service | 8004 | `order_db` | Checkout orchestration, order numbers (`ORD-YYYY-NNNNNN`), history |
| payment-service | 8005 | `payment_db` | Mock provider, idempotency keys, deterministic decline rule |

Inventory lives inside the catalog service for the MVP (embedded
`stock_quantity` per variant). Extracting it into a dedicated inventory
service with reservations is the intended Phase 2 exercise.

## Run it

```bash
cd Projects/sports-store
cp .env.example .env          # optional — defaults work for local dev
docker compose up --build -d
```

Then open **http://localhost:8080**.

On first run, MongoDB's `docker-entrypoint-initdb.d` hook runs
`seed/init-mongo.js`, idempotently loading ten Stryda products and an admin
user (only fires against an empty `mongo-data` volume):

- Admin login: `admin@stryda-sports.com` / `Admin1234!`
- Any card number "pays" successfully — except cards ending in `0000`
  (`PAYMENT_FAILURE_SUFFIX`), which are declined.

Each service also exposes interactive OpenAPI docs, e.g.
http://localhost:8001/docs (auth), http://localhost:8002/docs (catalog).

## Demo flow (curl)

```bash
BASE=http://localhost:8080

# Register + login
curl -X POST $BASE/api/auth/register -H 'Content-Type: application/json' \
  -d '{"email":"daniel@example.com","password":"Str0ngPass!","full_name":"Daniel Cohen"}'
TOKEN=$(curl -s -X POST $BASE/api/auth/login -H 'Content-Type: application/json' \
  -d '{"email":"daniel@example.com","password":"Str0ngPass!"}' | jq -r .access_token)

# Browse and add to cart
curl "$BASE/api/products?category=running-shoes"
curl -X POST $BASE/api/cart/items -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' -d '{"sku":"VR-BLK-42","quantity":2}'

# Checkout (paid) — use a card ending 0000 to see the 402 failure path
curl -X POST $BASE/api/orders/checkout -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' -d '{
    "shipping_address": {"full_name":"Daniel Cohen","street":"Example St 10",
      "city":"Netanya","postal_code":"1234567","country":"Israel"},
    "card_number":"4242424242424242"}'

curl $BASE/api/orders -H "Authorization: Bearer $TOKEN"
```

## Tests

Every service has a fully mocked pytest suite (no MongoDB or network needed):

```bash
cd services/auth-service        # or any other service
pip install -r requirements.txt
pytest tests/ -v
```

CI (`.github/workflows/sports-store-ci.yml`) runs all five suites as a matrix
plus a frontend build check, path-filtered to this project.

## Design notes

- **Database-per-service** on one MongoDB container: `auth_db`, `catalog_db`,
  `cart_db`, `order_db`, `payment_db`. Order items and shipping addresses are
  embedded immutable snapshots — later price or name changes never rewrite
  order history.
- **Inter-service trust**: all services share one `JWT_SECRET`; the order
  service forwards the caller's own bearer token on internal calls. Real
  systems would use dedicated service credentials/mTLS — a documented
  simplification.
- **Stock decrement** uses a guarded atomic update
  (`$elemMatch` + `$inc` with `stock_quantity >= qty`), so concurrent
  checkouts cannot oversell a variant.
- **Payment idempotency**: the charge endpoint is keyed by a unique
  `idempotency_key` (the order number); replays return the stored result
  instead of double-charging.
- **Known gap (on purpose)**: if payment succeeds but the stock decrement
  fails, the order is still marked paid and the inconsistency is only logged.
  Fixing this properly needs inventory *reservations* and asynchronous events
  (RabbitMQ) — that is the Phase 2 exercise this MVP is designed to motivate.

## Extension exercises (Phase 2+)

1. Extract an inventory service with TTL-based reservations.
2. Replace the synchronous checkout saga with RabbitMQ events
   (`OrderCreated`, `PaymentCompleted`, `PaymentFailed`).
3. Add a notification service (MailHog) for order/payment confirmations.
4. Add correlation-ID middleware and structured JSON logging across services.
5. Move carts to Redis; add rate limiting at the gateway.
6. Write Kubernetes manifests and a Helm chart; add Prometheus metrics.

## Security notes (dev defaults)

`JWT_SECRET` defaults to a well-known dev value; set a real secret outside
local development. Passwords are hashed with bcrypt; the payment service
stores only the last four card digits. The `/api/internal/*` routes are
exposed through the gateway for course demos — a production deployment would
keep them reachable only on the service network.
