import pymysql
import csv
import sys
#DONE
ip=input("İp adresi giriniz. :")
database=input("Database adı giriniz :") 
password = input("Password :") 
#mysql -u root -p --local_infile=1 kayıt atma
db_opts = {
    'user': 'root',
    'password': ('%s'%(str(password))),
    'host': ('%s'%(str(ip))),
    'database': ('%s'%(str(database))),
    
}
db = pymysql.connect(**db_opts)
cur = db.cursor()

query = """LOAD DATA [LOCAL] INFILE './cstmr.sql' INTO TABLE customer_list FIELDS TERMINATED BY ',' ENCLOSED BY '"'LINES TERMINATED BY "\n" IGNORE 1 ROWS"""

 
cur.execute(query)
rows = cur.fetchall()
    
sys.exit("No rows found for query: {}".format(sql))