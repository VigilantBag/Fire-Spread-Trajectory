import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np

import overpass
api = overpass.API()

response = api.get('node["name"="Springfield"]["place"]', responseformat="csv(name,::lon,::lat)")
print(response)