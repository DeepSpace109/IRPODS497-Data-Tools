import pandas as pd
import TIFDataTool
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

tool = TIFDataTool.Tools('master_TIF_UPDATED.csv')

df = tool.getDF()
df = df.drop(['tif_name','bank'], axis=1)

features = ['property_tax_extraction', 
            'cumulative_property_tax_extraction', 
            'transfers_in', 
            'cumulative_transfers_in', 
            'expenses', 
            'fund_balance_end', 
            'transfers_out', 
            'distribution', 
            'finance_costs']
xs = df.loc[:, features]
ys = df.loc[:,['admin_costs']].values
df = StandardScaler().fit_transform(xs)

pca = PCA(n_components=3)
pca.fit(df)
print(pca.components_[:][0])
print(pca.components_[:][1])
print(pca.components_[:][2])

