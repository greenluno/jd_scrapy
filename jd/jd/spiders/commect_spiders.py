# -*- coding: utf-8 -*-
import requests

from jd.items import commentItem
import json
import xlrd
import scrapy
from scrapy import Request


class JDCommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com']

    def parse(self, response):
        """jd"""
        url = "https://item.jd.com/1384071.html"
        yield Request(url, callback=self.parseDetails)




    def parseDetails(self, response):
        id= 1384071 # item id


        comment_num = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(id)
        com = requests.get(comment_num).text
        date = json.loads(com)
        comment_nums = date['CommentsCount'][0]['ShowCount']
        print(comment_nums)
        comment_total = int(comment_nums)
        if comment_total % 10 == 0:  # calculate the number of page, for 10 comment every page
            page = comment_total//10
        else:
            page = comment_total//10 + 1


        for k in range(page):
           #Scraping each comment page 
            com_url = 'https://sclub.jd.com/comment/productPageComments.action?productId=' + str(id) +'&score=0&sortType=5&page='+str(k)+'&pageSize=10'
            yield scrapy.Request(com_url, callback=self.parse_getCommentnum)


    def parse_getCommentnum(self, response):
        js = json.loads(response.text)
        # print(js)
        comments = js['comments']  # all comments on same page

        items = []
        for comment in comments:
            item1 = commentItem()
            item1['user_name'] = comment['nickname']  # username
            item1['user_id'] = comment['id']       #  user id
            item1['userProvince'] = comment['userProvince']  # user location
            item1['content'] = comment['content']  #  comment
            item1['good_id'] = comment['referenceId']  # item id
            item1['good_name'] = comment['referenceName']  # item name
            item1['date'] = comment['referenceTime']   # timestamp
            item1['replyCount'] = comment['replyCount']  # number of replies
            item1['score'] = comment['score']  # score
            item1['status'] = comment['status']   # status
            item1['userLevelId'] = comment['userLevelId']  # user level
            item1['productColor'] = comment['productColor']  # item color
            item1['productSize'] = comment['productSize']   # item size
            item1['userLevelName'] = comment['userLevelName']  # user status level name
            item1['isMobile'] = comment['isMobile']   # mobile indicator
            item1['userClientShow'] = comment['userClientShow']  # user client type
            item1['days'] = comment['days']  # number of day
            items.append(item1)
        return items
