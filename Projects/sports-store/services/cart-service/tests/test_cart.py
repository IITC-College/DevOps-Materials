from unittest.mock import AsyncMock, patch

USER_ID = "507f1f77bcf86cd799439011"

VARIANT_SNAPSHOT = {
    "product_id": "507f1f77bcf86cd799439021",
    "name": "Velocity Runner",
    "image_url": "/img/velocity.png",
    "sku": "VR-BLK-42",
    "color": "Black",
    "size": "42",
    "price": 129.99,
    "stock_quantity": 15,
}


def cart_item(quantity=2):
    return {
        "product_id": "507f1f77bcf86cd799439021",
        "sku": "VR-BLK-42",
        "name": "Velocity Runner",
        "size": "42",
        "color": "Black",
        "quantity": quantity,
        "unit_price": 129.99,
        "image_url": "/img/velocity.png",
    }


def stored_cart(quantity=2):
    return {"_id": "abc", "user_id": USER_ID, "items": [cart_item(quantity)]}


def test_get_cart_empty_shape(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.get("/api/cart", headers=auth_headers)

    assert response.status_code == 200
    assert response.json() == {"items": [], "subtotal": 0}


def test_get_cart_computes_subtotal(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=stored_cart(quantity=2))
        response = client.get("/api/cart", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["subtotal"] == 259.98


def test_get_cart_requires_token(client):
    response = client.get("/api/cart")
    assert response.status_code == 401


def test_add_item_creates_snapshot(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col, \
         patch("routes.cart.catalog_client") as mock_catalog:
        mock_col.find_one = AsyncMock(return_value=None)
        mock_col.update_one = AsyncMock()
        mock_catalog.get_variant = AsyncMock(return_value=VARIANT_SNAPSHOT.copy())
        response = client.post(
            "/api/cart/items",
            json={"sku": "VR-BLK-42", "quantity": 2},
            headers=auth_headers,
        )

    assert response.status_code == 200
    body = response.json()
    assert body["items"][0] == cart_item(quantity=2)
    assert body["subtotal"] == 259.98
    saved_items = mock_col.update_one.call_args.args[1]["$set"]["items"]
    assert saved_items[0]["sku"] == "VR-BLK-42"


def test_add_same_sku_merges_quantity(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col, \
         patch("routes.cart.catalog_client") as mock_catalog:
        mock_col.find_one = AsyncMock(return_value=stored_cart(quantity=2))
        mock_col.update_one = AsyncMock()
        mock_catalog.get_variant = AsyncMock(return_value=VARIANT_SNAPSHOT.copy())
        response = client.post(
            "/api/cart/items",
            json={"sku": "VR-BLK-42", "quantity": 3},
            headers=auth_headers,
        )

    assert response.status_code == 200
    assert response.json()["items"][0]["quantity"] == 5


def test_add_item_insufficient_stock_409(client, auth_headers):
    low_stock = dict(VARIANT_SNAPSHOT, stock_quantity=1)
    with patch("routes.cart.carts_collection") as mock_col, \
         patch("routes.cart.catalog_client") as mock_catalog:
        mock_col.find_one = AsyncMock(return_value=None)
        mock_catalog.get_variant = AsyncMock(return_value=low_stock)
        response = client.post(
            "/api/cart/items",
            json={"sku": "VR-BLK-42", "quantity": 2},
            headers=auth_headers,
        )

    assert response.status_code == 409


def test_update_item_quantity(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=stored_cart(quantity=2))
        mock_col.update_one = AsyncMock()
        response = client.put(
            "/api/cart/items/VR-BLK-42",
            json={"quantity": 4},
            headers=auth_headers,
        )

    assert response.status_code == 200
    assert response.json()["items"][0]["quantity"] == 4


def test_update_item_zero_removes(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=stored_cart(quantity=2))
        mock_col.update_one = AsyncMock()
        response = client.put(
            "/api/cart/items/VR-BLK-42",
            json={"quantity": 0},
            headers=auth_headers,
        )

    assert response.status_code == 200
    assert response.json() == {"items": [], "subtotal": 0}


def test_update_missing_item_404(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.put(
            "/api/cart/items/GHOST",
            json={"quantity": 1},
            headers=auth_headers,
        )

    assert response.status_code == 404


def test_remove_item(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=stored_cart(quantity=2))
        mock_col.update_one = AsyncMock()
        response = client.delete(
            "/api/cart/items/VR-BLK-42", headers=auth_headers
        )

    assert response.status_code == 200
    assert response.json() == {"items": [], "subtotal": 0}


def test_clear_cart(client, auth_headers):
    with patch("routes.cart.carts_collection") as mock_col:
        mock_col.delete_one = AsyncMock()
        response = client.delete("/api/cart", headers=auth_headers)

    assert response.status_code == 200
    query = mock_col.delete_one.call_args.args[0]
    assert query == {"user_id": USER_ID}
