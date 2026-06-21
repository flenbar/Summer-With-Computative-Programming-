#flenbar
t = int(input())
a = list(map(int,input().split()))
n = int(input())
if n not in a :
    print(-1)
else :
    c = a.index(n)
    print(c)
