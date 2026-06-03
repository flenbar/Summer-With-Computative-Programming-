#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    counts = 0
    result = 0
    for j in range(n):
        if a[j] == 1:
            counts = 0
        else:
            counts +=1
            if counts >= result :
                result = counts
    print(result)
