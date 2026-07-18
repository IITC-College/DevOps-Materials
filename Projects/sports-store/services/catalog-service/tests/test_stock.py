from unittest.mock import AsyncMock, MagicMock, patch


def variant_doc(stock):
    return {"variants": [{"sku": "VR-BLK-42", "stock_quantity": stock}]}


def test_stock_check_mixed_results(client, auth_headers):
    async def find_one(query, *_args, **_kwargs):
        if query["variants.sku"] == "VR-BLK-42":
            return variant_doc(15)
        return None

    with patch("routes.internal.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(side_effect=find_one)
        response = client.post(
            "/api/internal/stock/check",
            json=[
                {"sku": "VR-BLK-42", "quantity": 2},
                {"sku": "GHOST-SKU", "quantity": 1},
            ],
            headers=auth_headers,
        )

    assert response.status_code == 200
    assert response.json() == [
        {"sku": "VR-BLK-42", "available": 15, "in_stock": True},
        {"sku": "GHOST-SKU", "available": 0, "in_stock": False},
    ]


def test_stock_check_insufficient_quantity(client, auth_headers):
    with patch("routes.internal.products_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=variant_doc(1))
        response = client.post(
            "/api/internal/stock/check",
            json=[{"sku": "VR-BLK-42", "quantity": 5}],
            headers=auth_headers,
        )

    assert response.status_code == 200
    assert response.json()[0]["in_stock"] is False


def test_stock_decrement_success(client, auth_headers):
    with patch("routes.internal.products_collection") as mock_col:
        mock_col.update_one = AsyncMock(return_value=MagicMock(modified_count=1))
        response = client.post(
            "/api/internal/stock/decrement",
            json=[{"sku": "VR-BLK-42", "quantity": 2}],
            headers=auth_headers,
        )

    assert response.status_code == 200
    query = mock_col.update_one.call_args.args[0]
    assert query["variants"]["$elemMatch"]["stock_quantity"] == {"$gte": 2}


def test_stock_decrement_insufficient_409(client, auth_headers):
    with patch("routes.internal.products_collection") as mock_col:
        mock_col.update_one = AsyncMock(return_value=MagicMock(modified_count=0))
        response = client.post(
            "/api/internal/stock/decrement",
            json=[{"sku": "VR-BLK-42", "quantity": 99}],
            headers=auth_headers,
        )

    assert response.status_code == 409
    assert response.json()["detail"]["skus"] == ["VR-BLK-42"]


def test_stock_endpoints_require_token(client):
    response = client.post(
        "/api/internal/stock/check", json=[{"sku": "X", "quantity": 1}]
    )
    assert response.status_code == 401
