import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import products_collection
from routes import internal, products

logger = logging.getLogger("catalog-service")

app = FastAPI(title="Sports Store — Catalog Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api")
app.include_router(internal.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await products_collection.create_index("slug", unique=True)
        await products_collection.create_index("variants.sku", unique=True)
        await products_collection.create_index("category")
        await products_collection.create_index("tags")
        await products_collection.create_index(
            [("name", "text"), ("description", "text")]
        )
    except Exception as exc:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning("Index creation skipped: %s", exc)


@app.get("/health")
def health():
    return {"status": "ok", "service": "catalog-service"}
