class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_tree = defaultdict(list)
        visited = set()

        for u, v, t in times:
            adj_tree[u].append((t, v))

        heap = []
        heapq.heappush(heap, (0, k))
        t = 0

        while heap:
            curr_t, curr_v = heapq.heappop(heap)
            if curr_v in visited:
                continue

            t = curr_t
            for nei_t, nei_v in adj_tree[curr_v]:
                if nei_v not in visited:
                    heapq.heappush(heap, (curr_t + nei_t, nei_v))

            visited.add(curr_v)

        return t if len(visited) == n else -1  
