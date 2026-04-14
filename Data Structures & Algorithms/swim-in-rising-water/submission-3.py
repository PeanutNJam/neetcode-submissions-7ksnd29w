class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = []
        heapq.heappush(heap, [grid[0][0], 0, 0])
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            val, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return val
            
            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if (
                    new_r > n - 1 or 
                    new_c > n - 1 or 
                    new_r < 0 or
                    new_c < 0
                ):
                    continue

                heapq.heappush(heap, [max(grid[new_r][new_c], val), new_r, new_c])

            
                


