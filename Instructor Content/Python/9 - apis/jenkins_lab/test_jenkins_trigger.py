import pytest
import requests
from unittest.mock import patch, Mock

from main import trigger_jenkins_job


# ---------------------------
# Validation Tests
# ---------------------------

def test_raises_value_error_for_empty_job_name():
    with pytest.raises(ValueError):
        trigger_jenkins_job("https://jenkins.example.com", "", "token123")


def test_raises_value_error_for_empty_url():
    with pytest.raises(ValueError):
        trigger_jenkins_job("", "my-job", "token123")


def test_raises_value_error_for_empty_token():
    with pytest.raises(ValueError):
        trigger_jenkins_job("https://jenkins.example.com", "my-job", "")


# ---------------------------
# Success Case
# ---------------------------

@patch("requests.post")
def test_returns_true_on_successful_trigger(mock_post):
    mock_response = Mock()
    mock_response.status_code = 201
    mock_post.return_value = mock_response

    result = trigger_jenkins_job(
        "https://jenkins.example.com",
        "my-job",
        "token123"
    )

    assert result is True


# ---------------------------
# Error Cases
# ---------------------------

@patch("requests.post")
def test_returns_false_on_unauthorized_error(mock_post):
    mock_response = Mock()
    mock_response.status_code = 401
    mock_post.return_value = mock_response

    result = trigger_jenkins_job(
        "https://jenkins.example.com",
        "my-job",
        "bad-token"
    )

    assert result is False


@patch("requests.post")
def test_returns_false_on_not_found_error(mock_post):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_post.return_value = mock_response

    result = trigger_jenkins_job(
        "https://jenkins.example.com",
        "unknown-job",
        "token123"
    )

    assert result is False


@patch("requests.post")
def test_returns_false_on_network_error(mock_post):
    mock_post.side_effect = requests.exceptions.RequestException

    result = trigger_jenkins_job(
        "https://jenkins.example.com",
        "my-job",
        "token123"
    )

    assert result is False
