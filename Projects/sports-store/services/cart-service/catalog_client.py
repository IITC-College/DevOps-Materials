from os import environ

import httpx
from fastapi import HTTPException

CATALOG_URL = environ.get("CATALOG_URL", "http://localhost:8002")
TIMEOUT = float(environ.get("HTTP_TIMEOUT_SECONDS", "5"))


async def get_variant(sku: str, token: str) -> dict:
    """Fetch a product-variant snapshot (name, price, stock) from the catalog."""
    try:
        async with httpx.AsyncClient(base_url=CATALOG_URL, timeout=TIMEOUT) as client:
            response = await client.get(
                f"/api/internal/variants/{sku}",
                headers={"Authorization": f"Bearer {token}"},
            )
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Catalog service unavailable")
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Unknown SKU")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Catalog service error")
    return response.json()
