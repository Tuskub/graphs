from dataclasses import dataclass, field


@dataclass
class Matrix:

    n: int
    m: int

    matrix: list = None

    def __post_init__(self):
        if self.matrix is None:
            self.matrix = [[0] * self.m for i in range(self.n)]

    def __add__(self, other: "Matrix"):
        if self.n != other.n or self.m != other.m:
            raise Exception("Сложение матриц невозможно")
        answer = []
        for row in zip(self.matrix, other.matrix):
            answer.append([a + b for a, b in zip(row[0], row[1])])
        return Matrix(self.n, self.m, answer)

    def __mul__(self, other: "Matrix"):
        if self.m != other.n:
            raise Exception("Перемножение матриц невозможно")
        answer = []
        for row in self.matrix:
            answer.append(
                [sum([a * b for a, b in zip(row, other._get_col(j))])
                    for j in range(other.m)])
        return Matrix(self.n, other.m, answer)

    def __pow__(self, b):
        answer = Matrix(self.n, self.n, self.matrix)
        for i in range(1, b):
            answer *= self
        return answer

    def __str__(self):
        return '\n'.join(f"{row}" for row in self.matrix)

    def fill(self, *args):
        for i in range(self.n):
            self.matrix[i] = [int(j) for j in input().split(' ')[:self.m]]

    def _get_col(self, col_num: int):
        return [row[col_num] for row in self.matrix]
