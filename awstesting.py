import pymysql
import csv

#import secure read-only credentials to the database.
#MUST HAVE awscreds.csv EXISTING WITH VALID CREDENTIALS
with open('awscreds.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        creds = (row)

#establish connection to DB and create cursor.
try:
    conn = pymysql.connect(
        host=creds[0],
        user=creds[1],
        password=creds[2],
        database="chicago_TIF"
    )
    cursor = conn.cursor()
except pymysql.Error as e:
    print(e)

#Chicago_TIF capital C
sql = "SHOW COLUMNS FROM Chicago;"
"SELECT * FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"

cursor.execute(sql)
results = cursor.fetchall()
print(results)
cursor.close()
conn.commit()
conn.close()




