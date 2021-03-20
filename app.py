#!/usr/bin/python3
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, jsonify
import os

import core.response_builder as papy

def setup_local():

    # open file .env for key api
    with open(".env", "r") as file:
        lines = file.readlines()
    for line in lines:
        lg = line.split(" ")
        os.environ[lg[0]] = lg[2]


setup_local()

# Init Papy
papy = papy.Papy()

# Init Flask
app = Flask(__name__)


# Route index
@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


# Route ajax
@app.route("/request_ajax/")
def get_ajax():
    # Get args user of request
    msg = request.args.get("request_user")

    # Send Papy request
    text_address, url_image, text_wiki = papy.request(msg)

    return jsonify(address=text_address, image=url_image, history=text_wiki)


if __name__ == "__main__":
    app.run()
