class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if not fresh:
            return 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0

        while fresh > 0 and q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc

                    if (
                        nr < 0 or
                        nc < 0 or
                        nr >= ROWS or
                        nc >= COLS or
                        grid[nr][nc] != 1
                    ):
                        continue
                    fresh -= 1
                    q.append((nr, nc))
                    grid[nr][nc] = 3

            res += 1

        return res if not fresh else -1

