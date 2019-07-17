import scrapy

class commentItem(scrapy.Item):
    user_name = scrapy.Field()   
    user_id = scrapy.Field()  
    userProvince = scrapy.Field()  
    content = scrapy.Field()  
    good_id = scrapy.Field()  
    good_name = scrapy.Field()  
    date = scrapy.Field()   
    replyCount = scrapy.Field()   
    score = scrapy.Field()  
    status = scrapy.Field()  
    userLevelId = scrapy.Field()  
    productColor = scrapy.Field()  
    productSize = scrapy.Field()  
    userLevelName = scrapy.Field()   
    userClientShow = scrapy.Field()   
    isMobile = scrapy.Field()  
    days = scrapy.Field()  
    
