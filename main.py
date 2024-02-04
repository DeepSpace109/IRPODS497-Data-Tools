import pandas as pd
import TIFDataTool

tool = TIFDataTool.Tools('master_TIF_UPDATED.csv')


# tool.visualizeYear(2020, "tif_name", "property_tax_extraction")

print(tool.getDataTypes())
tool.plotDistrictFinancesOverTime("Cortland/Chicago River", "transfers_in")