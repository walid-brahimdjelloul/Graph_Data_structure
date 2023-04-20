from graph import Graph
from vertex import Vertex

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')
 
railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)
 
railway.add_edges(peel, harwick)
railway.add_edges(harwick, callan)
railway.add_edges(callan, peel)

# path_exist = sntf.find_path('agha','kharoba')
# print(path_exist)

railway.find_path('peel', 'ulfstead')