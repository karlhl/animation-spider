import scrapy
from myspider.items import MyspiderItem

# scrapy crawl weather --nolog

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['agemys.com']

    # start_urls = ['http://www.tianqihoubao.com/lishi/xian/month/201510.html']

    def parse(self, response):
        # 提取数据
        node_list = response.xpath('//*[@id="container"]/div[4]/div[2]/div/div')
        # print(len(node_list))
        for i, node in enumerate(node_list):
            # if i != 5:
            item = MyspiderItem()
            item["area"] = node.xpath("./ul/li[1]/span[2]/text()").extract_first()
            item["type"] = node.xpath("./ul/li[2]/span[2]/text()").extract_first()
            item["name_jp"] = node.xpath("./ul/li[3]/span[2]/text()").extract_first()
            item["name_cn"] = node.xpath("//*[@id='container']/div[5]/div[1]/div/h4/text()").extract_first()
            item["author"] = node.xpath("./ul/li[5]/span[2]/text()").extract_first()
            item["campany"] = node.xpath("./ul/li[6]/span[2]/text()").extract_first()
            item["play_state"] = node.xpath("./ul/li[8]/span[2]/text()").extract_first()
            item["time"] = node.xpath("./ul/li[7]/span[2]/text()").extract_first()
            item["target1"] = node.xpath("./ul/li[9]/span[2]/text()").extract_first()
            item["target2"] = node.xpath("./ul/li[10]/span[2]/text()").extract_first()
            item["link"] = node.xpath("./ul/li[11]/span[2]/text()").extract_first()
            item["detail"] = node.xpath("//*[@id='container']/div[5]/div[3]/div/div/p/text()").extract_first()
            print(item["name_cn"])
            yield item

    def start_requests(self):
        urls = []

        for i in range(2000,2023):
            for j in range(500):
                urls.append("https://www.agemys.com/detail/{}{}".format(i,format(j, '04d')))


        for url in urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return scrapy.Request(url, dont_filter=True)
