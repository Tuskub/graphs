from dataclasses import dataclass
import math


@dataclass()
class Edge:
    f: int
    t: int
    cost: int

    def __repr__(self):
        return f'From {self.f} to {self.t} with cost {self.cost}'


def ford_bellman_alg(v, num_edges, edges_):
    dest = []
    for i in range(num_edges):
        dest.append(0 if i == v else math.inf)

    for i in range(num_edges):
        for edge in edges_:
            t = dest[edge.f] if dest[edge.f] is math.inf else dest[edge.f] + edge.cost
            if dest[edge.t] > t:
                dest[edge.t] = t

    print(dest)


edges = [
    Edge(0, 1, 8), Edge(0, 4, 12), Edge(0, 6, 16),
    Edge(1, 0, 8), Edge(1, 2, 11), Edge(1, 4, 6),
    Edge(2, 1, 11), Edge(2, 3, 14), Edge(2, 5, 14),
    Edge(3, 2, 14), Edge(3, 9, 14), Edge(3, 5, 10),
    Edge(4, 0, 12), Edge(4, 1, 6), Edge(4, 5, 14), Edge(4, 6, 10), Edge(4, 7, 8),
    Edge(5, 4, 14), Edge(5, 2, 14), Edge(5, 3, 10), Edge(5, 7, 14), Edge(5, 8, 15), Edge(5, 9, 20),
    Edge(6, 0, 16), Edge(6, 4, 10), Edge(6, 8, 11),
    Edge(7, 4, 8), Edge(7, 5, 14), Edge(7, 6, 11), Edge(7, 8, 17),
    Edge(8, 5, 15), Edge(8, 7, 17), Edge(8, 9, 17),
    Edge(9, 3, 14), Edge(9, 5, 20), Edge(9, 8, 17)
]

ford_bellman_alg(1, 10, edges)
