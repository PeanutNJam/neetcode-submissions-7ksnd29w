class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        q = deque([])

        for r in range(ROWS):
            fc, sc = 0, COLS-1

            if board[r][fc] == "O":
                q.append((r, fc))
            if board[r][sc] == "O":
                q.append((r, sc))
        
        for c in range(COLS):
            fr, sr = 0, ROWS-1
            if board[fr][c] == "O":
                q.append((fr, c))
            if board[sr][c] == "O":
                q.append((sr, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
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

                visited.add((nr, nc))
                q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = "X"

                
        

