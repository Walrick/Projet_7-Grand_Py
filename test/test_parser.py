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
def param_text_list_space():
    return [
        "Salut ",
        "GrandPy",
        " !",
        "Est-ce",
        "que ",
        "tu",
        " connais",
        "l'adresse",
        "d'OpenClassrooms ",
        "?",
    ]


@pytest.fixture
def param_text_list_punctuation():
    return [
        "Salut ",
        "GrandPy",
        ".",
        "Est-ce",
        "que",
        ",",
        "tu",
        "connais",
        "l'adresse",
        "d'OpenClassrooms",
    ]


@pytest.fixture
def param_text_wiki():
    return "{{Ébauche|Paris}}\n{{Infobox Voie parisienne\n | num arr /   \
        = {{19e}}\n | nom            = Quai de la Gironde\n | latitude    \
        = 48.8965\n | longitude      = 2.383164\n | arrondissement = \
        [[19e arrondissement de Paris|19{{e}}]]\n | quartier       = \n \
        | début          = [[Quai de l'Oise]]\n | fin            \
        = [[Boulevard Macdonald]]\n | longueur       = 740\n | largeur  \
        = 5\n | création       = 1863\n | dénomination   = 1873\n | \
        ancien nom     = \n | photo          = Quai de la \
        Gironde à Paris 12.jpg\n | légende        = \n | Ville de \
        Paris = 4147\n | DGI            = 4197\n | commons       \
        = Category:Quai de la Gironde (Paris)\n}}\nLe \
        '''quai de la Gironde''' est un quai situé le long du [[canal \
        Saint-Denis]], à [[Paris]], dans le [[19e arrondissement de\
        Paris|{{19e|arrondissement}}]].\n\n== Situation et accès \
        ==\nIl fait face au [[quai de la Charente]], commence au \
        [[quai de l'Oise]] et se termine [[avenue Corentin-Cariou]].\
        \n\nLa ligne {{Tramway d'Île-de-France/correspondances avec \
        intitulé|3b}} du tramway passe sur ce quai.\n\n== Origine du \
        nom ==\nLe quai porte le [[Estuaire de la Gironde|nom]] que \
        prend le fleuve, la [[Garonne]]"


@pytest.fixture
def param_text_special():
    return [
        [
            "La",
            "ligne",
            "{{Tramway",
            "d'Île-de-France/correspondances",
            "avec",
            "intitulé|3b}}",
            "du",
            "tramway",
            "passe",
            "sur",
            "ce",
            "quai.",
        ],
        [
            "{{Tramway}}",
            "La",
            "ligne",
            "{{Tramway",
            "d'Île-de-France/correspondances",
            "avec",
            "intitulé|3b}}",
            "du",
            "tramway",
            "passe",
            "sur",
            "ce",
            "quai.",
        ],
    ]


@pytest.fixture
def param_hook():
    return [
        "[[Tramway]]",
        "La",
        "ligne",
        "[[Tramway",
        "d'Île-de-France/correspondances",
        "avec",
        "intitulé|3b]]",
        "du",
        "[[tramway",
        "passe",
        "sur",
        "ce",
        "quai.]]",
        "[[intitulé|3b]]",
    ]


class TestParser:
    parser = parser_file.Parser()
    parser_user = parser_file.ParserUser()
    parser_wiki = parser_file.ParserWiki()

    def test_change_type(self, param_text):
        text_list = self.parser.change_type(param_text)
        assert type(text_list) == list

    def test_remove_stop_word(self, param_text_list):
        text_list_finish = self.parser.remove_stop_word(
            param_text_list, self.parser.stop_word
        )
        assert self.parser.stop_word not in text_list_finish

    def test_find_index_research(self, param_text_list):
        index_text = self.parser_user.find_index_research(
            param_text_list, self.parser_user.address
        )
        assert index_text == 6

    def test_remove_letter(self, param_text_list):
        text = self.parser_user.remove_letter(
            param_text_list, self.parser_user.punctuation
        )
        assert text == [
            "Salut",
            "GrandPy",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "l adresse",
            "d OpenClassrooms",
        ]

    def test_remove_space(self, param_text_list_space):
        text = self.parser.remove_space(param_text_list_space)
        assert text == [
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

    def test_remove_special(self, param_text_special, param_hook):
        text = self.parser_wiki.remove_special(
            param_text_special[0], ["{{", "}}"])
        assert text == [
            "La",
            "ligne",
            "3b",
            "du",
            "tramway",
            "passe",
            "sur",
            "ce",
            "quai.",
        ]

        text = self.parser_wiki.remove_special(
            param_text_special[1], ["{{", "}}"])
        assert text == [
            "Tramway",
            "La",
            "ligne",
            "3b",
            "du",
            "tramway",
            "passe",
            "sur",
            "ce",
            "quai.",
        ]

        text = self.parser_wiki.remove_special(
            param_hook, ["[[", "]]"])
        assert text == [
            "Tramway",
            "La",
            "ligne",
            "3b",
            "du",
            "tramway",
            "passe",
            "sur",
            "ce",
            "quai.",
            "3b",
        ]

    def test_arranger_punctuation(self, param_text_list_punctuation):
        text = self.parser_wiki.arranger_punctuation(
            param_text_list_punctuation)
        assert text == [
            "Salut ",
            "GrandPy.",
            "Est-ce",
            "que,",
            "tu",
            "connais",
            "l'adresse",
            "d'OpenClassrooms",
        ]

    def test_research_extractor(self, param_text):
        research = self.parser_user.research_extractor(param_text)
        assert research == "OpenClassrooms"

    def test_text_wiki(self, param_text_wiki):
        text = self.parser_wiki.text_wiki(param_text_wiki)
        assert (
                text ==
                "Il fait face au quai de la Charente, commence au quai\
             de l'Oise et se termine avenue Corentin-Cariou. La ligne \
             3b du tramway passe sur ce quai."
        )
