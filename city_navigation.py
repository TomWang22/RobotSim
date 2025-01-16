import osmnx as ox
import networkx as nx
import googlemaps

class CityNavigation:
    def __init__(self, city, api_key=None):
        self.city = city
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key) if api_key else None
        self.graph = ox.graph_from_place(city, network_type='drive')

    def find_shortest_path(self, start_coords, end_coords):
        orig_node = ox.distance.nearest_nodes(self.graph, X=start_coords[1], Y=start_coords[0])
        dest_node = ox.distance.nearest_nodes(self.graph, X=end_coords[1], Y=end_coords[0])
        path = nx.shortest_path(self.graph, orig_node, dest_node, weight='length')
        return path

    def plot_path(self, start_coords, end_coords):
        path = self.find_shortest_path(start_coords, end_coords)
        ox.plot_graph_route(self.graph, path)

    def get_live_traffic(self, origin, destination):
        if not self.gmaps:
            raise ValueError("Google Maps API key is required for live traffic data.")
        directions = self.gmaps.directions(origin, destination, mode="driving", departure_time="now")
        return directions

if __name__ == "__main__":
    city = "New York, USA"
    nav = CityNavigation(city, api_key="YOUR_GOOGLE_MAPS_API_KEY")
    start = (40.730610, -73.935242)  # Start coordinates (latitude, longitude)
    end = (40.712776, -74.005974)    # End coordinates (latitude, longitude)

    # Find and plot the shortest path
    nav.plot_path(start, end)

    # Get live traffic (requires API key)
    traffic_data = nav.get_live_traffic("New York, NY", "Boston, MA")
    print(traffic_data)
