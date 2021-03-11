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

@pytest.fixture
def param_text_wiki():
    return "{{Ébauche|Paris}}\n{{Infobox Voie parisienne\n | num arr        = {{19e}}\n | nom            = Quai de la Gironde\n | latitude       = 48.8965\n | longitude      = 2.383164\n | arrondissement = [[19e arrondissement de Paris|19{{e}}]]\n | quartier       = \n | début          = [[Quai de l'Oise]]\n | fin            = [[Boulevard Macdonald]]\n | longueur       = 740\n | largeur        = 5\n | création       = 1863\n | dénomination   = 1873\n | ancien nom     = \n | photo          = Quai de la Gironde à Paris 12.jpg\n | légende        = \n | Ville de Paris = 4147\n | DGI            = 4197\n | commons        = Category:Quai de la Gironde (Paris)\n}}\nLe '''quai de la Gironde''' est un quai situé le long du [[canal Saint-Denis]], à [[Paris]], dans le [[19e arrondissement de Paris|{{19e|arrondissement}}]].\n\n== Situation et accès ==\nIl fait face au [[quai de la Charente]], commence au [[quai de l'Oise]] et se termine [[avenue Corentin-Cariou]].\n\nLa ligne {{Tramway d'Île-de-France/correspondances avec intitulé|3b}} du tramway passe sur ce quai.\n\n== Origine du nom ==\nLe quai porte le [[Estuaire de la Gironde|nom]] que prend le fleuve, la [[Garonne]]"


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

    def test_text_wiki(self, param_text_wiki):
        text = self.parser.text_wiki(param_text_wiki)
        assert text == "Le quai de la Gironde est un quai situé le long du canal Saint-Denis, à Paris, dans le 19e arrondissement de Paris. Il fait face au quai de la Charente, commence au quai de l'Oise et se termine avenue Corentin-Cariou. La ligne du tramway passe sur ce quai."
