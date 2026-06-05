#flenbar
t = int(input())
for i in range(t):
    a , b , c , d = map(int,input().split())
    if d < b:
        print(-1)
    else:
        a += d - b
        if a < c:
           print(-1)
        else:
           print((d-b) +(a-c))
