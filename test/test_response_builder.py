#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest

import core.response_builder as papy_bot
import core.static as static


@pytest.fixture
def address():
    return "10 Quai de la Charente, 75019 Paris, France"


class TestPapy:

    papy = papy_bot.Papy()

    def test_build_address(self, address ):
        text = self.papy.build_address(address, "Openclassrooms")
        text_part = text.split(",")
        assert text_part[0] in static.GRANDPA_START_ADDRESS
