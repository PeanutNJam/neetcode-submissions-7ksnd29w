class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.idx = -1
        self.refs = 0
    
    def addWord(self, word, i):
        curr = self
        for c in word:
            idx = ord(c) - ord("a")

            if not curr.chars[idx]:
                curr.chars[idx] = TrieNode()
            curr = curr.chars[idx]
            curr.refs += 1
        curr.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        curr = TrieNode()

        for i in range(len(words)):
            curr.addWord(words[i], i)

        def getIdx(c):
            return ord(c) - ord("a")
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "*"
            or not node.chars[getIdx(board[r][c])]):
                return
            tmp = board[r][c]
            board[r][c] = "*"
            prev = node
            node = node.chars[getIdx(tmp)]

            if node.idx != -1:
                res.append(words[node.idx])
                node.refs -= 1
                node.idx = -1
                if not node.refs:
                    node = None
                    prev.chars[getIdx(tmp)] = None
                    board[r][c] = tmp
                    return

            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(r1, c1, node)
            board[r][c] = tmp


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, curr)

        return res
