class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        po = set()
        ao = set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, prev, visited):
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visited or
                prev > heights[r][c]
            ):
                return

            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, heights[r][c], visited)
            
            return

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], po)
            dfs(r, COLS - 1, heights[r][COLS - 1], ao)

        for c in range(COLS):
            dfs(0, c, heights[0][c], po)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], ao)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in ao and (r, c) in po:
                    res.append([r, c])

            
        return res



            

            
