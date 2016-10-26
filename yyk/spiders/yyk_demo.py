#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from yyk.items import YykItem

class YykDemoSpider(scrapy.Spider):
    name = "yyk_demo"
    allowed_domains = ["familydoctor.com.cn"]
    start_urls = (
        'http://yyk.familydoctor.com.cn/disease_2458_0_0_0_1.html',
    )

    def parse(self, response):
        for i in response.xpath('//div[@id="listContent"]/div[@class="listItem"]/h3/a'):
            item = YykItem()
            item['YY_url'] = i.xpath('@href').extract()[0]
            item['YY_name'] = i.xpath('text()').extract()[0]
            #yield item
            urltemp = i.xpath('@href').extract()
            for j in urltemp:
                yield scrapy.Request(j,callback=self.parse_rate,meta={'item':item})

        next_page = response.xpath('//*[@class="endPage"]/a[@class="next"]/@href')  # next page
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_rate(self,response):
        item = response.meta['item']
        item['YY_rate'] = response.xpath('//*[@class="score"]/span/em/text()').extract()[0]
        item['YY_description'] = response.xpath('//span[@itemprop="description"]/text()').extract()[0]
        item['YY_keshi'] = response.xpath('//dd[@class="clearfix"]/a/text()').extract()
        yield item



