from src.python_clplot import *

test = Canvas(20, 20)

test.add_content(Rect(1, 2, 7, 11, char="*"))
test.add_content(Center_point_circle(9, 9, 5))

test.draw()