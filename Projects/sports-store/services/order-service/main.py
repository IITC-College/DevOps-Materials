import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import orders_collection
from routes import orders

logger = logging.getLogger("order-service")

app = FastAPI(title="Sports Store — Order Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await orders_collection.create_index("order_number", unique=True)
        await orders_collection.create_index([("user_id", 1), ("created_at", -1)])
        await orders_collection.create_index("status")
    except Exception as exc:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning("Index creation skipped: %s", exc)


@app.get("/health")
def health():
    return {"status": "ok", "service": "order-service"}
