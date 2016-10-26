#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YykItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    YY_name = scrapy.Field()
    YY_url = scrapy.Field()
    YY_rate = scrapy.Field()
    YY_description = scrapy.Field()
    YY_keshi = scrapy.Field()
