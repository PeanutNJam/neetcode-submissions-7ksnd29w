class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc)


        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res
        
