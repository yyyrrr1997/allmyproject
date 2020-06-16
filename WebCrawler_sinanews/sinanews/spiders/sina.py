# -*- coding: utf-8 -*-
import scrapy
import time
import os
from lxml import etree
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ["sina.com.cn"]
    start_urls = ["http://news.sina.com.cn/guide/"]

    def parse(self, response):
        # 解析新闻分类页
        #获取一级标题
        parents_infos =response.xpath('//div[@class="clearfix"]').extract() #列表
        for parents_info in parents_infos:#对于每一个大类
            parents_info = etree.HTML(parents_info)
            if parents_info.xpath('string(//h3/a)') :
                title1 = parents_info.xpath('string(//h3/a)')
            else:
                continue

            title2s = parents_info.xpath('//ul[@class="list01"]/li/a/text()') #列表
            title2_urls =parents_info.xpath('//ul[@class="list01"]/li/a/@href')#列表
            for i in range(len(title2_urls)):#对于每一个小类
                filepath='./data/'+title1+'/'+title2s[i]
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                yield scrapy.Request(title2_urls[i], callback=self.parse1,meta={'filepath':filepath})



    def parse1(self, response):
        #解析新闻集合页
        all_urls =response.xpath("//a/@href").extract() #列表

        sUrl = response.url.split("/")

        sUrl.pop(-2)
        sUrl = "/".join(sUrl)
        for news_url in all_urls:
            if news_url.startswith(sUrl) and news_url.endswith('.shtml'):

                rel = f"string(//a[@href=\"{news_url}\"])"
                title3 =response.xpath(rel).extract_first()

                title = title3.replace("/", "_")
                title = title3.replace("?", "？")
                title = title3.replace(">", "》")
                title = title3.replace("<", "《")
                title = title3.replace(":", "：")
                title = title3.replace("|", "|")
                title = title3.replace('\\', "_")
                title = title3.replace('"', "“")
                title = title3.replace("*", "_")
                storename = response.meta['filepath'] + '/' + title + '.txt'
                yield scrapy.Request(news_url, callback=self.parse2, meta={'storename':storename,'title':title3})
    def parse2(self, response):
        #解析新闻内容

        content =response.xpath('string(//div[@class="article"])').extract_first()


        if content:
            f =open(response.meta['storename'],'w',encoding='utf-8')
            f.write(response.meta['title'])
            f.write(content)
            f.close()
            print('完成新闻：', response.meta['storename'])



