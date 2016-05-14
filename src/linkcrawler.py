from lxml import html
import requests


class LinkCrawler:

  def __init__(self, url):
    self.url = url
    self.results = self.crawl()

  def crawl(self):
    return requests.get(self.url)

  def get_links(self):
    return html.fromstring(self.results.text).xpath('//a/@href')


crawl = LinkCrawler('http://ibandominguez.com')
print crawl.get_links()
