import scrapy
from BBCNewsWebCrawler.items import BbcnewswebcrawlerItem


class BBCCSpider(scrapy.Spider):
    name = "bbcNews"

    start_urls = ['https://www.bbc.com/news']

    allowed_domains = ["bbc.com"]

    def parse(self, response):
        general_posts = response.xpath('//div[@data-entityid]')
        for post in general_posts:
            item = BbcnewswebcrawlerItem()
            url = post.css('a::attr(href)').get()
            item['url'] = response.urljoin(url)
            item['title'] = post.css('h3::text').get()
            item['summary'] = post.css('p::text').get()
            item['pubdate'] = post.css('time::attr(datetime)').get()
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.parse_details1)
        must_posts = response.xpath('//li[@data-entityid]')
        for post in must_posts:
            item = BbcnewswebcrawlerItem()
            url = post.css('a::attr(href)').get()
            item['url'] = response.urljoin(url)
            item['title'] = post.css('span::text')[2].get()
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.parse_details1)

    def parse_details1(self, response):
        item = response.meta['item']
        item['children'] = []
        posts = response.css('li')
        for post in posts:
            childItem = BbcnewswebcrawlerItem()
            url = post.css('a::attr(href)').get()
            childItem['next_post_url'] = response.urljoin(url)
            childItem['next_post_pubdate'] = post.xpath('//dd//span[@aria-hidden]/text()').get()
            item['children'].append(childItem)
            yield scrapy.Request(childItem['next_post_url'], meta={'item': item['children']}, callback=self.parse_details1)
            yield item