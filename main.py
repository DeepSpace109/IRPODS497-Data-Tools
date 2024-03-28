import pandas as pd
import pymysql
import csv
from establishConnection import connect as cn
from utils.get.cols import cols

#Chicago_TIF capital C
"SELECT * FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"

#startup - create network connection and required cursor
conn = cn()
cursor = conn.cursor()

#startup queries
columnNames = cols(cursor)
#TODO write these names to file so as to not need to query database for this info again




#close everything off
cursor.close()
conn.commit()
conn.close()