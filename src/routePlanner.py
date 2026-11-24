"""
routePlanner.py
====================================
Program that shows the best route between two points in a map.

| Author: Logan Hudson
| Date: 2026 November 24
"""

import osmnx as ox
import networkx as nx
import folium

# Download street network data for a specific location
G = ox.graph_from_place('Sioux City, Iowa, USA', network_type='drive')

# Find shortest path between two points
origin = ox.distance.nearest_nodes(G, X=-96.3596, Y=42.4756)  # Example coordinates for origin
destination = ox.distance.nearest_nodes(G, X=-96.4155, Y=42.5258)  # Example coordinates for destination
route = nx.shortest_path(G, origin, destination, weight='length')

# Visualize the route on a map
route_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in route]

# Center the map on the starting point (use index)
route_map = folium.Map(location=route_coords[0], zoom_start=13)

# Draw the route line (this takes the full list)
folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(route_map)

# Add start ([0]) and end ([-1]) markers
folium.Marker(route_coords[0], popup="Origin", icon=folium.Icon(color="green")).add_to(route_map)
folium.Marker(route_coords[-1], popup="Destination", icon=folium.Icon(color="red")).add_to(route_map)

route_map.save("route_map.html")



if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
