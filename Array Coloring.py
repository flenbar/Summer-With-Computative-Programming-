#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    my_list = list(map(int,input().split()))
    if sum(my_list) %2 == 0:
        print("YES")
    else:
        print("NO")
