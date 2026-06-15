# flenbar
t = int(input())
for i in range(t):
    n, c, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for j in range(n):
        if a[j] > c:
            break
        add = min(k, c - a[j])
        a[j] += add
        k -= add
        c += a[j]
    print(c)
