class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_tree = defaultdict(list)

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_tree[i].append([dist, j])
                adj_tree[j].append([dist, i])
        
        heap = [[0, 0]]
        heapq.heapify(heap)
        visited = set()
        res = 0

        while heap:
            dist, p = heapq.heappop(heap)

            if p in visited:
                continue

            visited.add(p)

            res += dist
            if len(visited) == len(points):
                return res

            for nd, np in adj_tree[p]:
                if np not in visited:
                    heapq.heappush(heap, [nd, np])

            
            


