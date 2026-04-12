class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((v, w))

        dist[k] = 0
        heap = [(0, k)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if curr_dist > dist[node]:
                continue

            for nei, weight in adj_list[node]:
                new_dist = curr_dist + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        # Ignore index 0 since nodes are 1-based
        max_dist = max(dist[1:])

        return max_dist if max_dist != float("inf") else -1