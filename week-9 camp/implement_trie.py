class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = [None]*26
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = Node(c)
            # curr = Node(c)
            curr = curr.children[ord(c) - ord('a')]
            
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if not curr.children[ord(c) - ord('a')]:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if curr.children[ord(c) - ord('a')] is None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)