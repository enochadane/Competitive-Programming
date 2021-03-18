class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        validStrings = []
        s = S[1:len(S) -1]
        for i in range(1, len(s)):
            x = s[:i]
            y = s[i:]
            
            x_possibilities = [x]
            y_possibilities = [y]
            if len(x) > 1:
                x_possibilities += self.insertDecimal(x)
                
            if len(y) > 1:
                y_possibilities += self.insertDecimal(y)
            
            
            for x_num in x_possibilities:
                for y_num in y_possibilities:
                    if self.isValidString(x_num) and self.isValidString(y_num):
                        coordinate = '(' + x_num + ', ' + y_num + ')'
                        validStrings.append(coordinate)
            
        return validStrings
    
    def insertDecimal(self, num: str) -> List[str]:
        possibleStrings = []
        num = [digit for digit in num]
        for i in range(len(num) -1):
            decimal = num.copy()
            decimal[i] = decimal[i] + '.'
            possibleStrings.append(''.join(decimal))
        
        return possibleStrings
    
    def isValidString(self, num: str) -> bool:
        num = [digit for digit in num]
        if len(num) > 1 and num[0] == '0' and num[len(num) -1] == '0':
            return False
        if len(num) > 1 and num[0] == '0' and num[1] != '.':
            return False
        if num[len(num) -1] == '0' and '.' in num:
            return False
        
        return True
    
    
    
    