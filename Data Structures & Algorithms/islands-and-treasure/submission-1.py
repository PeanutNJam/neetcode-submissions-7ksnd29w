class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1

        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    nr >= ROWS or
                    nc >= COLS or
                    nr < 0 or
                    nc < 0 or
                    grid[nr][nc] != INF
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

