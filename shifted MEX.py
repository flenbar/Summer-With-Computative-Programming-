#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    new_list = list(set(a))
    new_list.sort()
    maxi = 1
    counts = 1
    for j in range(1,len(new_list)):
        if new_list[j] == new_list[j-1] + 1 :
            counts += 1
            if counts >= maxi:
                maxi = counts
        else:
            counts = 1
    print(maxi)        
