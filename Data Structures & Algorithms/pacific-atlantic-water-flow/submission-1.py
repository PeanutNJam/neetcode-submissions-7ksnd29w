from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r: int, c: int, visited: set):
            visited.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    # reverse flow: can go from ocean inward only if next is higher/equal
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        pac = set()
        atl = set()

        # Pacific: top row + left col
        for c in range(COLS):
            dfs(0, c, pac)
        for r in range(ROWS):
            dfs(r, 0, pac)

        # Atlantic: bottom row + right col
        for c in range(COLS):
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, COLS - 1, atl)

        # cells that can reach BOTH oceans
        return [[r, c] for (r, c) in pac & atl]