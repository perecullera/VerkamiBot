import tweepy, time, sys
from scrapy.spider import Spider
from scrapy.selector import Selector

CONSUMER_KEY = 'd9A58jFxpQURROph3St6g'
CONSUMER_SECRET ='tEaAKgazoS6ADKOFUSnHYPKRAXKiBSGAPnO2FS2szE'
OAUTH_TOKEN = '19491497-4jrBajpX0t2PHevDavyRnyJlkKpNjLwVx6YNBYgY0'
OAUTH_TOKEN_SECRET = 'KqUaDgn2RYfuGJx4b92qSsAn0qo38CCcMGRUpW1GlQ'

ACONSEGUIT = ' '
class CanViesSpider(Spider):	
	name = "CanVies"
	allowed_domains = ["verkami.com"]
	start_urls = [
		"http://www.verkami.com/projects/9257-refemcanvies",
		"http://www.verkami.com/projects/9257-refemcanvies"
	]

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//div[@class="current_amount"]')
		for site in sites:
			title = site.xpath('text()').extract()
			link = site.xpath('strong/text()').extract()
			# link = site.xpath('a/@href').extract()
			desc = site.xpath('/').extract()
			global ACONSEGUIT 
			ACONSEGUIT = str(link)
			print title, link, desc, ACONSEGUIT
			
			

			auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
			auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

			print ACONSEGUIT
			api = tweepy.API(auth)
			string = 'Can Vies. Aconseguit '
			HT = '#RefemCanVies'
			link = ' http://www.verkami.com/projects/9257-refemcanvies'
			string2 = string + ACONSEGUIT[9:15] +' ' + HT + link
			api.update_status(string2)