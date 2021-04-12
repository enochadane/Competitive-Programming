class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used, assigned = set(), defaultdict(int)
        output = []
        for name in names:
            k = assigned[name]
            current = name
            while current in used:
                k += 1
                current = name + '(' + str(k) + ')'
            assigned[name] = k
            used.add(current)
            output.append(current)
            
        return output
            