import networkx as nx
import edge_gravity

florentine_family = nx.generators.social.florentine_families_graph()

new_g = nx.DiGraph()
for node in florentine_family.nodes():
    new_g.add_node(node)
    
for u, v in florentine_family.edges():
    new_g.add_edge(u,v)
    new_g.add_edge(v,u)
    
florentine_family = new_g
print(edge_gravity.edge_gravity(florentine_family, k=15).most_common(40))