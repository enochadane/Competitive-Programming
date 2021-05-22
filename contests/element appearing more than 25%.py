class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occurence = Counter(arr)
        for el, occ in occurence.items():
            if occ > len(arr) / 4:
                return el