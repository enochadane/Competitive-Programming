class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}
        count = 0
        for i in range(len(arr)):
            if arr[i] not in freq_dict.keys():
                for j in range(i, len(arr), 1):
                    if arr[i] == arr[j] and arr[i]:
                        count += 1
                freq_dict[arr[i]] = count
                count = 0
        print(freq_dict.keys(), 'keys')
        print(set(freq_dict.values()))
        print(freq_dict.values())
        if len(set(freq_dict.values())) != len(freq_dict.values()):
            return False
        return True
    