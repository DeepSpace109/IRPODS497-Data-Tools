import pymysql
import sys
import boto3
import os

#declare connection variables
ENDPOINT="the url to the database which can be found in the aws dashboard"
PORT="3306"
USER="Stock_John"
REGION="us-east-1"
DBNAME="do i need to have the correct name?"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#establish session
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn = pymysql.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""DESCRIBE table_name """)
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))


