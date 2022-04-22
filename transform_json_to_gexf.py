import json 
from xml.etree.ElementTree import Element, SubElement, ElementTree

source_file = "cari_data.json"

#build out the xml tree

root = Element("gexf",xmnls="http://gexf.net/1.3",version="1.3")

graph_element = SubElement(root,"graph",mode="static",defaultedgetype="undirected")

attributes_element = SubElement(graph_element,"attributes")

nodes_element = SubElement(graph_element,"nodes")

edges_element = SubElement(graph_element,"edges")

descriptions_element = SubElement(attributes_element,"attribute",id="0",title="description",type="string")

start_years_element = SubElement(attributes_element,"attribute",id="1",title="start year",type="string")

end_years_element = SubElement(attributes_element,"attribute",id="2",title="end year",type="string")

urls_element = SubElement(attributes_element,"attribute",id="3",title="url",type="string")

#set attributes for attributes element here, otherwise interferes with adding subelements
attributes_element.set("class","nodes")

with open(source_file,"r") as json_file:

    data = json.load(json_file)

    for aesthetic_category in data:

        #loop through aesthetic categories, create nodes, and add attributes
        aesthetic_id = str(aesthetic_category["ID"])
        aesthetic_name = aesthetic_category["Name"]
        aesthetic_description = aesthetic_category["Description"]
        aesthetic_start_year = aesthetic_category["Start_Year"]
        aesthetic_url = aesthetic_category["Link"]

        node_element = SubElement(nodes_element,"node",id=aesthetic_id,label=aesthetic_name)

        att_values_element = SubElement(node_element,"attvalues")

        description_element = SubElement(att_values_element,"attvalue",value=aesthetic_description).set("for","0")

        start_year_element = SubElement(att_values_element,"attvalue",value=aesthetic_start_year).set("for","1")

        url_element = SubElement(att_values_element,"attvalue",value=aesthetic_url).set("for","3")

        #check if end year is present before adding attribute
        if aesthetic_category["End_Year"] is not None:

            aesthetic_end_year = aesthetic_category["End_Year"]
            end_year_element = SubElement(att_values_element,"attvalue",value=aesthetic_end_year).set("for","2")


        #loop through related aesthetics and create edges
        for similar_aesthetic in aesthetic_category["Similar_Aesthetics"]:
            aesthetic_id = str(aesthetic_category["ID"])
            similar_aesthetic_id = str(similar_aesthetic)

            edge_element = SubElement(edges_element,"edge",source=aesthetic_id,target=similar_aesthetic_id)


ElementTree(root).write("cari_data.gexf")