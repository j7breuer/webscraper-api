
# Webscraper Microservice [Beta]
Flask API that provides webscraping capabilities for HTML and JavaScript pages using the requests and requests-html libraries in Python.  The API serves as a centralized location for webscraping requests to store logs, optional capabilities (such as adding IP rotating to the container) for high throughput requests, and more.

The repository does not have any examples of IP rotating to obscure requests but services such as <a href="https://oxylabs.io/">Oxylabs</a> or <a href="https://brightdata.com/">Bright Data</a> could be integrated. 

## Installation
### Install requirements.txt first
```
pip install -r requirements.txt
```

## Usage
Expect the response to follow this format:
```json
{
  "message": "Request for webscrape processed.",
  "data": {
    "request": {
      "url": "<insert url scraped here>"
    },
    "response": {
      "status_code": "<insert response from scrape here>",
      "text": "<insert html/js body here>"
    }
  } 
}
```
If using the JavaScript endpoint, a JavaScript selector will need to be provided as it will be used to downselect from webpage.

### Optional - Sleeping Between Scraping:
Within the webscraper.py script, code can be updated, kept, or removed to sleep between requests.  Currently it will pause the scraper for a random amount of time between 2 and 8 seconds.  If the URL is redirected to another URL, the scraper will sleep for a random amount of time between 5-15 seconds.

## Endpoints:

### GET API Help
'GET /help'

**Response**

- '200 OK' on success

```json
{
  "message": "This is an API meant to conduct basic webscraping for standard HTML pages as well as JavaScript using requests_html."
}
```

### GET API Help Single HTML

'GET /help/single/html'

**Response**

- '200 OK' on success

```json
{
  "message": "Given a url, scrape and return the unparsed text off the HTML page."
}
```

### GET API Help JavaScript

'GET /help/single/js'

**Response**

- '200 OK' on success

```json
{
  "message": "Given a url, scrape and return the unparsed text off the JS page."
}
```

### POST HTML Single

'POST /scrape/single/html'

**Request**
```json
{
  "url": "https://www.google.com"
}
```

**Response**
- '200 OK' on success

```json
{
  "data": {
    "request": {
      "url": "https://www.google.com/"
    },
    "response": {
      "status_code": 200,
      "text": "<!doctype html><html itemscope=\"\" itemtype=\"http://schema.org/.. ... ..."
    }
  },
  "message": "Request for webscrape processed."
}
```

### POST JavaScript Single

'POST /scrape/single/js'

**Request**
```json
{
  "url": "https://www.reuters.com/business/autos-transportation/japan-puts-brakes-lucrative-used-car-trade-with-russia-2023-10-01/",
  "selector": "#fusion-metadata"
}
```

**Response**
- '200 OK' on success

```json
{
  "data": {
    "request": {
      "url": "https://www.reuters.com/business/autos-transportation/japan-puts-brakes-lucrative-used-car-trade-with-russia-2023-10-01/"
    },
    "response": {
      "status_code": 200,
      "text": "window.Fusion=window.Fusion||{};Fusion.arcSite=\"reuters\";Fusion... ... ..."
    }
  }
}
```