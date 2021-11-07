from collections import deque
def minimumMoves():
    positions = list(map(int, input().split()))
    start = tuple(map(int, positions[:2]))
    dest = tuple(map(int, positions[2:]))

    rookq = deque([(start[0], start[1], 0)])
    bishopq = deque([(start[0], start[1], 0)])
    kingq = deque([(start[0], start[1], 0)])

    rook_vis = {start}
    bishop_vis = {start}
    king_vis = {start}
    mins = [0] * 3
    r_reached, b_reached, k_reached = False, False, False
    while rookq or bishopq or kingq:
        if rookq:
            rr, rc, rmoves = rookq.popleft()
        if bishopq:
            br, bc, bmoves = bishopq.popleft()
        if kingq:
            kr, kc, kmoves = kingq.popleft()
        
        if rr == dest[0] or rc == dest[1]:
            mins[0] = 1
        else:
            mins[0] = 2
        # if rr == dest[0] and rc == dest[1]:
        #     r_reached = True
        #     mins[0] = rmoves
        if br == dest[0] and bc == dest[1]:
            b_reached = True
            mins[1] = bmoves
        if kr == dest[0] and kc == dest[1]:
            k_reached = True
            mins[2] = kmoves
        if r_reached and b_reached and k_reached:
            break
        
        # rook movement
        # for i in range(1, 9):
        #     down = rc - i
        #     up = rc + i
        #     left = rr - i
        #     right = rr + i

        #     if isValid(8, rr, down) and (rr, down) not in rook_vis:
        #         rook_vis.add((rr, down))
        #         rookq.append((rr, down, rmoves + 1))
        #     if isValid(8, rr, up) and (rr, up) not in rook_vis:
        #         rook_vis.add((rr, up))
        #         rookq.append((rr, up, rmoves + 1))
        #     if isValid(8, left, rc) and (left, rc) not in rook_vis:
        #         rook_vis.add((left, rc))
        #         rookq.append((left, rc, rmoves + 1))
        #     if isValid(8, right, rc) and (right, rc) not in rook_vis:
        #         rook_vis.add((right, rc))
        #         rookq.append((right, rc, rmoves + 1))
        
        # bishop movement
        for i in range(1, 9):
            x = br + i
            y = bc + i
            nx = br - i
            ny = bc - i

            if isValid(8, x, y) and (x, y) not in bishop_vis:
                bishop_vis.add((x, y))
                bishopq.append((x, y, bmoves + 1))
            if isValid(8, x, ny) and (x, ny) not in bishop_vis:
                bishop_vis.add((x, ny))
                bishopq.append((x, ny, bmoves + 1))
            if isValid(8, nx, y) and (nx, y) not in bishop_vis:
                bishop_vis.add((nx, y))
                bishopq.append((nx, y, bmoves + 1))
            if isValid(8, nx, ny) and (nx, ny) not in bishop_vis:
                bishop_vis.add((nx, ny))
                bishopq.append((nx, ny, bmoves + 1))
        
        # king movement
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr in directions:
            new_kx = kr + dr[0]
            new_ky = kc + dr[1]

            if isValid(8, new_kx, new_ky) and (new_kx, new_ky) not in king_vis:
                king_vis.add((new_kx, new_ky))
                kingq.append((new_kx, new_ky, kmoves + 1))

    print(mins[0], mins[1], mins[2])

def isValid(n, x, y):
    if 0 <= x <= n and 0 <= y <= n:
        return True
    return False

minimumMoves()