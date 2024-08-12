import scrapy
import json
import random
import os
import requests
from hotels_crawler.items import HotelCrawlerItem
from hotels_crawler.database import Session
from hotels_crawler.models import Hotel

class HotelCrawlerSpider(scrapy.Spider):
    name = 'hotel_crawler'
    
    def start_requests(self):
        url = 'https://uk.trip.com/htls/getHotDestination'
        headers = {
            'x-traceID': '1723089042493.7cfaXTHBxWn7-1723181981937-1029942597',
            'Content-Type': 'application/json',
        }
        yield scrapy.Request(url, method='POST', headers=headers, callback=self.parse_destinations)

    def parse_destinations(self, response):
        try:
            data = json.loads(response.text)
            countryInfo = [(item['id'], item['displayName']) for item in data['group'][0]['hotDestination']]
            location, country = random.choice(countryInfo)
            next_url = f"https://uk.trip.com/hotels/list?city={location}"
            yield scrapy.Request(url=next_url, callback=self.parse_hotels, meta={'country': country})
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to decode JSON: {e}")

    def parse_hotels(self, response):
        session = Session()
        country = response.meta.get('country')
        
        images_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        country_dir = os.path.join(images_dir, country)
        if not os.path.exists(country_dir):
            os.makedirs(country_dir)

        hotels = response.css('.hotel-item')  # Update this selector if needed
        for hotel in hotels:
            items = HotelCrawlerItem()
            title = hotel.css('.hotel-name::text').get()
            img_src_list = hotel.css('.hotel-image::attr(src)').getall()
            rating = hotel.css('.hotel-rating::text').get()
            room = hotel.css('.room-type::text').get()
            price = hotel.css('.hotel-price::text').get()
            location = hotel.css('.hotel-location::text').get()

            for img_src in img_src_list:
                img_name = f"{title}_{img_src.split('/')[-1]}"
                img_path = os.path.join(country_dir, img_name)
                self.download_image(img_src, img_path)

            items['country'] = country
            items['title'] = title
            items['img_src_list'] = ','.join(img_src_list)
            items['rating'] = rating
            items['room'] = room
            items['price'] = price
            items['location'] = location

            # Save to database
            hotel_entry = Hotel(
                country=country,
                title=title,
                img_src_list=items['img_src_list'],
                rating=float(rating) if rating else None,
                room=room,
                price=float(price.replace('£', '')) if price else None,
                location=location
            )
            session.add(hotel_entry)
            session.commit()

            yield items

    def download_image(self, img_url, path):
        try:
            response = requests.get(img_url)
            with open(path, 'wb') as f:
                f.write(response.content)
            self.logger.info(f"Image saved to {path}")
        except Exception as e:
            self.logger.error(f"Failed to download {img_url}: {e}")