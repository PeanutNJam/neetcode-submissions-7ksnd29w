class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X" or (r, c) in visited:
                    continue

                region = set()
                q = deque([(r, c)])
                visited.add((r, c))
                outside = False

                while q:
                    curr_r, curr_c = q.popleft()
                    region.add((curr_r, curr_c))

                    if (
                        curr_r == 0 or curr_c == 0 or
                        curr_r == ROWS - 1 or curr_c == COLS - 1
                    ):
                        outside = True

                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc

                        if (
                            nr < 0 or nc < 0 or
                            nr >= ROWS or nc >= COLS or
                            (nr, nc) in visited or
                            board[nr][nc] == "X"
                        ):
                            continue

                        visited.add((nr, nc))   # mark when adding
                        q.append((nr, nc))

                if not outside:
                    for rr, cc in region:
                        board[rr][cc] = "X"