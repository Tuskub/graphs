from graphs.graph import Graph
from matrix.adjacency_matrix import AdjacencyMatrix
from matrix.incidence_matrix import IncidenceMatrix

graph_v = 5
graph_edges = {
    (0, 1), (0, 3),
    (2, 0), (2, 1),
    (3, 2),
    (4, 0), (4, 3)
}

graph = Graph(graph_v, graph_edges)
adj_matrix = AdjacencyMatrix(graph)
print(f"Матрица смежности:\n{adj_matrix}")
inc_matrix = IncidenceMatrix(graph)
print(f"Матрица инцедентности:\n{inc_matrix}")

route = adj_matrix.get_route_matrix().matrix
test_matrix = []

for i in range(len(route)):
    test_matrix.append([])
    for j in range(len(route[i])):
        test_matrix[i].append(1 if route[i][j] > 0 or j == i else 0)
print(f"Матрица достижимости T:")
for i in test_matrix:
    print(i)

new_test_matrix = []
for i in range(len(route)):
    new_test_matrix.append([])
    for j in range(len(route[i])):
        new_test_matrix[i].append(1 if route[i][j] > 0 and route[j][i] > 0 else 0)
print(f"Матрица сильной связаности S:")
for i in new_test_matrix:
    print(i)


def get_sub_matrix(matrix, vert):
    ans = []
    for index in vert:
        ans.append([matrix[index][v] for v in vert])
    return ans


def get_graph_component(matrix):
    p = 0
    s = matrix

    for p in range(len(matrix)):
        v = [index for index, value in enumerate(matrix[p]) if value == 1]
        new_matrix = get_sub_matrix(adj_matrix.matrix, v)
        return new_matrix

    return


print('Матрица смежности для компонента сисльной связности графа:')
for i in get_graph_component(new_test_matrix):
    print(i)
