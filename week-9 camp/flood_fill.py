class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m, oldColor, visited = len(image), len(image[0]), image[sr][sc], set()
        
        return self.fill_helper(image, sr, sc, newColor, oldColor, visited, n, m)
    
    def fill_helper(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int, visited: set(), n: int, m: int) -> List[List[int]]:
        
        curr_r = sr
        curr_c = sc
        
        top = (curr_r - 1, curr_c)
        bottom = (curr_r + 1, curr_c)
        left = (curr_r, curr_c - 1)
        right = (curr_r, curr_c + 1)
        directions = [top, bottom, left, right]
        image[sr][sc] = newColor
        visited.add((curr_r, curr_c))

        for i in range(len(directions)):
            if self.isValid(directions[i][0], directions[i][1], n, m) and (directions[i][0], directions[i][1]) not in visited:
                if image[directions[i][0]][directions[i][1]] == oldColor:
                    self.fill_helper(image, directions[i][0], directions[i][1], newColor, oldColor, visited, n, m)
        return image
        
        
    def isValid(self, cr: int, cc: int, rows: int, columns: int) -> bool:
        return 0 <= cr < rows and 0 <= cc < columns
            
        
    
#  dfs-> iterative   
    
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         visited = []
#         n = len(image)
#         m = len(image[0])
#         stack = [(sr, sc)]
#         oldColor = image[sr][sc]
#         while len(stack) > 0:
#             print(stack, 'stack')
#             curr = stack.pop()
#             curr_r = curr[0]
#             curr_c = curr[1]
#             if (curr_r, curr_c) not in visited:
                
#                 visited.append((curr_r, curr_c))
                
#                 image[curr_r][curr_c] = newColor
                    
#                 top = (curr_r - 1, curr_c)
#                 bottom = (curr_r + 1, curr_c)
#                 left = (curr_r, curr_c - 1)
#                 right = (curr_r, curr_c + 1)
#                 directions = [top, bottom, left, right]
                
#                 for i in range(len(directions)):
#                     if self.isValid(directions[i][0], directions[i][1], n, m):
#                         if image[directions[i][0]][directions[i][1]] == oldColor:
#                             print(directions[i], i)
#                             stack.append((directions[i][0], directions[i][1]))
                    
#         return image
    

        
                