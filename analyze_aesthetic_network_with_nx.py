import json
import csv
import networkx as nx

source_file = "cari_data.json"

G = nx.Graph()

analysis_measures_dict = {}

#construct the graph by iterating through the json file
with open(source_file, "r") as json_file:
    data = json.load(json_file)
    for aesthetic_category in data:
        G.add_node(aesthetic_category["ID"],name=aesthetic_category["Name"])
        for similar_aesthetic in aesthetic_category["Similar_Aesthetics"]:
            G.add_edge(aesthetic_category["ID"],similar_aesthetic)

#store the ID of isolates, then remove from the graph
isolate_data = {"Isolate(s)":list(nx.isolates(G))}
analysis_measures_dict.update(isolate_data)
G.remove_nodes_from(list(nx.isolates(G)))

#calculate and store various analysis measures
analysis_measures = {
    "Diameter":nx.diameter(G),
    "Density": nx.density(G),
    "Bridges": list(nx.bridges(G)),
    "Degree Centrality": nx.degree_centrality(G)
}

analysis_measures_dict.update(analysis_measures)

#dump analysis measures to json
with open("network_analysis.json", "w") as json_file:
    
    json.dump(analysis_measures,json_file)