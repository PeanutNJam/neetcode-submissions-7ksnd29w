class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        root = self

        for c in word:
            idx = ord(c) - ord('a')
            if not root.children[idx]:
                root.children[idx] = TrieNode()
            root = root.children[idx]
            root.refs += 1

        root.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []

        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])

        def getIndex(c):
            return ord(c) - ord('a')

        def dfs(r, c, curr):
            if (
                r < 0
                or c < 0 
                or r >= ROWS 
                or c >= COLS 
                or board[r][c] == "*" 
                or not curr.children[getIndex(board[r][c])]
            ):
                return

            nonlocal res
            tmp = board[r][c]
            board[r][c] = "*"
            prev = curr
            curr = curr.children[getIndex(tmp)]

            if curr.idx != -1:
                res.append(words[curr.idx])
                curr.idx = -1
                curr.refs -= 1
                if curr.refs == 0:
                    prev.children[getIndex(tmp)] = None
                    curr = None
                    board[r][c] = tmp
                    return

            for r1, c1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(r1, c1, curr)

            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res

            