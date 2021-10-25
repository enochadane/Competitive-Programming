# num = int(input().split()[1])
num = input()
count = 0
while int(num) != 0:
    num = str(abs(int(num)))
    opt1 = ''
    opt2 = '1'
    for _ in range(len(num)):
        opt1 += '1'
        opt2 += '1'
    opt = int(opt1)
    diff1 = int(opt1) - int(num)
    diff2 = int(opt2) - int(num)
    if diff2 < diff1:
        opt = int(opt2)
        count += len(opt2)
    else:
        count += len(opt1)
    num = abs(int(num)) - opt
    
print(count)
