class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_tree = defaultdict(list)
        dist = [float("inf")] * (n + 1)
        dist[0] = dist[k] = 0
        visited = set()

        for u, v, w in times:
            adj_tree[u].append((w, v))

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            curr_dst, node = heapq.heappop(heap)

            if node in visited:
                continue

            for nei_dist, nei in adj_tree[node]:
                if nei not in visited:
                    heapq.heappush(heap, (curr_dst + nei_dist, nei))

            dist[node] = min(curr_dst, dist[node])
            visited.add(node)

        res = max(dist)
        return res if res != float("inf") else -1

        