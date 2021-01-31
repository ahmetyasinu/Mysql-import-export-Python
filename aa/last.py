import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ega.123456",
  database="sys",
  allow_local_infile=True
)

mycursor = mydb.cursor()
sql = "LOAD DATA LOCAL INFILE './cstmr.sql' INTO TABLE customer_list IGNORE 1 ROWS"


mycursor.execute(sql)

#close the connection to the database.
mydb.commit()
mydb.close()
mycursor.close()
