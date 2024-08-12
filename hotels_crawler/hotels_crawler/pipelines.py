from hotel_scraper.database import Session
from hotel_scraper.models import Hotel

class HotelScraperPipeline:
    def process_item(self, item, spider):
        session = Session()
        hotel = Hotel(**item)
        session.add(hotel)
        session.commit()
        session.close()
        return item