#flenbar
t = int(input())
a = list(map(int,input().split()))
for i in range(t) :
    if a[i] <= 10 :
        print(f'A[{i}] = {a[i]}')
