class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        fresh = count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while fresh > 0 and q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                visited.add((cr, cc))

                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (
                        nr < 0 or
                        nc < 0 or
                        nr >= ROWS or
                        nc >= COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] != 1
                    ):
                        continue
                    fresh -= 1
                    grid[nr][nc] = 3
                    q.append((nr, nc))
                
            count += 1

        print(count)
        return count if not fresh else -1

                    
                    

                    




    

