from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if fresh == 0:
            return 0

        mins = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):   # one BFS layer = one minute
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1
                    ):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            mins += 1

        return mins if fresh == 0 else -1