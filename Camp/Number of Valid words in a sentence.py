class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0
        for word in words:
            if self.isValid(word):
                count += 1
        return count
    def isValid(self, word: str) -> bool:
        word = list(word)
        punctuations = {'!', '.', ','}
        count_hyphen = 0
        notWord = False
        for i in range(len(word)):
            if 48 <= ord(word[i]) <= 57:
                return False
            if word[i] == '-':
                if i == 0:
                    return False
                elif i == len(word) - 1:
                    return False
                elif word[i + 1] in punctuations:
                    return False
            if word[i] == '-':
                count_hyphen += 1
            if count_hyphen > 1:
                return False
            if word[i] in punctuations and i != len(word) - 1:
                return False
        return True