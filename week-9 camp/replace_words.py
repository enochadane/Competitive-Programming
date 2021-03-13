class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None]*26
        self.word = None

class Solution:
    def __init__(self):
        self.node = TrieNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(' ')
        # print(words, 'words')
        for root in dictionary:
            self.insert(root)
        for i in range(len(words)):
            word = self.find_prefix(words[i])
            words[i] = word
                
        
        return ' '.join(words)
    
    def insert(self, word: str) -> None:
        curr = self.node
        for letter in word:
            if not curr.children[ord(letter) - ord('a')]:
                curr.children[ord(letter) - ord('a')] = TrieNode()
            curr = curr.children[ord(letter) - ord('a')]
        curr.isWord = True
        curr.word = word
        # print(curr.word, 'inserted word')
        
    def find_prefix(self, word: str) -> str:
        curr = self.node
        for letter in word:
            if curr.isWord:
                return curr.word
            if curr.children[ord(letter) - ord('a')]:
                curr = curr.children[ord(letter) - ord('a')]
            else:
                return word
        return word
    