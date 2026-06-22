#flenbar
t = int(input())
a = list(map(int,input().split()))
for i in range(t):
    if a[i] > 0:
        a[i] = 1
    elif a[i] < 0 :
        a[i] = 2
    else:
        a[i] = 0
print(*a)