#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    my_list = list(map(int,input().split()))
    pos_list = []
    neg_list = []
    for j in range(n-1):
        if my_list[j] < 0:
            neg_list.append(my_list[j])
        else:
            pos_list.append(my_list[j])
            
    print(abs(sum(neg_list))-sum(pos_list))      
