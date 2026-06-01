#flenbar
import math
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a[a.index(min(a))] += 1
    print(math.prod(a))
