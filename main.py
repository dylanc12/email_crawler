import scrapy

class EmailSpider(scrapy.Spider):
  name = 'email-spider'
  start_urls = ['https://mcgovern.mit.edu/']
   
  def parse(self, response):
     EMAIL_SELECTOR = '.quote'
     TEXT_SELECTOR = '.text::text'
     AUTHOR_SELECTOR = '.author::text'
