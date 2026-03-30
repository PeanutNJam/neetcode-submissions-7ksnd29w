class DSU:
    def __init__(self, n):
        self.comps = n
        self.pars = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if node != self.pars[node]:
            self.pars[node] = self.find(self.pars[node])
        return self.pars[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        self.comps -= 1
        if py > px:
            px, py = py, px

        self.pars[py] = self.pars[px]
        self.size[px] += self.size[py]
        self.size[py] = self.size[px]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = DSU(n)

        if len(edges) < n - 1:
            return False

        for x, y in edges:
            if not uf.union(x, y):
                return False

        return uf.comps == 1
        