# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BbcnewswebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    pubdate = scrapy.Field()
    url = scrapy.Field()
    children = scrapy.Field()
    author = scrapy.Field()
    context = scrapy.Field()
    next_post_pubdate = scrapy.Field()
    next_post_url = scrapy.Field()
    pass
