def airConditioners():
    t = int(input())
    for _ in range(t):
        input()
        nk = list(map(int, input().split()))
        n = nk[0]
        k = nk[1]
        pos_conditioners = list(map(int, input().split()))
        temperatures = list(map(int, input().split()))
        for i in range(n):
            cell_tempr = float('inf')
            for j in range(k):
                cell_tempr = min(cell_tempr, temperatures[j] + abs(pos_conditioners[j] - (i + 1)))
            print(cell_tempr, end = ' ')
        
        print('\n')

airConditioners()
    