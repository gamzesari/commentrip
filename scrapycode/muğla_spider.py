# -*-coding: utf-8 -*-
import scrapy


from gamzee.items import GamzeeItem
from scrapy import log,Request


class muglaSpider(scrapy.Spider):
    name = "eksisozluk"
    allowed_domains = ["eksisozluk.com"]
    start_urls = ["http://www.eksisozluk.com/"]

    def parse(self, response):

        resort= ["cesme", "foca","urla","selcuk","bergama","seferihisar","ozdere","dikili","akyaka","dalaman","dalyan","bodrum","turkbuku","turgutreis"
        "datca","fethiye","iztuzu","oludeniz","gocek","marmaris","bozburun","icmeler","selimiye","sogut","koycegiz","gulluk","oren","milas","kusadasi","didim","bozcaada","gokceada",
        "alanya","kemer","kekova","olympos","kalkan","kas","side","finike","anamur","manavgat","tarsus","susanoglu","kızkalesi","bozyazı","arsuz","iskenderun"]

        base_url="http://www.eksisozluk.com/%s"
        for re in resort:
            yield Request(base_url % re, self.parse2)

    def parse2(self, response):
        url = response.url
        base_url = url.split('?')[0] + "?p=%s"
        for i in range(80):
             yield Request(base_url % (i + 1), self.parse3)


    def parse3(self, response):
        item = GamzeeItem()
        print("------------page=%s" % (response.url))
        resortName=response.url.split('/')[3]
        sep = '--'
        resortName = resortName.split(sep, 1)[0]
        for i in response.css('ul#entry-list li'):
            comment = i.css(" div.content *::text").extract()
        if comment:
             item['comment'] = comment
             item['resort']=resortName
             #for i in response.xpath("//div[@class='content']"):
              #item['comment']=i.xpath("text()").extract()
             yield item
