import pandas as pd
import random as rnd
import time as time
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from math import *


rnd.seed(time.time())

nodes = [
            [1, 2, 17],
            [3, 2],
            [4],
            [5],
            [5, 9],
            [7],
            [9, 7],
            [8],
            [9, 12],
            [11],
            [11, 14],
            [13],
            [13],
            [14, 15],
            [17],
            [16],
            [19, 17],
            [19, 18],
            [19],
            []
]

reliability = [
            [0.95, 0.95, 0.95],
            [0.95, 0.95],
            [0.95],
            [0.95],
            [0.95, 0.95],
            [0.95],
            [0.95, 0.95],
            [0.95],
            [0.95, 0.95],
            [0.95],
            [0.95, 0.95],
            [0.95],
            [0.95],
            [0.95, 0.95],
            [0.95],
            [0.95],
            [0.95, 0.95],
            [0.95, 0.95],
            [0.95],
            []
    
]
capacity = [
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
            
]

intensity = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



flow = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

avgSize = 15000

for i in range(len(capacity)):
    for j in range(len(capacity[i])):
            capacity[i][j] = 100000000
            intensity[i][j] = 120
            if(i == j):
                intensity[i][j] = 0



delayMax = 0.1

G = nx.Graph()

for i in range(20):
    G.add_node(i)

index = 0
for edges in nodes:
    for edge in edges:
        G.add_edge(index, edge, weight=1)
    index += 1
    
print nx.info(G)
G.to_undirected()
print nx.is_directed(G)

#nx.draw(G)
#plt.show()

# +1
# ustalony przeplyw danych 
#
print("Ustalony przeplyw danych")
print("\nNetwork #1")
increases = 100
m = 1000
for inc in range(increases):
    
    falisPath = 0
    failsOverflow = 0
    failsTimeout = 0
    success = 0.0
    percent = 0.0
    for t in range(m):
        
        H = nx.Graph()

        for i in range(20):
            H.add_node(i)

        index = 0
        for edges in nodes:
            for edge in edges:
                H.add_edge(index, edge, weight=1)
            index += 1

        for i in range(len(flow)):
            for j in range(len(flow[i])):
                flow[i][j] = 0

        for i in range(len(intensity)):
            for j in range(len(intensity[i])):
                intensity[i][j] = 1 + rnd.randrange(1, 2)
                if(i == j):
                    intensity[i][j] = 0
        
        for edges in range(len(nodes)):
            for edge in range(len(nodes[edges])):
                rand = rnd.random()
                if(reliability[edges][edge] <= rand):
                    H.remove_edge(edges, nodes[edges][edge])
        
        ok = 1

        for i in range(20):
            for j in range(20):
                if(intensity[i][j] != 0):
                    if(nx.has_path(H, i, j)):
                        path = nx.shortest_path(H,i, j)
                        for el in range (len(path)-1):
                            flow[path[el]][path[el+1]] += intensity[path[el]][path[el+1]]
                    else:
                        if(ok == 1):
                            falisPath += 1
                        ok = 0
                    
        if(ok == 1):
            for i in range(20):
                for j in range(20):
                    if(flow[i][j]*avgSize > capacity[i][j]):
                        #print("ERROR!")
                        #print(str(i) + " " + str(j) + " actual:" + str(flow[i][j]) + " max:" + str(capacity[i][j]))
                        if(ok == 1):
                            #print(flow[i][j], capacity[i][j])
                            failsOverflow += 1
                        ok = 0

        if(ok == 1):
            delay = 0.0
            G = 0.0
            sum_e = 0.0
            c = 0.0
            a = 0.0

            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        G += intensity[i][j]
                        
            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        a = flow[i][j]
                        c = capacity[i][j]
                        tmp = 1.0*c/(1.0*avgSize)
                        tmp -= 1.0*a
                        sum_e += 1.0*a/(1.0*tmp)
                        #print(a, c, sum_e, a/(c/avgSize - a))

            
            delay = sum_e/G  
            
            if(delay > delayMax):
                if(ok == 1):
                    failsTimeout += 1
                ok = 0

        success += ok
    percent = success*100/m
    print(str(percent) + ";" + str(falisPath*100.0/m) + ";" + str(failsOverflow*100.0/m) + ";" + str(failsTimeout*100.0/m))

#    
#
#    


print("\n")

# +1
# zmiekszamy ilosc danych ---------------------------------------------------------------------------------------------------------------------------------
#
print("\nZwiekszane natezenie")
print("\nNetwork #2")

for i in range(len(capacity)):
    for j in range(len(capacity[i])):
            capacity[i][j] = 100000000
            intensity[i][j] = 120
            if(i == j):
                intensity[i][j] = 0

for inc in range(increases):
    falisPath = 0
    failsOverflow = 0
    failsTimeout = 0
    success = 0.0

    for i in range(len(intensity)):
            for j in range(len(intensity[i])):
                intensity[i][j] += rnd.randrange(0, 2)
                if(i == j):
                    intensity[i][j] = 0

    for t in range(m):
        
        H = nx.Graph()

        for i in range(20):
            H.add_node(i)

        index = 0
        for edges in nodes:
            for edge in edges:
                H.add_edge(index, edge, weight=1)
            index += 1

        for edges in range(len(nodes)):
            for edge in range(len(nodes[edges])):
                rand = rnd.random()
                if(reliability[edges][edge] <= rand):
                    H.remove_edge(edges, nodes[edges][edge])

        for i in range(len(flow)):
            for j in range(len(flow[i])):
                flow[i][j] = 0

        ok = 1

        for i in range(20):
            for j in range(20):
                if(intensity[i][j] != 0):
                    if(nx.has_path(H, i, j)):
                        path = nx.shortest_path(H,i, j)
                        for el in range (len(path)-1):
                            flow[path[el]][path[el+1]] += intensity[path[el]][path[el+1]]
                    else:
                        if(ok == 1):
                            falisPath += 1
                        ok = 0
                    
        if(ok == 1):
            for i in range(20):
                for j in range(20):
                    if(flow[i][j]*avgSize >= capacity[i][j]):
                        #print("ERROR!")
                        #print(str(i) + " " + str(j) + " actual:" + str(flow[i][j]) + " max:" + str(capacity[i][j]))
                        if(ok == 1):
                            #print(flow[i][j], capacity[i][j])
                            failsOverflow += 1
                        ok = 0

        if(ok == 1):
            delay = 0.0
            G = 0.0
            sum_e = 0.0
            c = 0.0
            a = 0.0

            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        G += intensity[i][j]
                        
            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        a = flow[i][j]
                        c = capacity[i][j]
                        tmp = 1.0*c/(1.0*avgSize)
                        tmp -= 1.0*a
                        sum_e += 1.0*a/(1.0*tmp)
                        #print(a, c, sum_e, a/(c/avgSize - a))

            
            delay = sum_e/G  
            if(delay < 0):
                print("less than zero")
            if(delay > delayMax):
                if(ok == 1):
                    failsTimeout += 1
                ok = 0

        success += ok

    percent = success*100/m
    print(str(percent) + ";" + str(falisPath*100.0/m) + ";" + str(failsOverflow*100.0/m) + ";" + str(failsTimeout*100.0/m))





#
# zmiekszamy przepustowosc ---------------------------------------------------------------------------------------------------------------------------------
#
for i in range(len(capacity)):
    for j in range(len(capacity[i])):
            capacity[i][j] = 100000000
            intensity[i][j] = 120
            if(i == j):
                intensity[i][j] = 0
print("\nZwiekszane przepustowosc")
print("\nNetwork #3")

for inc in range(increases):
    falisPath = 0
    failsOverflow = 0
    failsTimeout = 0
    success = 0.0

    for i in range(len(capacity)):
            for j in range(len(capacity[i])):
                capacity[i][j] += capacity[i][j]/100
                
    for t in range(m):
        
        H = nx.Graph()

        for i in range(20):
            H.add_node(i)

        index = 0
        for edges in nodes:
            for edge in edges:
                H.add_edge(index, edge, weight=1)
            index += 1

        for i in range(len(flow)):
            for j in range(len(flow[i])):
                flow[i][j] = 0

        for edges in range(len(nodes)):
            for edge in range(len(nodes[edges])):
                rand = rnd.random()
                if(reliability[edges][edge] <= rand):
                    H.remove_edge(edges, nodes[edges][edge])
        
        

        ok = 1

        for i in range(20):
            for j in range(20):
                if(intensity[i][j] != 0):
                    if(nx.has_path(H, i, j)):
                        path = nx.shortest_path(H,i, j)
                        for el in range (len(path)-1):
                            flow[path[el]][path[el+1]] += intensity[path[el]][path[el+1]]
                    else:
                        if(ok == 1):
                            falisPath += 1
                        ok = 0
                    
        if(ok == 1):
            for i in range(20):
                for j in range(20):
                    if(flow[i][j]*avgSize > capacity[i][j]):
                        #print("ERROR!")
                        #print(str(i) + " " + str(j) + " actual:" + str(flow[i][j]) + " max:" + str(capacity[i][j]))
                        if(ok == 1):
                            #print(flow[i][j], capacity[i][j])
                            failsOverflow += 1
                        ok = 0

        if(ok == 1):
            delay = 0.0
            G = 0.0
            sum_e = 0.0
            c = 0.0
            a = 0.0

            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        G += intensity[i][j]
                        
            for i in range(len(nodes)):
                for j in nodes[i]:
                    if(H.has_edge(i, j)):
                        a = flow[i][j]
                        c = capacity[i][j]
                        tmp = 1.0*c/(1.0*avgSize)
                        tmp -= 1.0*a
                        sum_e += 1.0*a/(1.0*tmp)
                        #print(a, c, sum_e, a/(c/avgSize - a))

            
            delay = sum_e/G  
            if(delay < 0):
                print("less than zero")
            if(delay > delayMax):
                if(ok == 1):
                    failsTimeout += 1
                ok = 0

        success += ok
    percent = success*100/m
    print(str(percent) + ";" + str(falisPath*100.0/m) + ";" + str(failsOverflow*100.0/m) + ";" + str(failsTimeout*100.0/m))




#
# dodajemy krawedzie ---------------------------------------------------------------------------------------------------------------------------------
#
edg = 29
for inc in range(increases):

    falisPath = 0
    failsOverflow = 0
    failsTimeout = 0
    success = 0.0
    
    B = nx.Graph()

    for i in range(20):
        B.add_node(i)

    index = 0
    for edges in nodes:
        for edge in edges:
            B.add_edge(index, edge, weight=1)
        index += 1

    added = 0

    while (added < inc):
        rand1 = rnd.randrange(0, 19)
        rand2 = rnd.randrange(0, 19)
        if(rand1 != rand2 and not B.has_edge(rand1, rand2)):
            B.add_edge(rand1, rand2)
            added += 1

    edg+=1

    for t in range(m):
        
        H = nx.Graph()
        H = B.copy()

        for i in range(len(flow)):
            for j in range(len(flow[i])):
                flow[i][j] = 0

        for i in range(20):
            for j in range(20):
                if(H.has_edge(i, j)):
                    rand = rnd.random()
                    if(0.95<= rand):
                        H.remove_edge(i, j)
       
        ok = 1

        for i in range(20):
            for j in range(20):
                if(intensity[i][j] != 0):
                    if(nx.has_path(H, i, j)):
                        path = nx.shortest_path(H,i, j)
                        for el in range (len(path)-1):
                            flow[path[el]][path[el+1]] += intensity[path[el]][path[el+1]]
                    else:
                        if(ok == 1):
                            falisPath += 1
                        ok = 0
                    
        if(ok == 1):
            for i in range(20):
                for j in range(20):
                    if(flow[i][j]*avgSize > capacity[i][j]):
                        #print("ERROR!")
                        #print(str(i) + " " + str(j) + " actual:" + str(flow[i][j]) + " max:" + str(capacity[i][j]))
                        if(ok == 1):
                            #print(flow[i][j], capacity[i][j])
                            failsOverflow += 1
                        ok = 0

        if(ok == 1):
            delay = 0.0
            G = 0.0
            sum_e = 0.0
            c = 0.0
            a = 0.0

            for i in range(20):
                for j in range(20):
                    if(H.has_edge(i, j)):
                        G += intensity[i][j]
                        
            for i in range(20):
                for j in range(20):
                    if(H.has_edge(i, j)):
                        a = flow[i][j]
                        c = capacity[i][j]
                        tmp = 1.0*c/(1.0*avgSize)
                        tmp -= 1.0*a
                        sum_e += 1.0*a/(1.0*tmp)
                        #print(a, c, sum_e, a/(c/avgSize - a))

            
            delay = sum_e/G  
            if(delay > delayMax):
                if(ok == 1):
                    failsTimeout += 1
                ok = 0

        success += ok

    percent = success*100/m
    print(str(percent) + ";" + str(falisPath*100.0/m) + ";" + str(failsOverflow*100.0/m) + ";" + str(failsTimeout*100.0/m))
