class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [i for i in range(26)]
        rank = [1] * 26
        def find(a):
            if a == leader[a]:
                return a
            leader[a] = find(leader[a])
            return leader[a]
        def union(a, b):
            aLead = find(a)
            bLead = find(b)
            
            if rank[aLead] > rank[bLead]:
                leader[bLead] = aLead
                rank[aLead] += rank[bLead]
            else:
                leader[aLead] = bLead
                rank[bLead] += rank[aLead]
            
        for equation in equations:
            if equation[1] == '=':
                x, y = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
                union(x, y)
        for equation in equations:
            x, y = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
            if equation[1] == '!' and find(x) == find(y):
                return False
        return True