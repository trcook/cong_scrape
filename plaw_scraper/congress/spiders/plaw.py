# -*- coding: utf-8 -*-
import scrapy
import re
from congress.items import PLawItem


yrs_to_get=range(93,115)


def numbsuffix(x):
    return "%d%s" % (x,"tsnrhtdd"[(x/10%10!=1)*(x%10<4)*x%10::4])

class PlawSpider(scrapy.Spider):
    name = "plaw"
    allowed_domains = ["congress.gov"]
    def start_requests(self):
        for i in yrs_to_get:
            url='https://www.congress.gov/public-laws/%s-congress'% numbsuffix(i)
            req=scrapy.Request(url,self.parse,meta={'yr':i})
            yield req
    start_urls=[]
    # start_urls=['www.congress.gov/public-laws/%s-congress'% numbsuffix(i) for i in range(93,115)]
    def parse(self, response):
        yr=response.meta['yr']
        pl=response.xpath("//th[contains(@class,'public')]/ancestor::table/tbody/tr/td[1]//text()").extract()
        congnum=response.xpath("//th[contains(@class,'public')]/ancestor::table/tbody/tr/td[2]/a/text()").extract()
        congnum=[re.sub(r"\.","",congnum[i]).lower()+"-%s" % yr for i in range(len(congnum))]
        for i in range(len(congnum)):
            scrapy_item=PLawItem()
            scrapy_item['bill']=congnum[i]
            scrapy_item['plaw']=pl[i]
            yield scrapy_item
# PICKUP HERE: finish writing this spider. put into scrapy record. putput to csv.
        pass
