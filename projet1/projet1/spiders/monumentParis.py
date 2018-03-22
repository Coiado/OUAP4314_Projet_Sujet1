# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from ..items import Projet1Item


class MonumentparisSpider(scrapy.Spider):
    name = 'monumentParis'
    allowed_domains = ['culture.gouv.fr']
    start_urls = ['http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC)']

    def parse(self, response):
        all_links = [response.urljoin(elt) for elt in response.css("table a::attr(href)").extract()]
        for link in all_links:
            yield Request(link, callback=self.parse_monument)

    def parse_monument(self, response):
        all_td = [response.css("table")[-2].css("tr")]
        for td in all_td:
            title = response.css("td font n::text").extract()
            print(title)
            #value = response.css("td.champ::text").extract()
            #print(title + " : " + value)
