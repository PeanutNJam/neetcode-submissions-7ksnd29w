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
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.chars.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in node.chars:
                        return False
                    node = node.chars[c]
                
            return node.word

        return dfs(0, self.root)



        
