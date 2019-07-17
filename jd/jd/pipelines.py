# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log

SETTINGS = get_project_settings()


class CommentPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # retrieve login information in setting
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # to handle chinese character
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)  

    def __init__(self, dbpool):
        self.dbpool = dbpool


    
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self._handle_error, item, spider)
        return item


    # insert table
    def _conditional_insert(self, tx, item):

        sql = "insert into jd_comment(user_name,user_id,userProvince,content,good_id,good_name,date,replyCount,score,status,userLevelId,productColor,productSize,userLevelName,userClientShow,isMobile,days) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        params = (item["user_name"], item["user_id"], item["userProvince"], item["content"], item["good_id"],
                  item["good_name"], item["date"], item["replyCount"], item["score"], item["status"],
                  item["userLevelId"], item["productColor"], item["productSize"], item["userLevelName"],
                  item["userClientShow"],
                  item["isMobile"], item["days"])
        tx.execute(sql, params)

    # exception handling
    def _handle_error(self, failue, item, spider):
        print('--------------database operation exception!!-----------------')
        print(failue)
