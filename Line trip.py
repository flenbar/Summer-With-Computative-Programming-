#flenbar
t = int(input())
for i in range(t):
    n , x = map(int,input().split())
    a = list(map(int,input().split()))
    counts = 0
    for j in range(n):
        if j == 0:
            counts += a[j]
        else:
            c = a[j] - a[j-1]
            if c > counts :
                counts = c
    d = (x - a[-1])*2
    print(max(counts,d))
