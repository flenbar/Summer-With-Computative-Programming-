#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = s.count("(")
    b = s.count(")")
    if a == b :
        print("Yes")
    else:
        print("No")
    
