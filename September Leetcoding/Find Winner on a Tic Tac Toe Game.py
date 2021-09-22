class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                board[i][j] = '.'
        for i in range(len(moves)):
            if i % 2 == 0:
                board[moves[i][0]][moves[i][1]] = 'X'
            elif i % 2 != 0:
                board[moves[i][0]][moves[i][1]] = 'O'
        return self.checkBoard(board)
    
    def checkBoard(self, board: List[List[str]]) -> str:
        for i in range(3):
            countA = 0
            countB = 0
            for j in range(3):
                if board[i][j] == 'X':
                    countA += 1
                elif board[i][j] == 'O':
                    countB += 1
            if countA == 3:
                return 'A'
            elif countB == 3:
                print('row')
                return 'B'
            
        for i in range(3):
            countA = 0
            countB = 0
            for j in range(3):
                if board[j][i] == 'X':
                    countA += 1
                elif board[j][i] == 'O':
                    countB += 1
            if countA == 3:
                return 'A'
            elif countB == 3:
                print('column')
                return 'B'
        
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            return 'A'
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            return 'B'
        
        if board[2][0] == board[1][1] == board[0][2] == 'X':
            return 'A'
        elif board[2][0] == board[1][1] == board[0][2] == 'O':
            return 'B'
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    return 'Pending'
        return 'Draw'