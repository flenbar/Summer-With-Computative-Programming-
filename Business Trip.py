#flenbar
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
sums = 0
if n == 0:
    print(0)
elif sum(a) < n :
    print(-1)    
else:
    for i in range(len(a)):
        sums += a[i]
        if sums >= n:
            print(i+1)
            break
