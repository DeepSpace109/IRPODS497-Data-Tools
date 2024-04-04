import pandas as pd
import pymysql
import csv
from establishConnection import connect as cn
from utils.get.cols import cols
from table.getTable import getTable as tab
from graphing.makeGraph import makeBarGraph as barGraph

#Chicago_TIF capital C
"SELECT * FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"

#startup - create network connection and required cursor
conn = cn()
cursor = conn.cursor()

#startup queries
columnNames = cols(cursor)
print(columnNames)
#TODO write these names to file so as to not need to query database for this info again


example = tab(cursor, "tif_year", "property_tax_extraction", "tif_name", "35th/Halsted")

barGraph(example)


#close everything off
cursor.close()
conn.commit()
conn.close()