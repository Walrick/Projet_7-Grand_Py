#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest
from io import BytesIO
import json

import core.wiki_api as api_wiki


@pytest.fixture
def http_return_wikigeo(mocker):
    results = {
        "batchcomplete": "",
        "query": {
            "geosearch": [
                {
                    "pageid": 3120649,
                    "ns": 0,
                    "title": "Quai de la Gironde",
                    "lat": 48.8965,
                    "lon": 2.383164,
                    "dist": 114.2,
                    "primary": "",
                }
            ]
        },
    }
    return mocker.patch(
        "urllib.request.urlopen", return_value=BytesIO(
            json.dumps(results).encode())
    )


@pytest.fixture
def http_return_wiki_text(mocker):
    results = {
        "parse": {
            "title": "Quai de la Gironde",
            "pageid": 3120649,
            "wikitext": "{{Ébauche|Paris}}\n{{Infobox Voie parisienne\n \
             | num arr        = {{19e}}\n | nom            = Quai de la \
             Gironde\n | latitude       = 48.8965\n | longitude      = \
             2.383164\n | arrondissement = [[19e arrondissement de Paris \
             |19{{e}}]]\n | quartier       = \n | début          = [[Quai \
              de l'Oise]]\n | fin            = [[Boulevard Macdonald]]\n \
              | longueur       = 740\n | largeur        = 5\n | création = \
               1863\n | dénomination   = 1873\n | ancien nom     = \
             \n | photo          = Quai de la Gironde à Paris 12.jpg \
             \n | légende        = \n | Ville de Paris = 4147\n | \
             DGI            = 4197\n | commons        = Category:Quai \
              de la Gironde (Paris)\n}}\nLe '''quai de la Gironde''' \
               est un quai situé le long du [[canal Saint-Denis]], à \
           [[Paris]], dans le [[19e arrondissement de Paris|{{19e \
           |arrondissement}}]].\n\n== Situation et accès ==\nIl \
           fait face au [[quai de la Charente]], commence au [[quai \
            de l'Oise]] et se termine [[avenue Corentin-Cariou]]. \
            \n\nLa ligne {{Tramway d'Île-de-France/correspondances \
             avec intitulé|3b}} du tramway passe sur ce quai.\n\n== \
              Origine du nom ==\nLe quai porte le [[Estuaire de la \
              Gironde|nom]] que prend le fleuve, la [[Garonne]], après \
               avoir reçu la [[Dordogne (fleuve)|Dordogne]] au \
               [[bec d'Ambès]].\n\n== Historique ==\nCette voie \
            de l'[[La Villette (Seine)|ancienne commune de \
            La Villette]] a été classée dans la [[voirie de \
            Paris]] par un décret du {{date-|23 mai 1863}} \
            et porte son nom actuel depuis un arrêté du \
            {{date-|11 juin 1873}}.\n[[Fichier:Panneau \
            Entrepots Généraux.jpg|150px|thumb|gauche|<center> \
            [[Panneau Histoire de Paris]] « [[Entrepôts généraux]] \
            ».</center>]]\n\n== Bâtiments remarquables et lieux de \
            mémoire ==\n{{Numéro|11}} : emplacement des [[Entrepôts \
            généraux]].\n\n== Voir aussi ==\n=== Articles connexes === \
            \n* [[Liste des voies du 19e arrondissement de Paris|Liste \
             des voies du {{19e}} arrondissement de Paris]]\n* [[Liste \
             des voies de Paris]]\n\n=== Navigation ===\n\n{{Palette Quais \
              de Paris}}\n\n{{Portail|Paris|route}}\n\n[[Catégorie:Quai \
           à Paris|Gironde]]\n[[Catégorie:Voie dans le 19e arrondissement \
            de Paris|Gironde (quai)]]",
        }
    }

    return mocker.patch(
        "urllib.request.urlopen", return_value=BytesIO(
            json.dumps(results).encode())
    )


class TestApiWiki:

    api_wiki = api_wiki.ApiWiki()

    def test_wiki_geosearch(self, http_return_wikigeo):
        result = self.api_wiki.wiki_geosearch(777, 999)
        assert result["query"]["geosearch"][0]["title"] == "Quai de la Gironde"

        http_return_wikigeo.assert_called_once_with(
            "https://fr.wikipedia.org/w/api.php?format=json"
            + "&list=geosearch&gscoord=777%7C999&gslimit=10&gsradius="
            + "10000&action=query"
        )

    def test_wiki_get_text(self, http_return_wiki_text):
        result = self.api_wiki.wiki_get_text("title")
        assert result["parse"]["title"] == "Quai de la Gironde"

        http_return_wiki_text.assert_called_once_with(
            "https://fr.wikipedia.org/w/api.php?action=parse&"
            + "prop=wikitext&page=title&formatversion=2&format=json"
        )
