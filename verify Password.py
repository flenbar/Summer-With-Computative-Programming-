t = int(input())
for i in range(t):
    n = int(input())
    password = input()
    digits = ""
    chars = ""
    for j in range(n):
        if password[j].isalpha():
            chars = chars + password[j]
        elif password[j].isdigit():
            digits = digits + password[j]
        else:
            print("NO")
            exit()
    if password == digits + chars :
        if digits == "".join(sorted(digits)) and chars == "".join(sorted(chars)):
            print("Yes")
        else:
            print("NO")
    else:
        print("NO")        


