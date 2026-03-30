class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            curr_y = i * 3
            for j in range(3):
                curr_x = j * 3
                visited = set()
                for x in range(curr_x, curr_x + 3):
                    for y in range(curr_y, curr_y + 3):
                        if board[x][y] == ".":
                            continue
                        if board[x][y] in visited:
                            return False
                        visited.add(board[x][y])

        for r in range(9):
            visited = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])

        for c in range(9):
            visited = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        
        return True



            





            
