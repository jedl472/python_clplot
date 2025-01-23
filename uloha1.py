from src.python_clplot import *
import pandas as pd

df = pd.read_csv("klasifikacni_tabulka.csv") # df - data frame

prezdivky = df['Prezdivka']
scores = df['Celkem']

graph_x_size = 20

scatter = Canvas(len(scores) * 2, graph_x_size+1)

mapped_values = []

for i in scores:
    mapped_values.append(round((graph_x_size/max(scores))*i))

for i in enumerate(mapped_values):
    print(i[0]*2, i[1])
    scatter.add_content(Point(i[0]*2, i[1], char="+"))

    if i[1] < graph_x_size/2:
        scatter.add_content(Text(i[0]*2, i[1]+len(prezdivky[i[0]])+2, text=prezdivky[i[0]], orientation=1))
    else:
        scatter.add_content(Text(i[0]*2, i[1]-1, text=prezdivky[i[0]], orientation=1))



scatter.filler_char = "  "
scatter.draw(label_rangey=max(scores))

