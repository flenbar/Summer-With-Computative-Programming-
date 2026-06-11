t = int(input())
for i in range(t):
    m , a , b , c = map(int,input().split())
    total = 2 * m
    if m < a :
        a = m
    if m < b :
        b = m
    free = total - ( a + b)
    c = min(free,c)
    print(a + b + c)        
