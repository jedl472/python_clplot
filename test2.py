from src.python_clplot import *

print("--------------- test2 -------------")

test2 = Canvas(40, 40)

test2.content.append(Center_point_circle(19, 19, 13, 45, 80))
test2.content.append(Center_point_circle(19, 19, 10))
#test2.content.append(Rect(1, 2, 7, 11, char="*"))


test2.draw()