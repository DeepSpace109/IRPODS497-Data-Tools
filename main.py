import pandas as pd
import pymysql
import csv
from establishConnection import connect as cn
from utils.get.cols import cols
from table.getTable import getTable as tab
from graphing.makeGraph import makeBarGraph as barGraph
from utils.get.netIncome import netIncomeByYear
from utils.support.exe import exe as ex
from utils.get.row import row

#Chicago_TIF capital C
"SELECT * FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"

#startup - create network connection and required cursor
conn = cn()
cursor = conn.cursor()

#startup queries
#TODO write these names to file so as to not need to query database for this info again

print(tab(cursor,'tif_year','cumulative_property_tax_extraction','tif_name',"35th/Halsted"))

barGraph(tab(cursor,'tif_year','cumulative_property_tax_extraction','tif_name',"35th/Halsted"))

netIncomeByYear(cursor, '35th/Halsted')

# print(ex(cursor, "SELECT DISTINCT start_year FROM Chicago_TIF WHERE tif_name = '35th/Halsted';"))

ret = row(cursor,'35th/Halsted',2021)

print(ret)






#close everything off
cursor.close()
conn.commit()
conn.close()