#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest

import core.parser as parser_file


@pytest.fixture
def param_text():
    return "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"


@pytest.fixture
def param_text_list():
    return [
        "Salut",
        "GrandPy",
        "!",
        "Est-ce",
        "que",
        "tu",
        "connais",
        "l'adresse",
        "d'OpenClassrooms",
        "?",
    ]


class TestParser:
    parser = parser_file.Parser()

    def test_change_type(self, param_text):
        text_list = self.parser.change_type(param_text)
        assert type(text_list) == list

    def test_remove_stop_word(self, param_text_list):
        text_list_finish = self.parser.remove_stop_word(
            param_text_list, self.parser.stop_word
        )
        assert self.parser.stop_word not in text_list_finish

    def test_find_index_research(self, param_text_list):
        index_text = self.parser.find_index_research(
            param_text_list, self.parser.address
        )
        assert index_text == 6

    def test_research_extractor(self, param_text):
        research = self.parser.research_extractor(param_text)
        assert research == "OpenClassrooms"
