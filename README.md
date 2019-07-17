# Instructions

EC2 server address: ec2-18-139-110-175.ap-southeast-1.compute.amazonaws.com

username: ubuntu

keyfile: key.ppk

==========================================================

RDS server address: database-1.c5lbvtpvjhci.ap-southeast-1.rds.amazonaws.com

username: admin

password: password

database name: jd

table name: jd_comment


# Procudures

1. Login aws ec2 server using login information above.

2. Execute : cd /home/ubuntu/scrapy/jd/jd

3. Execute : scrapy crawl comment 

4. Login RDS server using mySQL client: mysql -h database-1.c5lbvtpvjhci.ap-southeast-1.rds.amazonaws.com -P 3306 -u admin -p

5. Execute SQL command : select * from jd_comment;
   to view the result.
# Principle

1. The objective of this prototype is to extract comment data from one JD product page.

2. As the comment details on JD are store in JS, the url containing such data could be found using Network Inspect.

3. Firstly scrapy will scrap the number of comment from productCommentSummaries.

4. It will then calculate the number of comment page, by number of page = number of comment / 10 , as number of comment shown per page is 10. If there are any remainder add 1 page to the result.

5. Loop through the productPageComments 1 by 1 to scrap the comments data.

6. Use scrapy pipeline to insert the rows into database. The data should be roughly cleaned and ready for next steps.

