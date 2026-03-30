class unionFind:
    def __init__(self, n):
        self.count = n
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        self.count -= 1
        if py > px:
            px, py = py, px
        
        self.size[px] += self.size[py]
        self.size[py] = self.size[px]
        self.par[py] = self.par[px]




class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n)

        for x, y in edges:
            uf.union(x, y)

        return uf.count


        