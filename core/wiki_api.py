#!/usr/bin/python3
# -*- coding: utf8 -*-

import json
import time
import urllib.error
import urllib.parse
import urllib.request


class ApiWiki:
    def __init__(self):

        self.WIKIPEDIA_URL = "https://fr.wikipedia.org/w/api.php"

    def wiki_get_text(self, title):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "action": "parse",
                "prop": "wikitext",
                "page": f"{title}",
                "formatversion": "2",
                "format": "json",
            }
        )
        url = f"{self.WIKIPEDIA_URL}?{params}"

        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 5  # Set the maximum retry delay to 5 seconds.

        while True:
            try:
                # Get the API response.
                response = urllib.request.urlopen(url)

            except urllib.error.URLError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = json.load(response)
                return result

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    def wiki_geosearch(self, latitude, longitude):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "format": "json",
                "list": "geosearch",
                "gscoord": f"{latitude}|{longitude}",
                "gslimit": "10",
                "gsradius": "10000",
                "action": "query",
            }
        )
        url = f"{self.WIKIPEDIA_URL}?{params}"

        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 5  # Set the maximum retry delay to 5 seconds.

        while True:
            try:
                # Get the API response.
                response = urllib.request.urlopen(url)
            except urllib.error.URLError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = json.load(response)
                return result

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.
