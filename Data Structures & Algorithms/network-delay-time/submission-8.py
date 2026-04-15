class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = (n + 1) * [float("inf")]
        dist[0] = dist[k] = 0
        visited = set()

        adj_tree = defaultdict(list)

        for u, v, w in times:
            adj_tree[u].append((w, v))

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            new_w, new_v = heapq.heappop(heap)

            if new_v in visited:
                continue

            for nei_w, nei_v in adj_tree[new_v]:
                if nei_v not in visited:
                    heapq.heappush(heap, (new_w + nei_w, nei_v))

            dist[new_v] = min(new_w, dist[new_v])
            visited.add(new_v)

        res = max(dist)
        return res if res != float("inf") else -1                    





        
