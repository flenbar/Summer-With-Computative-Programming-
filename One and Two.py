import math
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    twos = a.count(2)
    if twos %2 != 0:
        print(-1)
        continue
    c = twos//2
    counts = 0
    for j in range(n):
        if a[j] == 2:
            counts += 1
        if counts == c :
            print(j+1)
            break
    
