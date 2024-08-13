import os
from hotels_crawler.models import Base, Hotel
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from scrapy import Request
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

class HotelScraperPipeline:
    def __init__(self):
        db_url = DATABASE_URL
        if not db_url:
            raise ValueError("DATABASE_URL not properly configured")
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.Session()
        try:
            hotel = Hotel(
                country=item.get('country'),
                title=item.get('title'),
                img_src_list=item.get('img_src_list'),
                rating=item.get('rating'),
                room=item.get('room'),
                price=item.get('price'),
                location=item.get('location'),
                latitude=item.get('latitude'),
                longitude=item.get('longitude'),
                image_paths=', '.join(item.get('image_paths', []))
            )
            session.add(hotel)
            session.commit()
        except Exception as e:
            spider.log(f"Failed to process item: {e}")
            session.rollback()
        finally:
            session.close()
        return item

class HotelImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('img_src_list', '').split(','):
            yield Request(image_url.strip())

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item