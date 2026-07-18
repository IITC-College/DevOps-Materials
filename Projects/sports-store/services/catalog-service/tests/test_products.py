from unittest.mock import AsyncMock, MagicMock, patch

from tests.conftest import AsyncCursor

PRODUCT_ID = "507f1f77bcf86cd799439021"

SAMPLE_PRODUCT = {
    "_id": PRODUCT_ID,
    "name": "Velocity Runner",
    "slug": "velocity-runner",
    "description": "Lightweight running shoe",
    "brand": "Stryda",
    "category": "running-shoes",
    "gender": "men",
    "tags": ["running", "lightweight"],
    "image_url": "",
    "base_price": 129.99,
    "variants": [
        {"sku": "VR-BLK-42", "color": "Black", "size": "42",
         "price": 129.99, "stock_quantity": 15},
    ],
    "is_active": True,
}

NEW_PRODUCT = {
    "name": "Court Master Pro",
    "slug": "court-master-pro",
    "category": "basketball-shoes",
    "base_price": 149.99,
    "variants": [
        {"sku": "CM-WHT-43", "color": "White", "size": "43",
         "price": 149.99, "stock_quantity": 10},
    ],
}


def test_list_products_builds_filter_query(client):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.find.return_value = AsyncCursor([SAMPLE_PRODUCT.copy()])
        response = client.get(
            "/api/products?category=running-shoes&gender=men&tag=running&q=velocity"
        )

    assert response.status_code == 200
    assert response.json()[0]["slug"] == "velocity-runner"
    query = mock_col.find.call_args.args[0]
    assert query == {
        "is_active": True,
        "category": "running-shoes",
        "gender": "men",
        "tags": "running",
        "$text": {"$search": "velocity"},
    }


def test_list_products_empty(client):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.find.return_value = AsyncCursor([])
        response = client.get("/api/products")

    assert response.status_code == 200
    assert response.json() == []


def test_get_product_by_slug(client):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=SAMPLE_PRODUCT.copy())
        response = client.get("/api/products/velocity-runner")

    assert response.status_code == 200
    assert response.json()["name"] == "Velocity Runner"


def test_get_product_unknown_slug_404(client):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.get("/api/products/nope")

    assert response.status_code == 404


def test_create_product_as_admin(client, admin_headers):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.insert_one = AsyncMock(
            return_value=MagicMock(inserted_id=PRODUCT_ID)
        )
        response = client.post(
            "/api/products", json=NEW_PRODUCT, headers=admin_headers
        )

    assert response.status_code == 201
    assert response.json() == {"id": PRODUCT_ID}


def test_create_product_as_customer_403(client, auth_headers):
    response = client.post("/api/products", json=NEW_PRODUCT, headers=auth_headers)
    assert response.status_code == 403


def test_create_product_anonymous_401(client):
    response = client.post("/api/products", json=NEW_PRODUCT)
    assert response.status_code == 401


def test_delete_product_soft_deletes(client, admin_headers):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.update_one = AsyncMock(return_value=MagicMock(matched_count=1))
        response = client.delete(
            f"/api/products/{PRODUCT_ID}", headers=admin_headers
        )

    assert response.status_code == 200
    update = mock_col.update_one.call_args.args[1]
    assert update == {"$set": {"is_active": False}}


def test_update_product_404_when_missing(client, admin_headers):
    with patch("routes.products.products_collection") as mock_col:
        mock_col.update_one = AsyncMock(return_value=MagicMock(matched_count=0))
        response = client.put(
            f"/api/products/{PRODUCT_ID}",
            json={"base_price": 99.99},
            headers=admin_headers,
        )

    assert response.status_code == 404
