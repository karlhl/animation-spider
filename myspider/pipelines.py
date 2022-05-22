# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MyspiderPipeline:
    def __init__(self):
        self.file = open('age5.csv','w',newline='',encoding='utf-8')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['其他名称','详情描述','地区', '动画种类', '原版名称','原作','制作公司','首播时间','播放状态','剧情类型','标签','官方网站'])

    def process_item(self, item, spider):
        item = dict(item)
        self.csvwriter.writerow([item["name_cn"],item["detail"],item["area"],item["type"],item["name_jp"],item["author"],item["campany"],item["time"],item["play_state"],item["target1"],item["target2"],item["link"]])

        return item

    def close_spider(self,spider):
        self.file.close()