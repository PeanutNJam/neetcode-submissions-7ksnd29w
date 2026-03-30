class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (
                r == 0 
                or c == 0 
                or c == COLS - 1
                or r == ROWS - 1
            ) and board[r][c] == "O":
                return True

            if board[r][c] == "X" or (r, c) in visited:
                return False

            visited.add((r, c))

            return dfs(r + 1, c) or dfs(r - 1, c) or dfs(r, c + 1) or dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if (r == 0 or 
                    c == 0 or 
                    c >= COLS - 1 or 
                    r >= ROWS - 1 or 
                    board[r][c] == "X"):
                    continue
                else:
                    if not dfs(r, c):
                        board[r][c] = "X"



