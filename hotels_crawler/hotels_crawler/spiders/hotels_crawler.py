import scrapy
import json
import re
from hotels_crawler.items import HotelItem
from pathlib import Path

class NewHotelSpider(scrapy.Spider):
    name = "hotels_crawler"

    def start_requests(self):
        start_url = "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP"
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        
        yield scrapy.Request(start_url, headers=headers, callback=self.parse_locations)

    def parse_locations(self, response):
        script_text = response.xpath('//script[contains(text(), "window.IBU_HOTEL")]/text()').get()
        try:
            json_data = re.search(r'window\.IBU_HOTEL\s*=\s*(\{.*?\});', script_text, re.DOTALL).group(1)
            data = json.loads(json_data)
        except (AttributeError, json.JSONDecodeError) as e:
            self.log(f"Error parsing JSON data: {e}")
            return

        for city_group in ['inboundCities', 'outboundCities']:
            if city_group in data['initData']['htlsData']:
                for city in data['initData']['htlsData'][city_group]:
                    if city['type'] == "City":
                        if 'recommendHotels' in city:
                            for hotel in city['recommendHotels']:
                                yield HotelItem(
                                    title=hotel['hotelName'],
                                    rating=hotel.get('rating', 'N/A'),
                                    location=city['cityUrl'],
                                    latitude=hotel.get('lat', 'N/A'),
                                    longitude=hotel.get('lon', 'N/A'),
                                    room=[amenities['name'] for amenities in hotel.get('hotelFacilityList', [])],
                                    price=hotel.get('displayPrice', {}).get('price', 'N/A'),
                                    img_src_list=f"https://ak-d.tripcdn.com/images{hotel.get('imgUrl', '')}"
                                )

    def close(self, reason):
        self.log("Spider closed: " + reason)