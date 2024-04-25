import scrapy
import os
# Scrapy file, where I created the json file for my scrapped documents from the chicago wiki page

class ChicagoWikiSpider(scrapy.Spider):
    name = 'chicago_wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Chicago']

    custom_settings = {
        'DEPTH_LIMIT': 1,  # As the data is only required from the main Chicago wiki page
        'CLOSESPIDER_PAGECOUNT': 1,  # The chicago page is only stored
        'AUTOTHROTTLE_ENABLED': True,  # Manages request rates dynamically
    }

    def parse(self, response):
        # Directory for storing scraped data
        dir_path = '/Users/mehalgosalia/CS429_IR_Project/chicago_crawler/chicago_data.json'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Create dictionary to store data
        data = {
            'History': self.extract_section(response, 'History'),
            'Demographics': self.extract_section(response, 'Demographics'),
            'Economy': self.extract_section(response, 'Economy'),
            'Culture and contemporary life': self.extract_section(response, 'Culture and contemporary life'),
            'Law and government': self.extract_section(response, 'Law and government'),
            'Education': self.extract_section(response, 'Education'),
            'Media': self.extract_section(response, 'Media'),
            'Infrastructure': self.extract_section(response, 'Infrastructure'),

        }

        # This saves the data to the JSON file
        filename = '//Users/mehalgosalia/CS429_IR_Project/chicago_crawler/chicago_data.json'
        with open(filename, 'w') as f:
            import json
            json.dump(data, f, ensure_ascii=False, indent=4)

        # for next_page in response.css('a::attr(href)'):
        #     yield response.follow(next_page, self.parse)

    def extract_section(self, response, section_title):
        ''' Extract section title from response '''
        section = response.xpath(f"//h2[.//span[@id='{section_title}']]/following-sibling::p[1] | "
                                 f"//h2[.//span[@id='{section_title}']]/following-sibling::ul[1] | "
                                 f"//h2[.//")
