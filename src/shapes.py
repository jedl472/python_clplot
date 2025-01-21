from .utils import *

#
# Program neprve zkontroluje, jestli je bod v bounding boxu isInBoundingBox, a pak az pocita samotnou funkci isInShape (hlavne u kruhu, odmocnina je náročná)
#

class Shape:
    def __init__(self):
        self.layer = 0
        self.visibility = 1
        id = -1

class Point(Shape):
    def __init__(self, x, y, char="#"):
        super().__init__()

        self.pos = [x, y]
        self.char = char
    
    def isInShape(self, point):
        if point == self.pos:
            return True
        
    def isInBoundingBox(self, point):
        return True


class Rect(Shape):
    def __init__(self, ax, ay, bx, by, char="#"):
        super().__init__()

        self.posa = [ax, ay]
        self.posb = [bx, by]
        self.char = char
    
    def isInShape(self, point):
        if self.posa[0] > self.posb[0]: self.posa[0], self.posb[0] = self.posb[0], self.posa[0] #kontrola, jestli neni prvni pozice vetsi nez druha
        if self.posa[1] > self.posb[1]: self.posa[1], self.posb[1] = self.posb[1], self.posa[1]

        if point[0] >= self.posa[0] and point[0] < self.posb[0]:  #samotna kontrola existence bodu v range os
            if point[1] >= self.posa[1] and point[1] < self.posb[1]:
                return True
        return False

        
    def isInBoundingBox(self, point):
        return True
    

class Center_point_circle(Shape):
    def __init__(self, x, y, size, anglea=0, angleb=360, char="#"):
        super().__init__()

        self.pos = [x, y]
        self.size = size
        self.char = char

        self.anglea = anglea
        self.angleb = angleb

    def isInShape(self, point):
        if round(distance(self.pos, point)) <= self.size:
            if self.anglea <= angle_from_origin(point, self.pos) <= self.angleb:
                return True
        return False
        
    def isInBoundingBox(self, point):
        if point[0] >= self.pos[0] - self.size and point[0] <= self.pos[0] + self.size:
            if point[1] >= self.pos[1] - self.size and point[1] <= self.pos[1] + self.size:
                return True
        return False