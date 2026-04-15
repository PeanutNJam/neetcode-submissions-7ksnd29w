class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_tree = defaultdict(list)
        n = len(points)
        visited = set()

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj_tree[i].append((cost, j))
                adj_tree[j].append((cost, i))

        heap = []
        heapq.heappush(heap, (0, 0))
        res = 0

        while heap:
            cost, idx = heapq.heappop(heap)

            if (idx) in visited:
                continue

            res += cost
            for cost, nei in adj_tree[idx]:              
                heapq.heappush(heap, (cost, nei))
            
            visited.add(idx)

        return res

            




