class Solution:
    def interpret(self, command: str) -> str:
        command = [char for char in command]
        interpreter = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interpreter.append('G')
            elif command[i] == '(':
                if command[i + 1] == ')':
                    interpreter.append('o')
                    i += 1
                else:
                    interpreter.append('al')
                    i += 3
            i += 1
        return ''.join(interpreter)