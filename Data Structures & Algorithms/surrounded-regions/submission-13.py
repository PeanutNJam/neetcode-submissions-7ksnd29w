class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([])

        for r in range(ROWS):
            lc, rc = 0, COLS - 1
            if board[r][lc] == "O":
                q.append((r, lc))
            if board[r][rc] == "O": 
                q.append((r, rc))

        for c in range(COLS):
            lr, rr = 0, ROWS - 1
            if board[lr][c] == "O":
                q.append((lr, c))
            if board[rr][c] == "O":
                q.append((rr, c))

        while q:
            cr, cc = q.popleft()
            visited.add((cr, cc))

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (
                    nr < 0 or
                    nc < 0 or
                    nr >= ROWS or
                    nc >= COLS or
                    (nr, nc) in visited or
                    board[nr][nc] == "X"
                ):
                    continue

                q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"

               

