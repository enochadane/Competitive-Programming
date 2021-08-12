class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            sorted_ = []
            for i in range(26):
                sorted_.append(count[i] * chr(i + ord('a')))
            return ''.join(sorted_)
        
        d = defaultdict(list)
        for s in strs:
            d[getKey(s)].append(s)
        return d.values()