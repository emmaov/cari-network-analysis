# cari-network-analysis

This repository contains the Python scripts used to create and analyze a network of consumer aesthetic movements catalogued by the [Consumer Aesthetics Research Institute (CARI)](https://cari.institute/).

1. scrape_cari_to_json: This script pulls data on the aesthetic categories cataloged by CARI and stores them in a JSON file
2. transform_json_to_gexf_1-3: This script uses the etree module to transform the JSON file into a GEXF 1.3 file, an XML-format used to represent networks
3. analyze_graph_with_nx: This script uses the networkx Python library to create and analyze the aesthetic category network



