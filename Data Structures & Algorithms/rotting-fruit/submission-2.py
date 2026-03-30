class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])
        fruits = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fruits.add((r, c))

        res = 0
        
        while q:
            curr_len = len(q)
            for _ in range(curr_len):
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or nr >= ROWS or 0 > nc or nc >= COLS or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fruits.remove((nr, nc))
                    q.append((nr, nc))
            
            if q:
                res += 1


        return res if not fruits else -1

            
            
