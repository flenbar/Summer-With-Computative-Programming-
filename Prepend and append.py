#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    counts = 0
    for j in range(n//2):
        if (s[j] == "1" and s[-1-j] == "0") :
            counts +=2
        elif (s[j] == "0" and s[-1-j] == "1"):
            counts += 2
        else:
            break
    print(n-counts)
