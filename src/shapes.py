from .utils import *

#
# Program neprve zkontroluje, jestli je bod v bounding boxu isInBoundingBox, a pak az pocita samotnou funkci isInShape (hlavne u kruhu, odmocnina je náročná)
#

class Point:
    def __init__(self, x, y, char="#"):
        self.pos = [x, y]
        self.char = char
    
    def isInShape(self, point):
        if point == self.pos:
            return True
        
    def isInBoundingBox(self, point):
        return True


class Rect:
    def __init__(self, ax, ay, bx, by, char="#"):
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
    

class Center_point_circle:
    def __init__(self, x, y, size, char="#"):
        self.pos = [x, y]
        self.size = size
        self.char = char

    def render(self, canvas):
        output_canvas = canvas.copy()
        for y in range(len(output_canvas)):
            for x in range(len(output_canvas[y])):
                if round(distance(self.pos, [x, y])) <= self.size: output_canvas[x][y] = self.char
        return canvas

    def isInShape(self, point):
        if round(distance(self.pos, point)) <= self.size: 
            return True
        else:
            return False
        
    def isInBoundingBox(self, point):
        if point[0] >= self.pos[0] - self.size and point[0] <= self.pos[0] + self.size:
            if point[1] >= self.pos[1] - self.size and point[1] <= self.pos[1] + self.size:
                return True