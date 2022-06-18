import numpy as np
import cv2

min_x = -200
max_x = 200
dom_x = range(min_x, max_x)

min_y = -200
max_y = 200
dom_y = range(min_y, max_y)

height = max_y - min_y
width = max_x - min_x

center_y = int((min_y + max_y) / 2)
center_x = int((min_x + max_x) / 2)

def main():
    global min_x, max_x, min_y, max_y, center_y, center_x
    
    img = np.zeros(shape = (height, width, 3))
    graph = {}
    
    for i in dom_y:
        for j in dom_x:
            pos = (i, j)
            
            graph[pos] = 1
    
    seps = { 
        "00": { "w": np.array([ 0, 1 ]), "b": 0 },
        "01": { "w": np.array([ -1, 1 ]), "b": 100 },
        "10": { "w": np.array([ 0.9, 1 ]), "b": -100 }
    }
    
    fill_graph(graph, seps)
    
    draw_separator(graph, seps["00"])
    draw_separator(graph, seps["01"])
    
    graph[(0, 0)] = (0, 0, 1)
    draw_graph(img, graph)
    
    cv2.imshow("test", img)
    cv2.waitKey(0)

def fill_graph(graph, seps):
    global dom_y, dom_x
    
    for i in dom_y:
        for j in dom_x:
            pos = (i, j)
            
            sep00 = seps["00"]
            sep01 = seps["01"]
            sep10 = seps["10"]
            
            d0 = calc_sep(sep00["w"], sep00["b"], pos)
            d1 = calc_sep(sep01["w"], sep01["b"], pos)
            
            relu = (max(0, d0), max(0, d1))
            
            d_f = calc_sep(sep10["w"], sep10["b"], relu)
            
            if (i, j) == (50, 0):
                
                print(d_f, relu, sep00, sep01, sep10)
            
            if d_f < 0:
                graph[pos] = (1, 0.7, 0.5)
            else:
                graph[pos] = (0.8, 1, 0.8)

def draw_separator(graph, sep):
    global min_y, max_y, min_x, max_x, center_x

    w = sep["w"]
    b = sep["b"]

    if w[0] != 0:
        start = (int(calc_y(w, b, min_x)), min_x)
        end = (int(calc_y(w, b, max_x)), max_x)
    else:
        start = (min_y, b)
        end = (max_y, b)

    draw_line(graph, start, end)
    
    start = np.array((int(calc_y(w, b, center_x)), center_x))
    
    unit_w = w / np.linalg.norm(w)
    end = start + (unit_w * 20)
    
    draw_line(graph, start, end)
        
def draw_line(graph, start, end):
    global min_y, max_y, dom_y
    
    if end[1] == start[1]:
        if end[0] < start[0]:
            temp = end
            end = start
            start = temp

        for i in range(int(start[0]), int(end[0])):
            if i < min_y or i >= max_y:
                continue
            
            pos = (i, end[1])
            graph[pos] = (0, 0, 0)
            
        return
    
    m = end[0] - start[0]
    m = m / (end[1] - start[1])
    b = start[0] - (m * start[1])
    
    d = end[1] - start[1]
    d = round(d / abs(d))
    
    for j in range(int(start[1]), int(end[1]), d):
        i = (m * j) + b
        
        if i < min_y or i >= max_y:
            continue
        
        pos = (i, j)
        graph[pos] = (0, 0, 0)
    
def calc_sep(w, b, x):
    return (w[0] * x[0]) + (w[1] * x[1]) + b
    
def calc_y(w, b, x):
    if w[0] == 0:
        return b
    
    return ((w[1] * x) + b) / -w[0]

def draw_graph(img, graph):
    global dom_x, dom_y, min_y, min_x
    
    for i in dom_y:
        for j in dom_x:
            pos = (i, j)
            mapped_y = height - (i - min_y) - 1
            mapped_x = j - min_x
            
            img[mapped_y, mapped_x] = graph[pos]
            
            

main()