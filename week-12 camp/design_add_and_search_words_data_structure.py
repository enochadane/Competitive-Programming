class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None]*26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if not curr.children[ord(letter) - ord('a')]:
                curr.children[ord(letter) - ord('a')] = TrieNode(letter)
            curr = curr.children[ord(letter) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
    def dfs(self, curr, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for child in curr.children:
                    if child and self.dfs(child, word[i + 1:]):
                        return True
                return False
            elif not curr.children[ord(c) - ord('a')]:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return curr.isWord
        
        
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)