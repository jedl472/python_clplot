class Point:
    def __init__(self, x, y, char="#"):
        self.pos = [x, y]
        self.char = char

class Rect:
    def __init__(self, ax, ay, bx, by, char="#"):
        self.posa = [ax, ay]
        self.posb = [bx, by]
        self.char = char

class Canvas:
    def __init__(self, sizex = 10, sizey = 10):
        self.sizex = sizex
        self.sizey = sizey

        self.content = []
    
    def draw(self, label_rangey=-1, filler_char=". "): #TODO optimalizovat aby se nemusel vytvářet list o velikosti canvas
        canvas_to_print = []
        for i in range(self.sizey): canvas_to_print.append(([filler_char[0]] * self.sizex).copy())

        for i in self.content: #zapsání obsahu self.content do canvas_to_print
            if isinstance(i, Point):
                canvas_to_print[i.pos[1]][i.pos[0]] = i.char
            
            elif isinstance(i, Rect):
                for y in range(i.posa[1], i.posb[1]):   
                    for x in range(i.posa[0], i.posb[0]):   
                        canvas_to_print[y][x] = i.char


        for y in range(self.sizey): #vytištění do konzole (přehodí osu y tak, aby byl origin vlevo dole)
            row_to_print = ""

            if label_rangey != -1:  # vertikalni labely se tisknou, pokud se label_rangey != -1, defaultně vypnuto
                row_label_value = str(round((label_rangey+1)-((label_rangey+1)*(y/self.sizey)))-1)
                row_to_print = (row_label_value + " " * (len(str(label_rangey)) - len(row_label_value)) + "| ")

            for x in range(self.sizex):
                row_to_print += canvas_to_print[self.sizey-y-1][x] + filler_char[1:]
            print(row_to_print)

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