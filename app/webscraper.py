import time
import random
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

class WebScraper:
    def __init__(self):
        self.session = HTMLSession()
    
    def restart_session(self):
        '''
        desc: 
            Given an HTMLSession object to scrape JS, restart the session
        inpt:
            None
        oupt:
            self.session [Session]: Restarted session
        '''
        self.session = HTMLSession()

    def scrape_html(self, url):
        '''
        desc:
            Given a generic webpage, scrape the text. No parsing done.
        inpt:
            url [str]: string of url
        oupt:
            oupt [dict]:
                status_code [str]: response code
                text [str]: html text returned from webpage
        '''
        r = requests.get(url)
        status_code = r.status_code
        text = r.text
        oupt = {
            "status_code": status_code, 
            "text": text
        }
        return oupt
    
    def scrape_js(self, url, selector):
        '''
        desc: 
            Given a JS webpage, scrape the text. No parsing done.
        inpt:
            url [str]: string of url
            selector [str]: CSS selector to pull
        oupt:
            oupt [dict]:
                status_code [str]: response code
                text [str]: text returned from webpage selector
        '''
        try:
            r = self.session.get(url)
            status_code = r.status_code
            body = r.html.find(selector, first = True).text
            oupt = {
                "status_code": status_code,
                "text": body
            }
        except:
            time.sleep(random.randint(2,8)
            r = requests.get(url)
            status_code = r.status_code
            if r.url != url:
                time.sleep(random.randint(5,15)
                r = self.session.get(r.url)
                body = r.html.find(selector, first = True).text
                oupt = {
                    "status_code": r.status_code,
                    "text": body
                }
            else:
                oupt = {
                    "status_code": status_code,
                    "text": "Error parsing."
                }
        return oupt
