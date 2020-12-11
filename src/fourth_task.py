from graphs.graph import Graph
from matrix.adjacency_matrix import AdjacencyMatrix
import copy


graph_v = 5
graph_edges = {
    (0, 1, 2), (0, 2, 3),
    (1, 2, 2),
    (2, 3, 2),
    (3, 0, 3), (3, 4, 2),
    (4, 2, 1),
}

# graph_v = 4
# graph_edges = {
#     (0, 1, 1), (0, 2, 2), (0, 3, 1),
#     (1, 0, 2), (1, 2, 7),
#     (2, 0, 6), (2, 1, 5), (2, 3, 2),
#     (3, 0, 1), (3, 2, 4),
# }


def floyd_warshall(matrix, vertices):
    for m in range(vertices):
        buf = copy.deepcopy(matrix)
        for c in range(len(matrix)):
            for j in range(len(matrix[c])):
                matrix[c][j] = min(buf[c][j], buf[c][m] + buf[m][j])
    return matrix


test = Graph(graph_v, graph_edges)
aj = AdjacencyMatrix(test)
print(f"Матрица смежности:\n{aj}")
new_test = aj.matrix

answer = floyd_warshall(new_test, graph_v)
for i in answer:
    print(i)
