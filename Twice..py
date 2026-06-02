#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    counts = 0
    dic = {}
    for x in a:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    for key in dic:
         counts += dic[key] // 2
    print(counts)
    
