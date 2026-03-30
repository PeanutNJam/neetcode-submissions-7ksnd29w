class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                (r, c) in visited
                or r >= ROWS
                or c >= COLS
                or r < 0
                or c < 0
                or grid[r][c] == 0
            ):
                return

            visited.add((r, c))
            nonlocal curr

            curr += 1

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc)

            return

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    curr = 0
                    dfs(r, c)
                    res = max(res, curr)

        return res