a = ['1','2','33','44']

for i in range(len(a)):
    a[i] = a[i] + '..'

b = '0'
c = [d for d in b]
print(len(c) > 0)

for i in range(1, len(b)):
    x = b[:i]
    y = b[i:]
    print(x, y)

print([1,2,3] + ['k', 'e'])

print(float('7'))


print(float(1e-05))