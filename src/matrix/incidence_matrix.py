from dataclasses import dataclass
from graphs.graph import Graph
from matrix.matrix import Matrix


@dataclass
class IncidenceMatrix(Matrix):

    def __init__(self, graph: Graph):
        self.n = graph.num_vertices
        self.m = graph.get_num_edges()
        super().__post_init__()
        self.fill(graph)

    def fill(self, graph: Graph):
        for i, edge in enumerate(graph.get_edges()):
            if edge[0] == edge[1]:
                self.matrix[edge[0]][i] += 1
            self.matrix[edge[0]][i] += -1
            self.matrix[edge[1]][i] += 1
