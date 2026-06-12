#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counts = [0] * 26
    s = ""
    for j in range(n):
        for k in range(26):
            if counts[k] == a[j]:
                s += chr(k + 97)
                counts[k] += 1
                break
    print(s)
