# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrupalcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
""" Todo
class ProjectSupported(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
"""
class CreditedIssue(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    issues_link = scrapy.Field()

class Service(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class Sector(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class Location(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class Company(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    services = scrapy.Field()
    sectors = scrapy.Field()
    locations = scrapy.Field()
    head_quarters = scrapy.Field()
    usual_budget = scrapy.Field()
    #projects_supported = scrapy.Field()
    credited_issues = scrapy.Field()
