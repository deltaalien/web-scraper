import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from ws.WebScraper import WebScraper
from ws.conf.ConfigLoader import ConfigLoader
import GlobalConstants

if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get("https://www.halooglasi.com/nekretnine/izdavanje-stanova")
    # driver.implicitly_wait(10)
    #
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    #
    # elements = soup.select("h3.product-title a")
    #
    # data = [element.get("href") for element in elements]
    #
    # print(data)

    config = ConfigLoader.load_from_file(GlobalConstants.PROJECT_ROOT + "/config/halo_oglasi_link.json")

    scraper = WebScraper(config)
    scraper.scrap()


