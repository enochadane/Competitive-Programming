class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        stack1 = [n for n in num1]
        stack2 = [n for n in num2]
        output = []
        carry = 0
        while stack1 or stack2:
            if stack1 and stack2:
                localSum = int(stack1.pop()) + int(stack2.pop()) + carry
                carry = 0
                if localSum > 9:
                    carry = int(str(localSum)[0])
                    localSum = int(str(localSum)[1])
                output.append(str(localSum))
            if stack1 and not stack2:
                localSum = int(stack1.pop()) + carry
                carry = 0
                if localSum > 9:
                    carry = int(str(localSum)[0])
                    localSum = int(str(localSum)[1])
                output.append(str(localSum))
            if stack2 and not stack1:
                localSum = int(stack2.pop()) + carry
                carry = 0
                if localSum > 9:
                    carry = int(str(localSum)[0])
                    localSum = int(str(localSum)[1])
                output.append(str(localSum))
        if carry != 0:
            output.append(str(carry))
            
        return ''.join(output[::-1])