class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        successes = set()
        res = []

        def dfs(r, c, prev):
            nonlocal a
            nonlocal p
            if a and p:
                return
            if r >= ROWS or c >= COLS:
                a = True
                return
            elif r < 0 or c < 0:
                p = True
                return
            elif (r, c) in visited or prev < heights[r][c]:
                return

            visited.add((r, c))
                
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, heights[r][c])

            
        for r in range(ROWS):
            for c in range(COLS):
                a = p = False
                visited = set()
                dfs(r, c, heights[r][c])
                if a and p:
                    res.append([r, c])

        return res
