# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HywCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    pname = scrapy.Field()
    pid = scrapy.Field()
    cids = scrapy.Field()
    aid = scrapy.Field()
    cname = scrapy.Field()
    level = scrapy.Field()
    lastModiTime = scrapy.Field()
    lastCrawTime = scrapy.Field()
    insertTime = scrapy.Field()
    pl1Name = scrapy.Field()
    pl2Name = scrapy.Field()
    pl3Name = scrapy.Field()
    pl4Name = scrapy.Field()
    pl5Name = scrapy.Field()
    rating = scrapy.Field()
    totalprice = scrapy.Field()
    price = scrapy.Field()
    shipping = scrapy.Field()
    feedTileText = scrapy.Field()
    numEntered = scrapy.Field()
    numRating = scrapy.Field()
    viewRate1 = scrapy.Field()
    viewRateGrowth = scrapy.Field()
    intervalRating = scrapy.Field()
    maxNumBought = scrapy.Field()
    genTime = scrapy.Field()
    approvedDate = scrapy.Field()
    merchant = scrapy.Field()
    viewData = scrapy.Field()
    viewTime = scrapy.Field()
