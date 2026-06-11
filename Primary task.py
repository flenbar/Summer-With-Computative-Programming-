#flenbar
t = int(input())
for i in range(t):
   s = input()
   if s[:2] == "10" and len(s) > 2:
       if str(int(s[2:])) == s[2:] and int(s[2:]) >= 2:
           print("Yes")
       else:
           print("No")
   else:
       print("No")
