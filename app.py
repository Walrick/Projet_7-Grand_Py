#!/usr/bin/python3
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, jsonify
import core.parser as parser
import core.google_api as api_request
import os


# open file .env.txt for key api
with open(".env.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    lg = line.split(" ")
    os.environ[lg[0]] = lg[2]

app = Flask(__name__)
pars = parser.Parser()
api_google = api_request.ApiGoogle()


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
    text_parser = (
        "Mots clés de la recherche : "
        + key_word
        + ", l'adresse est : "
        + text["formatted_address"]
        + ", et le nom de la recherche et : "
        + text["name"]
    )

    return jsonify(status=text_parser, image=url_image)


if __name__ == "__main__":
    app.run()
