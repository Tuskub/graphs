import pygraphviz as pgv

from graphs.graph import Graph
from matrix.adjacency_matrix import AdjacencyMatrix
from matrix.incidence_matrix import IncidenceMatrix

graph_v = 6
graph_edges = {
    (0, 4), (0, 5),
    (1, 0), (1, 2),
    (2, 1), (2, 3),
    (3, 5),
    (4, 1), (4, 3), (4, 5),
    (5, 2), (5, 3)
}

graph = Graph(graph_v, graph_edges)
adj_matrix = AdjacencyMatrix(graph)
print(f"Матрица смежности:\n{adj_matrix}")
inc_matrix = IncidenceMatrix(graph)
print(f"Матрица инцедентности:\n{inc_matrix}")
print(f"Полустепень исхода:\n{adj_matrix.get_outdegree()}")
print(f"Полустепень захода:\n{adj_matrix.get_indegree()}")
print(f"Матрица маршрутов С:\n{adj_matrix.get_route_matrix()}")
print(f"Матрица замкнутых маршрутов С:\n{adj_matrix.get_circle_route_matrix()}")
length = int(input("Введите длину маршрута: "))
print(f"Число маршрутов длины L={length}\n{adj_matrix.get_path_len(length)}")

A = pgv.AGraph(directed=True, strict=False)

A.add_nodes_from(graph.vertices)
A.add_edges_from(graph.get_edges())
A.node_attr["style"] = "filled"
A.node_attr["shape"] = "circle"
A.node_attr["fixedsize"] = "true"
A.node_attr["fillcolor"] = "#BD93F9"
A.write("simple.dot")
A.layout()
A.draw("img/simple.png", prog="dot")
