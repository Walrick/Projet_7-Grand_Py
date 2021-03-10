#!/usr/bin/python3
# -*- coding: utf8 -*-

import json
import time
import urllib.error
import urllib.parse
import urllib.request


class ApiWiki :

    def __init__(self):

        self.WIKI_MEDIA_URL = "https://www.mediawiki.org/w/api.php"
        self.WIKIPEDIA_URL = "https://en.wikipedia.org/w/api.php"

    def wiki_media_request (self, title):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "action": "query",
                "prop": "revisions",
                "titles": f"{title}",
                "rvprop": "content",
                "rvslots": "*",
                "formatversion": "2",
                "format": "json"
            }
        )
        url = f"{self.WIKI_MEDIA_URL}?{params}"
        print(url)

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
                print(result)
                return result

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    def wikipedia_request (self, latitude, longitude):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "format": "json",
                "list": "geosearch",
                "gscoord": f"{latitude}|{longitude}",
                "gslimit": "10",
                "gsradius": "10000",
                "action": "query"
            }
        )
        url = f"{self.WIKIPEDIA_URL}?{params}"
        print(url)

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
                print(result)
                return result

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.










