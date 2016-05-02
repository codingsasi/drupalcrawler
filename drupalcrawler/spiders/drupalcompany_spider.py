import scrapy
from drupalcrawler.items import Service, Sector, Location, Company


class DrupalCompanySpider(scrapy.Spider):
    name = 'drupalcompanies'
    allowed_domains = ['www.drupal.org', 'drupal.org']
    start_urls = [
         "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        company = Company()
        company['name'] = response.css('h1::text').extract_first()
        company['link'] = response.css('div.intro a::text').extract_first()

        services = []
        sectors = []
        locations = []
        head_quarters = []
        usual_budget = []
        all_details = []
        for detail in response.css('div.intro dl dd'):
            all_details.append(detail)

        print "=========="
        print all_details
        print "=========="
        return company
