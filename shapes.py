from utils import *

class Point:
    def __init__(self, x, y, char="#"):
        self.pos = [x, y]
        self.char = char
    
    def render(self, canvas):
        output_canvas = canvas.copy()
        output_canvas[self.pos[1]][self.pos[0]] = self.char
        return output_canvas


class Rect:
    def __init__(self, ax, ay, bx, by, char="#"):
        self.posa = [ax, ay]
        self.posb = [bx, by]
        self.char = char

    def render(self, canvas):
        output_canvas = canvas.copy()
        for y in range(self.posa[1], self.posb[1]):
            for x in range(self.posa[0], self.posb[0]):
                output_canvas[y][x] = self.char
        return output_canvas
    
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