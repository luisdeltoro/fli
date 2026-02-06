"""Tests for the HTTP client."""

import json

from fli.search.client import Client


def test_set_currency():
    """Test that set_currency sets the locale header with the correct currency."""
    client = Client()
    client.set_currency("EUR")
    header = json.loads(client._client.headers["x-goog-ext-259736195-jspb"])
    assert header[2] == "EUR"


def test_set_currency_usd():
    """Test that set_currency works with USD."""
    client = Client()
    client.set_currency("USD")
    header = json.loads(client._client.headers["x-goog-ext-259736195-jspb"])
    assert header[2] == "USD"
