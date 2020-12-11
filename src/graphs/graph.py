from dataclasses import dataclass
from typing import Set, Tuple


@dataclass
class Graph:
    num_vertices: int
    edges: Set[Tuple[int, int, int]] = None
    vertices: set = None

    def __post_init__(self):
        if self.edges is None:
            raise Exception('Не передавайте None, пожожста!')
        if self.vertices is None:
            self.vertices = set(range(self.num_vertices))

    def get_num_edges(self):
        return len(self.edges)

    def get_edges(self, custom_vertex=False):
        if custom_vertex:
            sort_vertex = sorted(list(self.vertices))
            res = list()
            for e in self.edges:
                res.append(
                    (sort_vertex.index(e[0]), sort_vertex.index(e[1]))
                )
            return res
        return list(self.edges)

    def union(self, other: 'Graph') -> 'Graph':
        vertices = self.vertices.union(other.vertices)
        return Graph(
            num_vertices=len(vertices),
            edges=self.edges.union(other.edges),
            vertices=vertices
        )

    def intersection(self, other: 'Graph') -> 'Graph':
        vertices = self.vertices.intersection(other.vertices)
        return Graph(
            num_vertices=len(vertices),
            edges=self.edges.intersection(other.edges),
            vertices=vertices
        )

    def symmetric_difference(self, other: 'Graph') -> 'Graph':
        vertices = self.vertices.union(other.vertices)
        return Graph(
            num_vertices=len(vertices),
            edges=self.edges.symmetric_difference(other.edges),
            vertices=vertices
        )

    def joining(self, other: 'Graph') -> 'Graph':
        vertices = self.vertices.union(other.vertices)
        return Graph(
            num_vertices=len(vertices),
            edges=self.edges.union(
                other.edges,
                set((x, y) for x in range(len(vertices)) for y in range(len(vertices)) if x != y)
            ),
            vertices=vertices
        )

    # def cartesian_product(self, other: 'Graph') -> 'Graph':
    #     vertices = {(x, y) for x in self.vertices for y in other.vertices}
    #     return Graph(
    #         num_vertices=len(vertices),
    #         edges=set(
    #             (x, y) for x in vertices for y in vertices
    #             if ((x[0] == y[0] and other.edges.__contains__((x[1], y[1]))) or
    #                 (x[1] == y[1] and self.edges.__contains__((x[0], y[0])))) and
    #             (x != y)
    #         ),
    #         vertices=vertices
    #     )
