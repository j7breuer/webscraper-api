
from flask_restx import fields, Namespace

api = Namespace("Webscraper Models", description = "namespace for webscraper API models")

#-------------------#
# Webscraper Single #
#-------------------#
webscraper_html_single_schema = {
    "url": fields.String(description = "URL to be scraped by API", required = True)
}
webscraper_html_single_model = api.model("webscraper_html_single", webscraper_html_single_schema)

webscraper_js_single_schema = {
    "url": fields.String(description = "URL to be scraped by API", required = True),
    "selector": fields.String(description = "CSS selector to scrape specifically", required = True)
}
webscraper_js_single_model = api.model("webscraper_js_single", webscraper_js_single_schema)

#------------------#
# Webscraper Batch #
#------------------#
webscraper_html_batch_schema = {
    "urls": fields.List(fields.String(description = "Text to be translated by API"), required = True)
}
webscraper_html_batch_model = api.model("webscraper_html_batch", webscraper_html_batch_schema)

webscraper_js_batch_schema = {
    "urls": fields.List(fields.String(description = "Text to be translated by API"), required = True),
    "selectors": fields.List(fields.String(description = "Text to be translated by API"), required = True)
}
webscraper_js_batch_model = api.model("webscraper_js_batch", webscraper_js_batch_schema)