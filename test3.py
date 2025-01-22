from src.python_clplot import *

print("--------------- test3 -------------")

test = pie_graph(11)

test.graphValues = [1, 2, 4, 5]
test.graphLabels = ["1", "2", "3", "4"]

test.active_part = 1

test.draw_graph()