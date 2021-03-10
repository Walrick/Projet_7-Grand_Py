#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest
from io import BytesIO
import json

import core.google_api as api_google


@pytest.fixture
def http_return(mocker):
    results = {
        "candidates": [
            {
                "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                "geometry": {
                    "location": {"lat": 48.8975156, "lng": 2.3833993},
                    "viewport": {
                        "northeast": {
                            "lat": 48.89886702989273,
                            "lng": 2.384756379892722,
                        },
                        "southwest": {
                            "lat": 48.89616737010729,
                            "lng": 2.382056720107278,
                        },
                    },
                },
                "name": "OpenClassrooms",
            }
        ],
        "status": "OK",
    }
    url_test = mocker.patch(
        "urllib.request.urlopen", return_value=BytesIO(json.dumps(results).encode())
    )


class TestApiGoogle:
    api_google = api_google.ApiGoogle()

    def test_google_place_request(self, http_return):
        result = self.api_google.google_place_request("test au hasard")
        assert (
            result["formatted_address"] == "10 Quai de la Charente, 75019 Paris, France"
        )
