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
    'local_infile': 1
}
db = pymysql.connect(**db_opts)
cur = db.cursor()
fileUpload=input("Yüklenecek olan dosya Pathini giriniz.:\n")
tableName=input("Üzerine kayıt atılacak tablo adını giriniz.")
sql = ("""LOAD DATA LOCAL INFILE '%s.sql' INTO TABLE %s FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY "\r\n" IGNORE 1 LINES"""%(str(fileUpload),str(tableName)))

 
try:
    cur.execute(sql)
    db.commit()
    print("işlem Başarılı")
    cur.close()
finally:
    db.close()
