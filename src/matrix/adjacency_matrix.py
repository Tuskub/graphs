from graphs.graph import Graph
from matrix.matrix import Matrix
from math import inf


class AdjacencyMatrix(Matrix):

    def __init__(self, graph: Graph, custom_vertex=False):
        self.n = graph.num_vertices
        self.m = graph.num_vertices
        self.custom_vertex = custom_vertex
        super().__post_init__()
        self.fill(graph)

    # Определение полустепени исхода
    def get_outdegree(self):
        return [sum(row) for row in self.matrix]

    # Определение полустепени захода
    def get_indegree(self):
        return [sum(self._get_col(j)) for j in range(self.m)]

    def get_path_len(self, length: int) -> 'AdjacencyMatrix':
        return self ** length

    def get_route_matrix(self) -> Matrix:
        answer = self
        for i in range(1, self.n - 1):
            answer += answer * self
        return answer

    def get_circle_route_matrix(self) -> Matrix:
        answer = self
        for i in range(1, self.n):
            answer += answer * self
        return answer

    def fill(self, graph: Graph):
        for i in graph.get_edges(self.custom_vertex):
            self.matrix[i[0]][i[1]] += i[2]

        for i in range(self.n):
            for j in range(self.m):
                if i != j and self.matrix[i][j] == 0:
                    self.matrix[i][j] = inf
