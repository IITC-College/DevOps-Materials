from unittest.mock import AsyncMock, MagicMock, patch

PAYMENT_ID = "507f1f77bcf86cd799439031"

CHARGE_PAYLOAD = {
    "idempotency_key": "ORD-2026-000123",
    "order_number": "ORD-2026-000123",
    "amount": 269.98,
    "currency": "USD",
    "card_number": "4242424242424242",
}

STORED_PAYMENT = {
    "_id": PAYMENT_ID,
    "idempotency_key": "ORD-2026-000123",
    "order_number": "ORD-2026-000123",
    "user_id": "507f1f77bcf86cd799439011",
    "amount": 269.98,
    "currency": "USD",
    "card_last4": "4242",
    "status": "succeeded",
}


def test_charge_success(client, auth_headers):
    with patch("routes.payments.payments_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        mock_col.insert_one = AsyncMock(
            return_value=MagicMock(inserted_id=PAYMENT_ID)
        )
        response = client.post(
            "/api/payments/charge", json=CHARGE_PAYLOAD, headers=auth_headers
        )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "succeeded"
    assert body["card_last4"] == "4242"
    inserted = mock_col.insert_one.call_args.args[0]
    assert "card_number" not in inserted


def test_charge_failure_suffix(client, auth_headers):
    payload = dict(CHARGE_PAYLOAD, card_number="4242424242420000")
    with patch("routes.payments.payments_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        mock_col.insert_one = AsyncMock(
            return_value=MagicMock(inserted_id=PAYMENT_ID)
        )
        response = client.post(
            "/api/payments/charge", json=payload, headers=auth_headers
        )

    assert response.status_code == 200
    assert response.json()["status"] == "failed"


def test_charge_idempotent_replay(client, auth_headers):
    with patch("routes.payments.payments_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=STORED_PAYMENT.copy())
        mock_col.insert_one = AsyncMock()
        response = client.post(
            "/api/payments/charge", json=CHARGE_PAYLOAD, headers=auth_headers
        )

    assert response.status_code == 200
    assert response.json()["payment_id"] == PAYMENT_ID
    mock_col.insert_one.assert_not_called()


def test_charge_invalid_amount_422(client, auth_headers):
    payload = dict(CHARGE_PAYLOAD, amount=0)
    response = client.post(
        "/api/payments/charge", json=payload, headers=auth_headers
    )
    assert response.status_code == 422


def test_charge_requires_token(client):
    response = client.post("/api/payments/charge", json=CHARGE_PAYLOAD)
    assert response.status_code == 401


def test_get_payment_found(client, auth_headers):
    with patch("routes.payments.payments_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=STORED_PAYMENT.copy())
        response = client.get(
            "/api/payments/ORD-2026-000123", headers=auth_headers
        )

    assert response.status_code == 200
    assert response.json()["status"] == "succeeded"


def test_get_payment_missing_404(client, auth_headers):
    with patch("routes.payments.payments_collection") as mock_col:
        mock_col.find_one = AsyncMock(return_value=None)
        response = client.get("/api/payments/GHOST", headers=auth_headers)

    assert response.status_code == 404
