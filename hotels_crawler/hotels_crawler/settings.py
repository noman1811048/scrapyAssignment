BOT_NAME = 'hotels_crawler'
SPIDER_MODULES = ['hotels_crawler.spiders']
NEWSPIDER_MODULE = 'hotels_crawler.spiders'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'hotels_crawler.pipelines.HotelImagePipeline': 1,  
   'hotels_crawler.pipelines.HotelScraperPipeline': 300,  
}

IMAGES_STORE = 'images'  # Directory to store downloaded images
