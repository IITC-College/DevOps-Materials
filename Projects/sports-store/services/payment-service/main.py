import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import payments_collection
from routes import payments

logger = logging.getLogger("payment-service")

app = FastAPI(title="Sports Store — Payment Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payments.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await payments_collection.create_index("idempotency_key", unique=True)
    except Exception as exc:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning("Index creation skipped: %s", exc)


@app.get("/health")
def health():
    return {"status": "ok", "service": "payment-service"}
