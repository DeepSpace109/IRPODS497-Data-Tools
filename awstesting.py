import pymysql
import sys
import boto3
import os
import mysql.connector
from mysql.connector import Error
import csv
import json

#import secure read-only credentials to the database.
with open('awscreds.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in spamreader:
        creds = (row)

try:
    conn = pymysql.connect(
        host=creds[0],
        user=creds[1],
        password=creds[2],
        database="chicago_TIF"
    )   
except pymysql.Error as e:
    print(e)

#Chicago_TIF capital C
sql = "describe Chicago_TIF;"
cursor = conn.cursor()
cursor.execute(sql)
results = cursor.fetchall()
print(results)
cursor.close()
conn.commit()
conn.close()




