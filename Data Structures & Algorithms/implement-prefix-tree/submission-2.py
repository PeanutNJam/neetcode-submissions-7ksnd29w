class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.lastChar = False

class PrefixTree:

    def __init__(self):
        self.trietree = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.trietree
        for char in word:
            if char not in curr.children:
                new = TrieNode(char)
                curr.children[char] = new
            curr = curr.children[char]
        curr.lastChar = True


    def search(self, word: str) -> bool:
        curr = self.trietree

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return curr.lastChar
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trietree

        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return True

        
        