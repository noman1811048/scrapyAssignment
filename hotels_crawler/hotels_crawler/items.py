import scrapy

class HotelItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    location = scrapy.Field()
    room = scrapy.Field()
    price = scrapy.Field()
    img_src_list = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()  
    latitude = scrapy.Field()
    longitude = scrapy.Field()
