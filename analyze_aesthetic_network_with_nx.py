import json
import csv
import networkx as nx

source_file = "cari_data.json"

G = nx.Graph()

#construct the graph by iterating through the json file
with open(source_file, "r") as json_file:
    data = json.load(json_file)
    for aesthetic_category in data:
        G.add_node(aesthetic_category["ID"],name=aesthetic_category["Name"])
        for similar_aesthetic in aesthetic_category["Similar_Aesthetics"]:
            G.add_edge(aesthetic_category["ID"],similar_aesthetic)

#store the ID of isolates, then remove from the graph
isolates = list(nx.isolates(G))
G.remove_nodes_from(list(nx.isolates(G)))

# #calculate the diameter of the graph, ie the smallest path between opposite ends of the network
nx.diameter(G)

# #calculate the density of the graph, ie # of actual connections divided by # of total possible connections
nx.density(G)

# #return a list of bridges, ie edges whose removal would disconnect the graph
list(nx.bridges(G))

# #return the degree centrality for each node, ie how many edges a node has
nx.degree_centrality(G)