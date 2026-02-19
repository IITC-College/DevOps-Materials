import pytest
import requests
from unittest.mock import patch, Mock

from main import get_incident_summary


# -----------------------
# Validation Tests
# -----------------------

@pytest.mark.parametrize("api_url, api_key, service_id", [
    ("", "key", "SVC1"),
    ("url", "", "SVC1"),
    ("url", "key", ""),
])
def test_validation_errors(api_url, api_key, service_id):
    with pytest.raises(ValueError):
        get_incident_summary(api_url, api_key, service_id)


# -----------------------
# Successful Response
# -----------------------

@patch("requests.get")
def test_success_multiple_incidents(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "incidents": [
            {
                "id": "INC123",
                "title": "Database CPU is high",
                "urgency": "high",
                "created_at": "2023-10-27T10:00:00Z"
            },
            {
                "id": "INC456",
                "title": "API latency is over threshold",
                "urgency": "low",
                "created_at": "2023-10-27T11:30:00Z"
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = get_incident_summary("https://api.example.com", "key", "SVC1")

    assert result == [
        "[HIGH] INC123: Database CPU is high",
        "[LOW] INC456: API latency is over threshold"
    ]


# -----------------------
# No Incidents
# -----------------------

@patch("requests.get")
def test_empty_incidents(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"incidents": []}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = get_incident_summary("https://api.example.com", "key", "SVC1")

    assert result == []


@patch("requests.get")
def test_missing_incidents_key(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = get_incident_summary("https://api.example.com", "key", "SVC1")

    assert result == []


# -----------------------
# HTTP Errors
# -----------------------

@patch("requests.get")
def test_returns_none_on_503(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
    mock_get.return_value = mock_response

    result = get_incident_summary("https://api.example.com", "key", "SVC1")

    assert result is None


@patch("requests.get")
def test_returns_none_on_404(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
    mock_get.return_value = mock_response

    result = get_incident_summary("https://api.example.com", "key", "SVC1")

    assert result is None