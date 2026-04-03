class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            curr = curr.children[c]
        curr.is_word = True

    def search(self, s, i, j):
        curr = self.root
        for idx in range(i, j + 1):
            char = s[idx]
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_word



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        node = self.root
        t = 0
        n = len(s)

        for word in wordDict:
            self.insert(word)
            t = max(t, len(word))

        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n, -1, -1):
            for j in range(i, min(n, i + t)):
                if self.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]




        