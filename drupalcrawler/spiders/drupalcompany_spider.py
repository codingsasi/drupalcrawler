import scrapy, os
from drupalcrawler.items import Service, Sector, Location, Company, CreditedIssue


class DrupalCompanySpider(scrapy.Spider):
    name = 'drupalcompanies'
    allowed_domains = ['www.drupal.org', 'drupal.org']

    start_urls = []
    with open(os.getcwd() + '/start_urls.csv') as f:
        for url in f.readlines():
            start_urls.append(url.rstrip())

    def parse(self, response):
        company = Company()
        company['name'] = response.css('h1::text').extract_first()
        company['link'] = response.css('div.intro a::text').extract_first()

        services = []
        sectors = []
        locations = []
        all_details = []
        credited_issues = []
        head_quarters = ""
        usual_budget = ""

        """
        Serializing all the details of the company, if it exists
        1. Services
        2. Sectors
        3. Locations
        4. Headquarters
        5. Usual Project Budget
        """
        for detail in response.css('div.intro dl dd'):
            all_details.append(detail)

        for i, detail in enumerate(response.css('div.intro dl dt')):
            more_details = response.css('div.intro dl dd')[i]
            item = detail.css('::text').extract_first()
            if item == 'Services':
                for detail in more_details.css('a'):
                    service = Service()
                    service['name'] = detail.css('::text').extract_first()
                    service['link'] = 'www.drupal.org' + detail.css('::attr(href)').extract_first()
                    services.append(service)
            elif item == 'Sectors':
                for detail in more_details.css('a'):
                    sector = Sector()
                    sector['name'] = detail.css('::text').extract_first()
                    sector['link'] = 'www.drupal.org' + detail.css('::attr(href)').extract_first()
                    sectors.append(sector)
            elif item == 'Locations':
                for detail in more_details.css('a'):
                    location = Location()
                    location['name'] = detail.css('::text').extract_first()
                    location['link'] = 'www.drupal.org' + detail.css('::attr(href)').extract_first()
                    locations.append(location)
            elif item == 'Headquarters':
                head_quarters = more_details.css('::text').extract_first()
            elif item == 'Usual project budget':
                usual_budget = more_details.css('::text').extract_first()
            else:
                pass


        company['services'] = services
        company['sectors'] = sectors
        company['locations'] = locations
        company['head_quarters'] = head_quarters
        company['usual_budget'] = usual_budget

        """
        Serializing Credited Issues
        """
        for detail in response.css('div.main .view-issue-credit.view-id-issue_credit > .view-content > ul > li'):
            credited_issue = CreditedIssue()
            credited_issue['name'] = detail.css('span.views-field.views-field-title-1 > span > a::text').extract_first()
            credited_issue['link'] = 'www.drupal.org' + detail.css('span.views-field.views-field-title-1 > span > a::attr(href)').extract_first()
            credited_issue['issues_link'] = 'www.drupal.org' + detail.css('span.views-field.views-field-nid > span > a::attr(href)').extract_first()
            credited_issues.append(credited_issue)

        company['credited_issues'] = credited_issues
        return company
