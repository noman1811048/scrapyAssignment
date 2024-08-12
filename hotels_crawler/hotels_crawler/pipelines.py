from hotels_crawler.database import Session
from hotels_crawler.models import Hotel

class HotelScraperPipeline:
    def process_item(self, item, spider):
        session = Session()
        hotel = Hotel(**item)
        session.add(hotel)
        session.commit()
        session.close()
        return item