from src.python_clplot import *

print("--------------- test3 -------------")

test = pie_graph(13)

test.graphValues = [1, 2, 4, 5]
test.graphLabels = ["A", "B", "C", "D"]

test.draw_graph()