#flenbar
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    my_list = list(map(int, input().split()))
    total = sum(my_list)
    if total % 2 != 0:
        print("YES")
    else:
        if (n * k) % 2 == 0:
            print("YES")
        else:
            print("NO")
