from graphs.graph import Graph
from matrix.adjacency_matrix import AdjacencyMatrix

test_data_g1 = {(0, 2), (0, 3), (1, 2), (2, 2), (3, 1)}
test_data_g2 = {(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)}
g1 = Graph(4, test_data_g1)
g2 = Graph(3, test_data_g2)


adj_matrix_g1 = AdjacencyMatrix(g1)
print(f"Матрица смежности G1:\n{adj_matrix_g1}")
adj_matrix_g2 = AdjacencyMatrix(g2)
print(f"Матрица смежности G2:\n{adj_matrix_g2}")
g_union = g1.union(g2)
adj_matrix_g_union = AdjacencyMatrix(g_union)
print(f"Матрица смежности G union:\n{adj_matrix_g_union}")
g_intersection = g1.intersection(g2)
adj_matrix_g_intersection = AdjacencyMatrix(g_intersection)
print(f"Матрица смежности G intersection:\n{adj_matrix_g_intersection}")
g_symmetric_difference = g1.symmetric_difference(g2)
adj_matrix_g_symmetric_difference = AdjacencyMatrix(g_symmetric_difference)
print(f"Матрица смежности G symmetric_difference:\n{adj_matrix_g_symmetric_difference}")
g_joining = g1.joining(g2)
adj_matrix_g_joining = AdjacencyMatrix(g_joining)
print(f"Матрица смежности G joining:\n{adj_matrix_g_joining}")
g_cartesian_product = g1.cartesian_product(g2)
adj_matrix_g_cartesian_product = AdjacencyMatrix(g_cartesian_product, custom_vertex=True)
print(f"Матрица смежности G cartesian_product:\n{adj_matrix_g_cartesian_product}")
print(sum(adj_matrix_g_cartesian_product.get_outdegree()))
