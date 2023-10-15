
from flask import Flask, jsonify, abort
from flask_restx import Resource, Api, fields
from requests.api import request
from restx_models.schemas import api as webscraper_models
from flask_restx.apidoc import apidoc
from webscraper import WebScraper

# Load webscraper and start HTMLSession
ws = WebScraper()

app = Flask(__name__)
api = Api(app)

api.add_namespace(webscraper_models)

@api.route("/help", methods = ["GET"])
class help(Resource):
    def get(self):
        return {
            "message": "This is an API meant to conduct basic webscraping for standard HTML pages as well as JavaScript using requests_html."
        }

@api.route("/help/single/html", methods = ["GET"])
class help_single(Resource):
    def get(self):
        return {
            "message": "Given a url, scrape and return the unparsed text off the HTML page."
        }
    
@api.route("/help/single/js", methods = ["GET"])
class help_single(Resource):
    def get(self):
        return {
            "message": "Given a url, scrape and return the unparsed text off the JS page."
        }

@api.route("/help/batch", methods = ["GET"])
class help_batch(Resource):
    def get(self):
        return {
            "message": "Given an array of urls, scrape and return the unparsed text off the pages."
        }
    
@api.route("/scrape/single/html", methods = ["POST"])
class webscrape_single(Resource):
    @api.expect(webscraper_models.models["webscraper_html_single"], validate = True)
    def post(self):
        data = api.payload
        url = data["url"]
        oupt = ws.scrape_html(url)

        return jsonify(
            {
                "message": "Request for webscrape processed.",
                "data": {
                    "request": {
                        "url": url
                    },
                    "response": {
                        "status_code": oupt["status_code"],
                        "text": oupt["text"]
                    }
                }
            }
        )
    
@api.route("/scrape/single/js", methods = ["POST"])
class webscrape_single(Resource):
    @api.expect(webscraper_models.models["webscraper_js_single"], validate = True)
    def post(self):
        data = api.payload
        url = data["url"]
        selector = data["selector"]
        oupt = ws.scrape_js(url, selector)

        return jsonify(
            {
                "message": "Request for webscrape processed.",
                "data": {
                    "request": {
                        "url": url
                    },
                    "response": {
                        "status_code": oupt["status_code"],
                        "text": oupt["text"]
                    }
                }
            }
        )
    
# Run API
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = False, port = 7654)