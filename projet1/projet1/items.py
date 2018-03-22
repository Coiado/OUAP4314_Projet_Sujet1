# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Projet1Item(scrapy.Item):
    localisation = scrapy.Field()
    adresse = scrapy.Field()
    pass
