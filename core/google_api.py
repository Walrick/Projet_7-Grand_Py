#!/usr/bin/python3
# -*- coding: utf8 -*-

import json
import time
import urllib.error
import urllib.parse
import urllib.request
import os


class ApiGoogle:

    def __init__(self):

        self.KEY_GOOGLE = os.environ.get('API_GOOGLE')
        self.GOOGLE_PLACE_URL = (
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        )
        self.GOOGLE_MAP_URL = "https://maps.googleapis.com/maps/api/staticmap"

    def google_place_request(self, key_word):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "input": f"{key_word}",
                "inputtype": "textquery",
                "fields": "formatted_address,name",
                "key": self.KEY_GOOGLE,
            }
        )

        url = f"{self.GOOGLE_PLACE_URL}?{params}"
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
                if result["status"] == "OK":
                    return result["candidates"][0]
                elif result["status"] != "UNKNOWN_ERROR":
                    # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                    # ZERO_RESULTS. There is no point retrying these requests.
                    raise Exception(result["error_message"])

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    def google_map_request(self, key_word):

        # Join the parts of the URL together into one string.
        params = urllib.parse.urlencode(
            {
                "center": f"{key_word}",
                # 10 = zoom sur la ville, 15 = zoom sur la rue, 20 = zoom sur le bâtiment
                "zoom": "14",
                "size": "300x300",
                "markers": "red" + f"{key_word}",
                "key": self.KEY_GOOGLE,
            }
        )

        url = f"{self.GOOGLE_MAP_URL}?{params}"
        print(url)
        return url
