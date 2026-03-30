class TrieNode:
    def __init__(self):
        self.characters = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            curr = curr.characters[c]
        curr.endOfWord = True
            


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return curr.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return True

        
        