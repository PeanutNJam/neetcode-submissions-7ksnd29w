class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        adj_tree = defaultdict(list)
        res = 0
        n = len(points)

        for i in range(n):
            xi, yi = points[i]
            for j in range(n):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj_tree[i].append([cost, j])

        heap = []
        heapq.heappush(heap, [0, 0])

        while len(visited) < n:
            cost, idx = heapq.heappop(heap)

            if idx in visited:
                continue

            res += cost
            visited.add(idx)

            for nei_cost, nei in adj_tree[idx]:
                if nei not in visited:
                    heapq.heappush(heap, [nei_cost, nei])
            
            
        return res


