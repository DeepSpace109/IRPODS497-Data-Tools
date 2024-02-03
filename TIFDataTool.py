
import pandas as pd 
import matplotlib.pyplot as plt


class Tools:

    def __init__(self, filename:str):
        self.df = pd.read_csv(filename)

    def getDataTypes(self):
        return list(self.df.columns)
    
    
    def visualizeYear(self, year:int, xvar:str, yvar:str):
        """
        Takes a year, a variable to display along the x-axis, a variable to display along the y-axis

        displays a plot
        returns True
        """
        relevantData = self.df[self.df['tif_year']==year]
        print(relevantData)

        xs = relevantData[xvar].tolist() 
        ys = relevantData[yvar].tolist()

        plt.scatter(xs,ys)
        plt.autoscale()
        plt.show()
        
        return True

       


