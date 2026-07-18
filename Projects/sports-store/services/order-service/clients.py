from os import environ

import httpx
from fastapi import HTTPException

CART_URL = environ.get("CART_URL", "http://localhost:8003")
CATALOG_URL = environ.get("CATALOG_URL", "http://localhost:8002")
PAYMENT_URL = environ.get("PAYMENT_URL", "http://localhost:8005")
TIMEOUT = float(environ.get("HTTP_TIMEOUT_SECONDS", "5"))


def _headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


async def _request(method: str, url: str, token: str, service: str, json=None):
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            return await client.request(method, url, headers=_headers(token), json=json)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail=f"{service} unavailable")


async def get_cart(token: str) -> dict:
    response = await _request("GET", f"{CART_URL}/api/cart", token, "Cart service")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Cart service error")
    return response.json()


async def clear_cart(token: str) -> None:
    await _request("DELETE", f"{CART_URL}/api/cart", token, "Cart service")


async def check_stock(items: list[dict], token: str) -> list[dict]:
    response = await _request(
        "POST", f"{CATALOG_URL}/api/internal/stock/check", token,
        "Catalog service", json=items,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Catalog service error")
    return response.json()


async def decrement_stock(items: list[dict], token: str) -> bool:
    response = await _request(
        "POST", f"{CATALOG_URL}/api/internal/stock/decrement", token,
        "Catalog service", json=items,
    )
    return response.status_code == 200


async def charge(payload: dict, token: str) -> dict:
    response = await _request(
        "POST", f"{PAYMENT_URL}/api/payments/charge", token,
        "Payment service", json=payload,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Payment service error")
    return response.json()
