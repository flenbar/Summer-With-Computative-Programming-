#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for j in range(n):
        if a[j] >= b[j] :
            a[j] , b[j] = b[j] , a[j]
    maxi = max(max(a),max(b))
    mini = min(max(a),max(b))
    suma = sum(b)
    print(maxi + (suma - maxi + mini))
