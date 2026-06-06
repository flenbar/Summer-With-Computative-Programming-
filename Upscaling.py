#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = "##..##..##..##..##..##..##..##..##..##..##"
    for i in range(n):
        if i % 2 == 0 :
            print(s[0:2*n])
            print(s[0:2*n])
        else:
            print(s[2:2*(n+1)])
            print(s[2:2*(n+1)])
