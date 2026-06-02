#flenbar
t = int(input())
for i in range(t):
    n , f , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[f-1]
    a.sort(reverse = True)
    r = a[:k]
    if b not in r:
        print("No")
    else:
        count_a = a.count(b)
        count_r = r.count(b)
        if count_a == count_r :
            print("Yes")
        else:
            print("Maybe")
