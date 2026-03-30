
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, char_idx):
            if (
                r < 0 or
                c < 0 or
                char_idx >= len(word) or
                r >= ROWS or
                c >= COLS or
                board[r][c] != word[char_idx] or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))
            if char_idx == len(word) - 1 and word[char_idx] == board[r][c]:
                return True

            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for next_r, next_c in moves:
                res = dfs(next_r, next_c, char_idx + 1)
                if res == True:
                    visited.remove((r, c))
                    return res
                
            visited.remove((r, c))
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if dfs(r, c, 0):
                    return True

        return False

            
