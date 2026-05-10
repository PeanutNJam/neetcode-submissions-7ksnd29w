class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_tree = defaultdict(list)

        for u, v, t in times:
            adj_tree[u].append([t, v])

        visited = set()

        heap = [[0, k]]
        heapq.heapify(heap)

        while heap:
            dist, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            if len(visited) == n:
                return dist

            for nd, nnode in adj_tree[node]:
                if nnode not in visited:
                    heapq.heappush(heap, [nd + dist, nnode])


        return -1
            
            

