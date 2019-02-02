# -*- coding: utf-8 -*-
import scrapy


class TripadvisorSevilleSpider(scrapy.Spider):
    name = 'tripadvisor_seville'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g187443-Seville_Province_of_Seville_Andalucia-Hotels.html/']

    def parse(self, response):
        # Extract data using xpath
        hotel_name = response.xpath('//div[@class="prw_rup prw_meta_hsx_listing_name listing-title"]/div[@class="listing_title"]/a[@class="property_title prominent "]/text()').extract()
        review_count = response.xpath('//a[@class="review_count"]/text()').extract()
        review_avg = response.css('[class~="ui_bubble_rating"]::attr(alt)').extract()

        row_data = zip(hotel_name, review_count, review_avg)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'hotel_name': item[0],
                # item[0] means product in the list and so on, index tells what value to assign
                'review_count': item[1],
                'review_avg': item[2]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = '[class="nav next taLnk ui_button primary"]::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
