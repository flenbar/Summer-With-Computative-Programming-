#flenbar
a = input().strip()
b = 0
initials = "a"
for i in range(len(a)):
    d = abs(ord(a[i]) - ord(initials))
    b += min(d, 26 - d)
    initials = a[i]
print(b)
