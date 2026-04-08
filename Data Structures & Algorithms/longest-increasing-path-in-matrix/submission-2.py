class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        
        def dfs(r, c, prev):
            if (
                r >= ROWS or 
                c >= COLS or
                r < 0 or
                c < 0 or
                matrix[r][c] <= prev
            ):
                return 0
            
            if (r, c) in cache:
                print(r, c)
                return cache[(r, c)]

            curr = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                curr = max(dfs(r + dr, c + dc, matrix[r][c]), curr)
            
            cache[(r, c)] = curr + 1
            return curr + 1

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c, -1), res)

        return res
            