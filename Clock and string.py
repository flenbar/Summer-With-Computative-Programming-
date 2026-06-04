#flenbar
t = int(input())
for i in range(t):
    a , b ,c , d = map(int,input().split())
    if a > b :
        a , b = b , a
    x = a < c < b
    y = a < d < b
    if x != y :
        print("Yes")
    else:
        print("No")
        
