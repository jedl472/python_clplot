from src.python_clplot import *
import pandas as pd

df = pd.read_csv("klasifikacni_tabulka.csv") # df - data frame

frames = list(df.columns)[4:]

bgraph = bar_graph(4, 20)

for i in frames:
    bgraph.graphValues.append(df[i].fillna(0).max().astype(int).item())

bgraph.graphLabels = frames


print("Maximální skore dosažené v úlohách:")
bgraph.drawGraph()