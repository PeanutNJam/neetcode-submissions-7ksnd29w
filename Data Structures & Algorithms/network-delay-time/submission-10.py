class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()

        adj_tree = defaultdict(list)

        for u, v, t in times:
            adj_tree[u].append([t, v])

        heap = []
        heapq.heappush(heap, [0, k])
        res = 0


        while heap:
            t, u = heapq.heappop(heap)
            if u in visited:
                continue

            visited.add(u)
            res = t
            
            for new_t, new_v in adj_tree[u]:
                if new_v not in visited:
                    heapq.heappush(heap, [t + new_t, new_v])

            

        return res if len(visited) == n else -1
            