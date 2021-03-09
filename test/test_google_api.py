#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest
from io import BytesIO
import json

import core.google_api as api_request


@pytest.fixture
def http_return(mocker):
    results = {
        "candidates": [
            {
                "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                "name": "OpenClassrooms",
            }
        ],
        "status": "OK",
    }
    url_test = mocker.patch(
        "urllib.request.urlopen", return_value=BytesIO(json.dumps(results).encode())
    )


class TestApiGoogle:
    api_google = api_request.ApiGoogle()

    def test_google_place_request(self, http_return):
        result = self.api_google.google_place_request("test au hasard")
        assert result["formatted_address"] == "10 Quai de la Charente, 75019 Paris, France"


