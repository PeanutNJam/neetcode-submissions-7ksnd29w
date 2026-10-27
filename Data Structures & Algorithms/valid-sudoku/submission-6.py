class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        r_map = defaultdict(set)
        c_map = defaultdict(set)
        rc_map = defaultdict(set)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != ".":
                    if board[r][c] in r_map[r] or board[r][c] in c_map[c] or board[r][c] in rc_map[(r // 3, c // 3)]:
                        return False
                    r_map[r].add(board[r][c])
                    c_map[c].add(board[r][c])
                    rc_map[(r // 3 ,c // 3)].add(board[r][c])

        return True

