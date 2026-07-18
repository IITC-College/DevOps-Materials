from unittest.mock import AsyncMock, patch

PRODUCT_DOC = {
    "_id": "507f1f77bcf86cd799439021",
    "name": "Velocity Runner",
    "image_url": "/img/velocity.png",
    "variants": [
        {"sku": "VR-BLK-42", "color": "Black", "size": "42",
         "price": 129.99, "stock_quantity": 15},
    ],
}


def test_get_variant_snapshot(client, auth_headers):
    with patch("routes.internal.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=PRODUCT_DOC.copy())
        response = client.get(
            "/api/internal/variants/VR-BLK-42", headers=auth_headers
        )

    assert response.status_code == 200
    assert response.json() == {
        "product_id": "507f1f77bcf86cd799439021",
        "name": "Velocity Runner",
        "image_url": "/img/velocity.png",
        "sku": "VR-BLK-42",
        "color": "Black",
        "size": "42",
        "price": 129.99,
        "stock_quantity": 15,
    }


def test_get_variant_unknown_sku_404(client, auth_headers):
    with patch("routes.internal.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.get(
            "/api/internal/variants/GHOST", headers=auth_headers
        )

    assert response.status_code == 404
