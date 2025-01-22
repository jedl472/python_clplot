from src.python_clplot import *
import keyboard
import os

graph = pie_graph()

graph.filler_char = "  "

graph.graphValues = [1, 2, 4, 5]
graph.graphLabels = ["1", "2", "3", "4"]

graph.sizex = 41
graph.draw_graph()

def left_arrow(keyboard_event):
    if graph.active_part < len(graph.graphValues)-1:
        os.system("cls")
        graph.active_part += 1
        graph.draw_graph()
        
        for i in graph_ui():
            graph.content.append(i)

def right_arrow(keyboard_event):
    if graph.active_part > 0:
        os.system("cls")
        graph.active_part -= 1
        graph.draw_graph()

        for i in graph_ui():
            graph.content.append(i)

def graph_ui():
    print("Stiskněte šipky na klávesnici pro pohyb v grafu")

    return [Point(1, 1), Point(3, 1)]

keyboard.on_press_key("Left", left_arrow)
keyboard.on_press_key("Right", right_arrow)

keyboard.wait()
