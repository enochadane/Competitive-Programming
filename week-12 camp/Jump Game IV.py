class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set()
        dict_ = {}
        steps = 0
        queue = deque()
        queue.append((0, 0))
        visited.add(0)
        
        for i in range(len(arr)):
            if arr[i] in dict_:
                dict_[arr[i]].append(i)
            else:
                dict_[arr[i]] = [i]
        while queue:
            curr, steps = queue.popleft()
            if curr == len(arr) - 1:
                return steps
            if curr + 1 < len(arr) and curr + 1 not in visited:
                queue.append((curr + 1, steps + 1))
                visited.add(curr + 1)
            if curr - 1 >= 0 and curr - 1 not in visited:
                queue.append((curr - 1, steps + 1))
                visited.add(curr - 1)
            
            for v in dict_[arr[curr]]:
                if v not in visited:
                    queue.append((v, steps + 1))
                    visited.add(v)
            dict_[arr[curr]].clear()
            
        return -1
                    
            