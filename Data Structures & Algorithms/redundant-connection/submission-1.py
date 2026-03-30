class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, node):
        if node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if py > px:
            px, py = py, px
        
        self.size[px] += self.size[py]
        self.size[py] = self.size[px]
        self.par[py] = self.par[px]
        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = DSU(len(edges) + 1)

        for u, v in edges:
            if not uf.union(u, v):
                res = [u, v]

        return res

        
            

        
        