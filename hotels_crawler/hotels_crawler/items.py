import scrapy

class HotelCrawlerItem(scrapy.Item):
    country = scrapy.Field()
    title = scrapy.Field()
    img_src_list = scrapy.Field()
    rating = scrapy.Field()
    room = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()