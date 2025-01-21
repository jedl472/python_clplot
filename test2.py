from src.python_clplot import *

test2 = Canvas(20, 20)

test2.add_content(Rect(1, 2, 7, 11, char="*"))
test2.add_content(Center_point_circle(9, 9, 5))

print(test2.content)
print(test2.content[0].id)
print(test2.content[1].id)

test2.content_with_id(0).visibility = 0


test2.draw()