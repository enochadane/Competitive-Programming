from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        vertical_move = [(1, 0), (0, 1)]
        horizontal_move = [(0, 1), (1, 0)]
        cw_rotation = [(0,0), (1, -1)]
        ccw_rotation = [(0,0), (-1, 1)]
        n = len(grid[0])
        finish = [(n - 1, n - 2), (n - 1, n - 1)]
        curr_position = [(0, 0), (0, 1)]
        moves = 0
        next = []
        next.append([(0, 0), (0, 1), moves])
        while next:
            curr_position = next.pop(0)
            if curr_position[0][0] == curr_position[1][0]: #current position is horizontal
                #move right
                if grid[curr_position[0][0]][curr_position[1][1] + 1] == 0 and curr_position[1][1] < len(grid[0]):
                    next_move_tail = (curr_position[0][0] + horizontal_move[0][0], curr_position[0][1] + horizontal_move[1][1])
                    next_move_head = (curr_position[1][0] + horizontal_move[0][0], curr_position[1][1] + horizontal_move[0][1])
                    next.append([next_move_tail, next_move_head, moves+1])
                #move down or rotate cw
                if grid[curr_position[0][0] + 1][curr_position[0][1]] == 0 and grid[curr_position[1][0] + 1][curr_position[1][1]] == 0:
                    next_move_tail = (curr_position[0][0] + horizontal_move[1][0], curr_position[0][1] + horizontal_move[1][1])
                    next_move_head = (curr_position[1][0] + horizontal_move[1][0], curr_position[1][1] + horizontal_move[1][1])
                    #some conditions to rotate
                    # next_move_tail = (curr_position[0])
                    # next_move_head = (curr_position[1][0] + cw_rotation[1][0], curr_position[1][1] + cw_rotation[1][1])
                    next.append([next_move_tail, next_move_head, moves+1])
                next.append(curr_position, 1)
            if curr_position[0][1] == curr_position[1][1]: #current position is vertical
                #move down
                if grid[curr_position[0][1]][curr_position[1][1] + 1] == 0:
                    next_move_tail = (curr_position[0][0] + vertical_move[0][0], curr_position[0][1] + vertical_move[0][1])
                    next_move_head = (curr_position[1][0] + vertical_move[0][0], curr_position[1][1] + vertical_move[0][1])
                    next.append([next_move_tail, next_move_head, moves+1])
                #move right or rotate ccw
                if grid[curr_position[0][0]][curr_position[0][1] + 1] == 0 and grid[curr_position[1][0]][curr_position[1][1] + 1] == 0:
                    next_move_tail = (curr_position[0][0] + vertical_move[1][0], curr_position[0][1] + vertical_move[1][1])
                    next_move_head = (curr_position[1][0] + vertical_move[1][0], curr_position[1][1] + vertical_move[1][1])
                    #rotate -> some condition
                    # next_move_tail = (curr_position[0])
                    # next_move_head = (curr_position[1][0] + ccw_rotation[1][0], curr_position[1][1] + ccw_rotation[1][1])
                    next.append([next_move_tail, next_move_head, moves+1])
        return moves
                    


