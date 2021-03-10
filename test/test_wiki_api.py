#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest
from io import BytesIO
import json

import core.wiki_api as api_wiki


@pytest.fixture
def http_return_wikipedia(mocker):
    results = {'batchcomplete': '',
               'query': {'geosearch': [{'pageid': 504400, 'ns': 0, 'title': 'Porte de la Villette (Paris Métro)',
                                        'lat': 48.89709, 'lon': 2.38588, 'dist': 187.4, 'primary': ''}]}}
    url_test = mocker.patch(
        "urllib.request.urlopen", return_value=BytesIO(json.dumps(results).encode())
    )


class TestApiWiki:

    api_wiki = api_wiki.ApiWiki()

    def test_wikipedia_request(self, http_return_wikipedia):
        result = self.api_wiki.wikipedia_request(48.89709, 2.38588)
        assert result["query"]["geosearch"][0]["title"] == "Porte de la Villette (Paris Métro)"

