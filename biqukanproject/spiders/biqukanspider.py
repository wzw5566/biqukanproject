# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from biqukanproject.items import BiqukanprojectItem


class BiqukanspiderSpider(scrapy.Spider):
    name = 'biqukanspider' # 爬虫的名称
    allowed_domains = ['biqukan.com'] # 允许的域名
    start_urls = ['http://biqukan.com/0_790/']
    # 开始爬取的链接
    def parse(self, response):
    # 链接爬取的方法
        selector = Selector(response)
        # 创建一个选择器的实例
        listmain = selector.xpath('.//div[@class="listmain"]/dl/dd')[60:64]

        for dd in listmain:
            title_novel = selector.xpath('.//h2/text()').extract_first()
            item = BiqukanprojectItem(title_novel=title_novel)
            partial_url = dd.xpath('.//a/@href').extract_first()
            url = response.urljoin(partial_url)
            title_chapter = dd.xpath('.//a/text()').extract_first()
            item['url'] = url
            item['title_chapter'] =title_chapter
            request = scrapy.Request(url=url,callback=self.parse_body)

            # 从这里可以看出，scrapy.Request返回值是它回调函数的返回值

            # Request中有一个参数是meta
            # 作用是将一个信息（任意的类型）传递给callback回调函数
            # 当然传递使用字典的形式进行的，
            # meta={'key':item}  （下面的request.meta【‘item’】可以这么写）

            # 这里为了将详情页的内容和主页的内容一起存储，用了meta方法对，主页的内容
            # 进行了一个暂存，在后面进行统一的提交
            request.meta['item'] = item # 将item暂存一下
            yield request

    def parse_body(self,response):
    # 爬取详情页的方法
        item = response.meta['item']
        # 这是在回调函数中调用刚传进来的信息
        # 当然用的是字典的形式调用信息的呀
        # 这是回调函数中有一个response的meta属性可以调用传过来的信息
        content_list = response.xpath('.//div[@id="content"]/text()').extract()
        content = '\n\n'.join(content_list)
        # 提取详情页的内容
        item['content'] = content
        print( item['content'])
        yield item
        # yield是将这个函数包装成一个迭代器，每次调用都返回这个item
