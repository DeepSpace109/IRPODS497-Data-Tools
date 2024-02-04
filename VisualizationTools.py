import matplotlib.pyplot as plt
import numpy as np
import Utils

class VisualizationTools(Utils.Utils):
    def __init__(self, filename:str) -> None:
        super().__init__(filename)

    def moneyTypes(self):
        return ['tif_number', 'property_tax_extraction'
                , 'cumulative_property_tax_extraction'
                , 'transfers_in'
                , 'cumulative_transfers_in'
                , 'expenses'
                , 'fund_balance_end'
                , 'transfers_out'
                , 'distribution'
                , 'admin_costs'
                , 'finance_costs']

    def visualizeYear(self, year:int, xvar:str, yvar:str) -> bool:
        """
        Takes a year, a variable to display along the x-axis, a variable to display along the y-axis

        displays a plot
        returns True
        """
        relevantData = self.select('tif_year',year)

        xs = relevantData[xvar].tolist() 
        ys = relevantData[yvar].tolist()

        plt.scatter(xs,ys)
        plt.autoscale()
        plt.show()
        
        return True
    
    def plotDistrictFinancesOverTime(self, distName:str, yvar:str) -> bool:
        """
        Takes a TIF District name and displays the associated yvar values in dollars over time for as many values as are in the dataset.

        displays a plot
        returns True if given a money based item in the data frame as as the yvar,
        returns False is yvar is not a money based item (hardcoded)
        """
        if yvar not in self.moneyTypes():
            return False
        relevantData = self.select('tif_name',distName)
        xs = relevantData['tif_year'].tolist()
        ys = relevantData[yvar].tolist()

        #'${:,.2f}'.format()

        plt.bar(xs,ys)
        plt.xticks(np.arange(min(xs),max(xs)+1,step=1))
        for i, j in zip(xs,ys):
            plt.text(i,j, str('${:,.2f}'.format(j)), ha='center', va='bottom')
        plt.autoscale()
        plt.show()

    def showNetTransfers(self, distName:str) -> bool:
        #TODO transfers_in - transfers_out
        pass
