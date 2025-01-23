from src.python_clplot import *
import keyboard
import os
import pandas as pd

graph = pie_graph()

graph.filler_char = "  "
graph.graphpos = [14, 16]
graph.graph_diameter = 9
graph.active_part = 0

graph.graphValues = [0, 0, 0, 0, 0]
graph_meta = [[], [], [], [], []]

df = pd.read_csv("klasifikacni_tabulka.csv") # df - data frame

x_values = df['Prezdivka']
y_values = df['Znamka']

for i in enumerate(y_values):
    graph.graphValues[int(i[1])-1] += 1
    graph_meta[int(i[1])-1].append(x_values[i[0]])


graph.sizex = 47

def left_arrow(keyboard_event):
    if graph.active_part < len(graph.graphValues)-1:
        os.system("cls")
        graph.active_part += 1
        
        for i in graph_ui():
            graph.content.append(i)

        graph.draw_graph()

def right_arrow(keyboard_event):
    if graph.active_part > 0:
        os.system("cls")
        graph.active_part -= 1

        for i in graph_ui():
            graph.add_content(i)

        graph.draw_graph()

def graph_ui():
    ui = []
    ui.append(Text(1, 1, "Stiskněte šipky na klávesnici pro pohyb v grafu"))
    ui.append(Rect(30, 1, 45, 29, char="+"))
    ui.append(Rect(31, 2, 44, 28, char=" ", layer=1))

    ui.append(Text(33, 26, text="Známka: " + graph.graphLabels[graph.active_part], layer=2))
    ui.append(Text(32, 24, text="---------------------", layer=2))

    for i in enumerate(graph_meta[graph.active_part]):
        ui.append(Text(32, 22-i[0], text=i[1], layer=2))

    return ui

keyboard.on_press_key("Left", left_arrow)
keyboard.on_press_key("Right", right_arrow)

left_arrow("")

keyboard.wait()
