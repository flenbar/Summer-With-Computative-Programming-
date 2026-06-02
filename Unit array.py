#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = a.count(1)
    c = a.count(-1)
    result = 0
    while c > b:
        c -= 1
        b += 1
        result += 1
    if c % 2 == 1:
        result += 1
    print(result)    
