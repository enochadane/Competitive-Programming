class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        choices = ['A', 'C', 'G', 'T']
        queue = deque([(start, 0)])
        while queue:
            gene, steps = queue.popleft()
            if gene == end:
                return steps
            gene = [c for c in gene]
            for i in range(8):
                modified = [c for c in gene]
                for c in choices:
                    if gene[i] == c:
                        continue
                    modified[i] = c
                    next_gene = ''.join(modified)
                    if next_gene in bank:
                        queue.append((next_gene, steps + 1))
        return -1