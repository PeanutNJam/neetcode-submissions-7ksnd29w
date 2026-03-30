class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2**31 - 1

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append((r, c))

        while q:
            nr, nc = q.popleft()
            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r, next_c = nr + r, nc + c
                if (next_r < 0
                or next_r >= ROWS
                or next_c < 0
                or next_c >= COLS
                or grid[next_r][next_c] != INF):
                    continue
                
                grid[next_r][next_c] = grid[nr][nc] + 1
                q.append((next_r, next_c))
                                 

