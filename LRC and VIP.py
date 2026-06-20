#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    count_max = a.count(mx)
    if count_max == n:
        print("No")
    else:
        print("Yes")
        groups = []
        for num in a:
            if num == mx:
                groups.append(1)
            else:
                groups.append(2)
 
        print(*groups)
