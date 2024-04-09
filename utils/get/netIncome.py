import pymysql
from table.getTable import getTable
from graphing.makeGraph import makeBarGraph as bg

def netIncomeByYear(cursor, tifname):

    tab = getTable(cursor,'tif_year','property_tax_extraction','tif_name',tifname)
    
    alteredTab = []
    for idx in range(1,len(tab)):
        alteredTab.append([tab[idx][0],(tab[idx][1]-tab[idx-1][1])])

    bg(alteredTab,"Years after first year " + str(tab[0][0]), "Change in end of year balance since start year")