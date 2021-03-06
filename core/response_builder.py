#!/usr/bin/python3
# -*- coding: utf8 -*-

import random

import core.parser as parser
import core.google_api as google_api
import core.wiki_api as wiki_api
import core.static as static


class Papy:
    def __init__(self):

        self.parser_user = parser.ParserUser()
        self.parser_wiki = parser.ParserWiki()
        self.google_api = google_api.ApiGoogle()
        self.wiki_api = wiki_api.ApiWiki()

        self.NB_GRANDPA_START_ADDRESS = len(static.GRANDPA_START_ADDRESS) - 1
        self.NB_GRANDPA_MEDIUM_ADDRESS = len(static.GRANDPA_MEDIUM_ADDRESS) - 1
        self.NB_GRANDPA_END_ADDRESS = len(static.GRANDPA_END_ADDRESS) - 1

        self.NB_GRANDPA_START_WIKI = len(static.GRANDPA_START_WIKI) - 1
        self.NB_GRANDPA_MEDIUM_WIKI = len(static.GRANDPA_MEDIUM_WIKI) - 1

    def request(self, text):
        """
        The request methods respond at the question of user
        :param text: str
        :return: address (str), url_image (str), text_wiki (str)
        """

        # keyword research
        key_word = self.parser_user.research_extractor(text)

        # google answer
        response_google = self.google_api.google_place_request(key_word)
        if response_google != "error_message":
            url_image = self.google_api.google_map_request(
                response_google["formatted_address"]
            )

            # Build first bubble
            address = self.build_address(
                response_google["formatted_address"], response_google["name"]
            )

            # Build end bubble
            text_wiki = self.build_wiki(
                response_google["geometry"]["location"]["lat"],
                response_google["geometry"]["location"]["lng"],
            )

            return address, url_image, text_wiki

        else:

            address = "Mhh se que tu me dis ne me parle pas"
            text_wiki = "Tu peux répéter ?"
            url_image = ""
            return address, url_image, text_wiki

    def build_address(self, address, name):
        """
        The build_address methods build the response of address
        :param address:
        :param name:
        :return:
        """

        index_start = random.randint(0, self.NB_GRANDPA_START_ADDRESS)
        index_medium = random.randint(0, self.NB_GRANDPA_MEDIUM_ADDRESS)
        index_end = random.randint(0, self.NB_GRANDPA_END_ADDRESS)

        text = (
            static.GRANDPA_START_ADDRESS[index_start]
            + ", "
            + name
            + " "
            + static.GRANDPA_MEDIUM_ADDRESS[index_medium]
            + " au "
            + address
            + ", "
            + static.GRANDPA_END_ADDRESS[index_end]
            + "."
        )

        return text

    def build_wiki(self, lat, lng):
        """
        The build_wiki methods build the response of wiki
        :param lat: str
        :param lng: str
        :return: str
        """

        index_start = random.randint(0, self.NB_GRANDPA_START_WIKI)
        index_medium = random.randint(0, self.NB_GRANDPA_MEDIUM_WIKI)

        # wiki answer
        wiki_p = self.wiki_api.wiki_geosearch(lat, lng)
        wiki_t = self.wiki_api.wiki_get_text(
            wiki_p["query"]["geosearch"][0]["title"]
        )

        distance = str(wiki_p["query"]["geosearch"][0]["dist"])
        title = wiki_p["query"]["geosearch"][0]["title"]

        # Parse the text
        text_wiki = self.parser_wiki.text_wiki(wiki_t["parse"]["wikitext"])

        text = (
            static.GRANDPA_START_WIKI[index_start]
            + " "
            + title
            + ", "
            + static.GRANDPA_MEDIUM_WIKI[index_medium]
            + " "
            + distance
            + " m, "
            + text_wiki
        )

        return text
