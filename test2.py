from src.python_clplot import *

print("--------------- test2 -------------")

test2 = Canvas(10, 10)

#test2.content.append(Center_point_circle(9, 9, 5))
#test2.content.append(Rect(1, 2, 7, 11, char="*"))

test2.content.append(Point(4, 4))
test2.content.append(Point(90, 3))

test2.draw()

print(angle_from_origin(test2.content[1].pos, test2.content[0].pos))