class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [word for word in paragraph]
        onlyWords = []
        notBanned = []
        
        for word in paragraph:
            if word is "'":
                continue
            onlyWords.append(word.lower())
        onlyWords = ''.join(onlyWords)
        onlyWords = onlyWords.replace(',', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split(' ')
        
        print(onlyWords, 'onlyWords')
        
        for word in onlyWords:
            if word in banned:
                continue
            notBanned.append(word)
        print(notBanned, 'not banned')
        frequency = {}
        
        for word in notBanned:
            if word != '':
                if word in frequency.keys():
                    frequency[word] += 1
                else:
                    frequency[word] = 1
        frequency = sorted(frequency.items(), key = lambda item: item[1], reverse = True)
        
        return frequency[0][0]
        
        