import pymysql
import csv
import sys
#DONE
db_opts = {
    'user': 'root',
    'password': 'Ega.123456',
    'host': '127.0.0.1',
    'database': 'sys'
}

db = pymysql.connect(**db_opts)
cur = db.cursor()

sql = 'SELECT * FROM sys_config WHERE 1 = 1;'
ON CONFLICT
insert = "INSERT INTO sys_config(variable,value,set_time,set_by) VALUES(%s, %s, %s);" 
% ("diagnostics.allow_i_s_tables","OFF","2021-01-24 13:38:11")
csv_file_path = './out.csv'

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