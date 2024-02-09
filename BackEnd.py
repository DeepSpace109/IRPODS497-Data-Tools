import pandas as pd

class BackEnd:
    def __init__(self,filename:str):
        self.df = pd.read_csv(filename)

    def getDataTypes(self):
        return list(self.df.columns)
    
    def getDF(self):
        return self.df