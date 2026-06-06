#flenbar
n =int(input())
s = input()
if n % 2 == 0:
    x = ""
    for i in range(n):
        
        b = s[i]
        if i%2 == 0:
            x = b + x
        else:
            x = x + b
else:
    x = ""
    for i in range(n):
        b = s[i]
        if i%2 == 0:
            x = x + b
        else:
            x = b + x
print(x)            
