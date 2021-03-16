#!/usr/bin/python3
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, jsonify
import core.parser as parser
import core.google_api as google_api
import core.wiki_api as wiki_api
import os


# open file .env for key api
with open(".env", "r") as file:
    lines = file.readlines()
for line in lines:
    lg = line.split(" ")
    os.environ[lg[0]] = lg[2]

app = Flask(__name__)
pars = parser.Parser()
api_google = google_api.ApiGoogle()
api_wiki = wiki_api.ApiWiki()


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/test_ajax/")
def get_ajax():
    msg = request.args.get("variable")
    key_word = pars.research_extractor(msg)
    text = api_google.google_place_request(key_word)
    url_image = api_google.google_map_request(text["formatted_address"])
    wikip = api_wiki.wiki_geosearch(
        text["geometry"]["location"]["lat"], text["geometry"]["location"]["lng"]
    )
    wikim = api_wiki.wiki_get_text(wikip["query"]["geosearch"][0]["title"])
    text_wiki = pars.text_wiki(wikim["parse"]["wikitext"])
    text_parser = (
        "Mots clés de la recherche : "
        + key_word
        + ", l'adresse est : "
        + text["formatted_address"]
        + ", et le nom de la recherche et : "
        + text["name"]
        + ", les coordonnées sont : lat : "
        + str(text["geometry"]["location"]["lat"])
        + " lng : "
        + str(text["geometry"]["location"]["lng"])
        + ", résultat sur wikipedia: titre: "
        + wikip["query"]["geosearch"][0]["title"]
        + ", distance cible : "
        + str(wikip["query"]["geosearch"][0]["dist"])
        + ", texte récupéré : "
        + text_wiki
    )

    return jsonify(status=text_parser, image=url_image)


if __name__ == "__main__":
    app.run()
