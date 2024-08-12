BOT_NAME = 'hotels_crawler'
SPIDER_MODULES = ['hotels_crawler.spiders']
NEWSPIDER_MODULE = 'hotels_crawler.spiders'

# Add other Scrapy settings as needed
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {
   'hotels_crawler.pipelines.HotelScraperPipeline': 300,
}
