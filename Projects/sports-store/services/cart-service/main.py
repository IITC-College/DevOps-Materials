import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import carts_collection
from routes import cart

logger = logging.getLogger("cart-service")

app = FastAPI(title="Sports Store — Cart Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cart.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await carts_collection.create_index("user_id", unique=True)
    except Exception as exc:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning("Index creation skipped: %s", exc)


@app.get("/health")
def health():
    return {"status": "ok", "service": "cart-service"}
