class TrieNode:
    def __init__(self):
        self.chars = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for node in curr.chars.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                else:
                    if char not in curr.chars:
                        return False
                    curr = curr.chars[char]

            return curr.word

        return dfs(0, self.root)
         
        
