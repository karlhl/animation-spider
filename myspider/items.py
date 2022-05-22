# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:

    # 地区
    area = scrapy.Field()
    # 动画种类
    type = scrapy.Field()
    # 原版名称
    name_jp = scrapy.Field()
    # 其他名称
    name_cn = scrapy.Field()
    # 原作
    author = scrapy.Field()
    # 制作公司
    campany = scrapy.Field()
    # 播放状态
    play_state = scrapy.Field()
    # 首播时间
    time = scrapy.Field()
    # 剧情类型
    target1 = scrapy.Field()
    # 标签
    target2 = scrapy.Field()
    # 官方网站
    link = scrapy.Field()
    # 详情介绍
    detail = scrapy.Field()
