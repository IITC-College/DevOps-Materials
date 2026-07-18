import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import users_collection
from routes import auth

logger = logging.getLogger("auth-service")

app = FastAPI(title="Sports Store — Auth Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await users_collection.create_index("email", unique=True)
    except Exception as exc:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning("Index creation skipped: %s", exc)


@app.get("/health")
def health():
    return {"status": "ok", "service": "auth-service"}
