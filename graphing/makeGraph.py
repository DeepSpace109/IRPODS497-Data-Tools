import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def makeBarGraph(table,xname="",yname="") -> None:

    x = []
    y = []

    for rows in table:
        x.append(rows[0])
        y.append(rows[1])
    
    plt.bar(x,y, color="blue")
    plt.xlabel(xname)
    plt.ylabel(yname)

    plt.show()





