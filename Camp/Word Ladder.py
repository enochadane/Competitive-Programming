class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            currWord, steps = queue.popleft()
            if currWord == endWord:
                return steps
            currWord = [c for c in currWord]
            for i in range(n):
                modified = [c for c in currWord]
                for c in range(97, 123):
                    if currWord[i] == chr(c):
                        continue
                    modified[i] = chr(c)
                    next_word = ''.join(modified)
                    if next_word in wordList and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))
        return 0