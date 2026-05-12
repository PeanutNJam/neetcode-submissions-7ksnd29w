class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X" or (r, c) in visited or not r or not c or r == ROWS - 1 or c == COLS - 1:
                    continue
                new_visited = set()
                visited.add((r, c))
                q = deque([(r, c)])

                outside = False
                while q:
                        curr_r, curr_c = q.popleft()
                        if curr_r == 0 or curr_c == 0 or curr_r == ROWS - 1 or curr_c == COLS - 1:
                            outside = True
                        new_visited.add((curr_r, curr_c))
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
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

                if not outside:
                    for rr, cc in new_visited:
                        board[rr][cc] = "X"

               

