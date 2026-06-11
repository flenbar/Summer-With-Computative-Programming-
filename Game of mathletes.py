#flenbar
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = 0
    right = n - 1
    score = 0
    while left < right:
        s = a[left] + a[right]
        if s == k:
            score += 1
            left += 1
            right -= 1
        elif s < k:
            left += 1
        else:
            right -= 1
    print(score)
