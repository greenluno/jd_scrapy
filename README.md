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
