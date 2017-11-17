from scrapy.spider import Spider
from scrapy.selector import Selector

from test1.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["eastmoney.com"]
    start_urls = [
        "http://fund.eastmoney.com/020026.html",
        "http://fund.eastmoney.com/160222.html",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[1]/dl[3]')
        items = []
        for site in sites:
            item = DmozItem() 
            tmp = sel.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/text()').extract()
            item['name'] = tmp[0]
            item['gszze'] = sites.xpath('.//*[@id="gz_gszze"]/text()').extract()[0]
            item['gszzl'] = sites.xpath('.//*[@id="gz_gszzl"]/text()').extract()[0]
            items.append(item)
        return items