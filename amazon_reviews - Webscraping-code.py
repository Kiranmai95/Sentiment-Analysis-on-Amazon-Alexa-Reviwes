# -*- coding: utf-8 -*-

# Importing Scrapy Library
import scrapy

# Creating a new class to implement Spide
class AmazonReviewSpider(scrapy.Spider):

    # Spider name
    name = 'amazon_review'

    # Domain names to scrape
    allowed_domains = ['amazon.in']

    # Base URL for the MacBook air reviews
    #"https://www.amazon.ca/Echo-Dot-3rd-gen-speaker/product-reviews/B07WLVCCVK/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
    myBaseUrl = "https://www.amazon.in/Echo-Dot-3rd-Gen/product-reviews/B07PFFMP9P/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews &amp;amp;pageNumber="
    start_urls=[]

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,600):
        start_urls.append(myBaseUrl+str(i))

    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')

            # Collecting product star ratings
            star_rating = data.css('.review-rating')

            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0

            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
