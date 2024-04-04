import pandas as pd
import matplotlib.pyplot as plt
def makeBarGraph(table) -> None:

    xs = []
    ys = []

    for rows in table:
        xs.append(rows[0])
        ys.append(rows[1])
    
    plt.bar(xs,ys, color="blue")
    plt.show()





