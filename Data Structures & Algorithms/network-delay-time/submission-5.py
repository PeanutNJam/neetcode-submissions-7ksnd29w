class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = (n + 1) * [float("inf")]
        visited = set()

        adj_tree = defaultdict(list)

        for u, v, w in times:
            adj_tree[u].append((w, v))

        heap = []
        heapq.heappush(heap, (0, k))
        t = 0

        while heap:
            new_w, new_v = heapq.heappop(heap)

            if new_v in visited:
                continue

            for nei_w, nei_v in adj_tree[new_v]:
                if nei_v not in visited:
                    heapq.heappush(heap, (new_w + nei_w, nei_v))

            visited.add(new_v)
            t = new_w

        return t if len(visited) == n else -1





        
