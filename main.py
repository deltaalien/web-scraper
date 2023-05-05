from bs4 import BeautifulSoup

from cache.BasicCache import BasicCache
from ws.WebScraper import WebScraper
from ws.conf.ConfigLoader import ConfigLoader
import GlobalConstants

if __name__ == '__main__':
    # driver = GlobalConstants.WEBDRIVER
    # driver.get("https://www.halooglasi.com/nekretnine/izdavanje-stanova/the-best-in-premium-bw-terra-riverview/5425642948536?kid=4&sid=1681654594925")
    # driver.implicitly_wait(10)
    #
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    #
    # elements = soup.select("img.fotorama__img")
    #
    # data = [element.get("src") for element in elements]
    #
    # print(data)

    config = ConfigLoader.load_from_file(GlobalConstants.PROJECT_ROOT + "/config/halo_oglasi_link.json")

    scraper = WebScraper(config)
    #scraper.scrap()

    cache = BasicCache()

    cache.set("1", "1")
    cache.set("2", "2")
    cache.save()


