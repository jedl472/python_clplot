from .shapes import *
from .utils import *

class Canvas:
    def __init__(self, sizex = 10, sizey = 10):
        self.sizex = sizex
        self.sizey = sizey

        self.content = []

        self.filler_char = ". "

    def draw(self, label_rangey=-1):
        for y in range(self.sizey-1, -1, -1):
            row_to_print = ""
            text_buffer = []

            if label_rangey != -1:  # vertikalni labely se tisknou, pokud se label_rangey != -1, defaultně vypnuto
                row_label_value = str(round((label_rangey+1)-((label_rangey+1)*((self.sizey - y)/self.sizey)))-1)
                row_to_print = (row_label_value + " " * (len(str(label_rangey)) - len(row_label_value)) + "| ")

            for x in range(self.sizex):
                pixel_buffer = []

                for i in self.content:
                    if i.visibility == 1:
                        if i.isInBoundingBox([x, y]):
                            if i.isInShape([x, y]):
                                if not isinstance(i, Text) or i.orientation == 1:
                                    pixel_buffer.append(i)
                                else:
                                    text_buffer = i.text
                
                if len(text_buffer) > 0: #jako důsledek se text vždy renderuje v popředí TODO: zprovoznit vrstvy u textu
                    text_to_add = (text_buffer[:(len(self.filler_char))])
                    if len(text_to_add) != len(self.filler_char): text_to_add += " " * (len(self.filler_char) - len(text_to_add)) #doplní string na požadovanou délku buňky
                    row_to_print += text_to_add
                    text_buffer = text_buffer[(len(self.filler_char)):]
                elif len(pixel_buffer) > 0: #v pixel_buffer jsou věci uložené kvůli vrstvám
                    top_layer_shape = max(pixel_buffer, key=lambda obj: obj.layer)
                    row_to_print += top_layer_shape.char + self.filler_char[1:]
                else:
                    row_to_print += self.filler_char
            
            print(row_to_print)
        
    def content_with_id(self, id):
        for i in self.content:
            if id == i.id:
                return i
    
    def add_content(self, content):
        if len(self.content) == 0:
            content.id = 0
        else:
            content.id = self.content.copy().pop().id + 1
        
        self.content.append(content)

        

class bar_graph(Canvas):
    def __init__(self, bar_width=2, max_bar_height=10):
        self.sizex = 0
        self.sizey = max_bar_height

        self.bar_width = bar_width

        self.content = []

        self.graphValues = []
        self.graphLabels = []
    
    def drawGraph(self):
        max_value = max(self.graphValues)
        mapped_values = []

        for i in enumerate(self.graphValues):
            bar_height = round((i[1]/max_value)*self.sizey)
            bar_originx = i[0]*(self.bar_width+1)
            bar = Rect(bar_originx, 0, bar_originx+self.bar_width, bar_height)
            self.content.append(bar)

        self.sizex = ((self.bar_width+1) * len(self.graphValues))-1

        self.draw(label_rangey=max_value, filler_char=" ")

        self.content = []

        labels_to_print = " " * (len(str(max_value))+2)
        for i in self.graphLabels: # ----------------------------------- tisk horizontalnich labelu
            labels_to_print += str(i[:self.bar_width]) + (self.bar_width - len(str(i[:self.bar_width]))) * " " + " "

        print(labels_to_print)

class pie_graph(Canvas):
    def __init__(self):
        Canvas.__init__(self)

        self.sizex = 30
        self.sizey = 30

        self.graphpos = [15, 15]

        self.graph_diameter = 10
        self.active_part = -1

        self.content = []

        self.graphValues = []
        self.graphLabels = ["1", "2", "3", "4", "5"]

    def draw_graph(self):
        mapped_values = []
        graph_sum = sum(self.graphValues)

        for i in enumerate(self.graphValues):
            mapped_values.append((360/graph_sum)*i[1])

        mapped_values.append(360)


        generator_angle = 0
        for i in enumerate(mapped_values[:-1]):
            section_diameter = self.graph_diameter
            if i[0] == self.active_part:
                section_diameter += 3
            self.content.append(Center_point_circle(self.graphpos[0], self.graphpos[1], section_diameter, generator_angle, generator_angle+i[1], char=self.graphLabels[i[0]]))
            generator_angle += i[1]
        #print(mapped_values)

        self.draw()

        self.content = []





if __name__ == "__main__":
    print("Running library not test!")