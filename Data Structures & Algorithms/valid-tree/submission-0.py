class DSU:
    def __init__(self, n):
        self.comps = n
        self.pars = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, edge):
        if self.pars[edge] != edge:
            self.pars[edge] = self.find(self.pars[edge])
        return self.pars[edge]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False

        if self.size[px] > self.size[py]:
            px, py = py, px

        self.pars[px] = self.pars[py]
        self.size[px] += self.size[py]
        self.size[py] = self.size[px]
        self.comps -= 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = DSU(n)

        if len(edges) > n - 1:
            return False

        for x, y in edges:
            if not uf.union(x, y):
                return False
        
        return uf.comps == 1