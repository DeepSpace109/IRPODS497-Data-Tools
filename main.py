import pandas as pd
import pymysql
import csv
from establishConnection import connect as cn

#Chicago_TIF capital C
getCols = "SHOW COLUMNS FROM Chicago_TIF;"
"SELECT * FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"

conn = cn()
cursor = conn.cursor()

cursor.execute(getCols)
results = cursor.fetchall()
cols = []
for each in results:
    cols.append(each[0])
print(cols)
cursor.close()
conn.commit()
conn.close()