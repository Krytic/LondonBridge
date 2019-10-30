import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools

plt.close('all')
G = nx.Graph()

games = {0: dict()}

i = 0

with open("data/Bridgetoernooi_20191030095517", 'r') as f:
    contents = f.readlines()
    for line in contents:
        line = line.strip()
        if line == "":
            i += 1
            games[i] = dict()
            continue
        if line[0] == "%":
            continue

        if line[0] == "[":
            # data field
            field = line[1:-1] # strips square brackets
            field = field.split(" ", maxsplit=1)
            field_name = field[0]
            field_value = field[1][1:-1] # strips quotes

            games[i][field_name] = field_value

for game in games.values():
    if game != dict():
        north = game['North']
        south = game['South']
        east = game['East']
        west = game['West']

        G.add_nodes_from([north, south, east, west])
        G.add_edges_from(itertools.product([north, south, east, west], repeat=2))

nx.draw(G, node_size=6.9, with_labels=True)