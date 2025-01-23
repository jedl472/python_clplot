from src.python_clplot import *

#print("------ canvas ------")
#
#test1 = Canvas(10, 10) #x a y velikost platna
#test1.content.append(Point(7, 8, "L")) #x, y a znak
#test1.content.append(Point(8, 6, "X"))
#test1.content.append(Rect(6, 4, 1, 2)) #x, y prvniho bodu, x, y druheho bodu a znak
#test1.content.append(Rect(2, 6, 5, 9, "$"))
#test1.draw()
print("\n------ bar graph 1 ------")
test = bar_graph(2, 10) # 1. hodnota je sirka sloupcu a druha je vyska grafu
test.graphValues = [1, 2, 3, 4, 5]
test.graphLabels = ["A", "B", "C", "D", "E", "F", "Ahoj"]
test.drawGraph()
#print("\n------ bar graph 2 ------")
#test.bar_width = 1
#test.sizey = 20
#test.drawGraph()