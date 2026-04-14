class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        n = len(points)
        visited = set()
        res = 0

        for i in range(n):
            x_i, y_i = points[i]
            for j in range(i + 1, n):
                x_j, y_j = points[j]
                cost = abs(x_i - x_j) + abs(y_i - y_j)
                adj_list[i].append([cost, j])
                adj_list[j].append([cost, i])

        heap = []
        heapq.heappush(heap, [0, 0])
        while len(visited) < n:
            curr, idx = heapq.heappop(heap)
            if idx in visited:
                continue

            res += curr
            
            for dst, i in adj_list[idx]:
                if i not in visited:
                    heapq.heappush(heap, [dst, i])
            visited.add(idx)

        return res

        
