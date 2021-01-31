import pymysql
import csv
import sys
#DONE
ip=input("İp adresi giriniz. :")
database=input("Database adı giriniz :") 
password = input("Password :") 

db_opts = {
    'user': 'root',
    'password': ('%s'%(str(password))),
    'host': ('%s'%(str(ip))),
    'database': ('%s'%(str(database)))
}
db = pymysql.connect(**db_opts)
cur = db.cursor()

def readTable():
    table = input("Çekmek istediğiniz Tablo Adını Giriniz :") 
    sql = ("SELECT * FROM (%s)"%(str(table)))
    return sql


pass#
def readTableWithCount() :
    table = input("Çekmek istediğiniz Tablo Adını Giriniz :") 
    columnName=input("Çekmek istediğiniz Column Adını Giriniz :") 
    startInt=input("kaçıncı id den sonra çekmek istersiniz sayısını giriniz. :") 
    sql = ("SELECT * FROM (%s) Where (%s)>= (%s)"%(str(table),str(columnName),startInt))
    return sql
def count() :
    table = input("istediğiniz Tablo Adını Giriniz :") 
    columnName=input("id sayısını istediğiniz Column Adını Giriniz :") 
    sql = ("SELECT Count(%s) FROM (%s) "%(str(columnName),str(table)))
    return sql

def showDb() :
    sql = "SHOW TABLES;"
    cur.execute(sql)
    myresult=cur.fetchall()
    for x in myresult:
     print(x)
    sys.exit("İşlem tamamlandı.")

operationCount = input("Database de ki Tabloları Görüntülemek İçin 1'e,\n"
"İstediğiniz bir tabloyuu direk çekmek için 2'ye,\n"
"İstediğiniz Tablonun Column sayısının Countunu öğrenmek isterseniz 3'e,\n"
"İstediğinz Tablonun İstediğiniz column sayısından itibaren çekmek isterseniz 4'e basınız.:\n"
"Menüden Çıkmak için 5'e basınız")


if int(operationCount)==1:
    showDb()
elif int(operationCount) == 2:
    sql = readTable()
    path = input("Pathini ve dosya adını giriniz. :") 
elif int(operationCount)==3: 
    sql = count()
    path = input("Pathini ve dosya adını giriniz.:") 
elif int(operationCount)==4:
    sql = readTableWithCount()
    path = input("Pathini ve dosya adını giriniz.:") 
else: print("yanlış sayı girdiniz.")

    
   

#table="customer_list"

csv_file_path = ('%s.sql'%(str(path)))
try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    db.close()

# Continue only if there are rows returned.
if rows:
    # New empty list called 'result'. This will be written to a file.
    result = list()

    # The row name is the first entry for each entity in the description tuple.
    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))