# cari-network-analysis

This repository contains the Python scripts used to create and analyze a network of consumer aesthetic movements for my final project for INFO664 Programming for Cultural Heritage. My data source is the [Consumer Aesthetics Research Institute (CARI)](https://cari.institute/), a collective of researchers and designers who catalog “consumer aesthetics” from the mid-20th century to the present. CARI defines a “consumer aesthetic” as “a visual movement unified by overarching attitudes and themes that survived long enough or became popular enough to be appropriated by capital”; this relationship between culture, capital, and visual artifacts can deepen our understanding of social and economic events. CARI’s web catalogue contains pages for nearly 100 aesthetic categories, each with an approximate date range, description, gallery, and related aesthetics. By visualizing these aesthetic categories as a network, I hope to be able to identify aesthetic categories that are important for linking disparate movements and time periods. 

This project contains several scripts:

1. scrape_cari_to_json: This script pulls data on the aesthetic categories cataloged by CARI and stores them in a JSON file. Although CARI does not have a documented public API, their catalog is powered by a hidden API. I discovered this by loading the catalog page and watching the network traffic using Chrome DevTools. The Aesthetic Categories page (”the catalog”) makes an XHR request to the Are.na API, an online software for saving and organizing content that CARI uses to organize aesthetics research. The individual aesthetic pages make an XHR request to the Are.na API as well as the CARI API. The Are.na API is used to get images of the given aesthetic, while the CARI API gets information like the aesthetic name, description, dates, and related aesthetics.
2. transform_json_to_gexf_1-3: This script uses the etree module to transform the JSON file into a GEXF 1.3 file, an XML-format used to represent networks.
3. analyze_graph_with_nx: This script uses the networkx Python library to create and analyze the aesthetic category network. Networkx does not support the current version of GEXF files, so this script also creates a simplified node and edge list for use in the networkx analysis.

The final portion of this project will be an interactive network visualization generated with Gephi as well as a complete write up of my process and findings.


