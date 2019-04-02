import scrapy
from ..items import QuotesItem
class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
	'http://quotes.toscrape.com/'
	]
	#this start_urls means the url which do you want to scrap 

	def parse(self, response):
		items = QuotesItem()
		#Instance is created

		all_div_quotes = response.css('div.quote')
		#all_div_quotes is used to make to code easier
		#for loop is used to extract the data one by one
		for quotes in all_div_quotes:
			title = quotes.css('.text::text').extract()
			author = quotes.css('.author::text').extract()
			tag = quotes.css('.tags .tag::text').extract()

			items['title'] = title
			items['author'] = author
			items['tag'] = tag
			yield items
			
		next_page= response.css("li.next a::attr(href)").get()
		
		if next_page is not None:
			yield response.follow(next_page, callback = self.parse)

		# title = response.css('.header-box .col-md-8 a::text').extract()

		# yield{'titletext':title}