nums = int(input())
my_list = list(map(int, input().split()))
counts = 1
maxi_counts = 1
for i in range(1, nums):
    if my_list[i] >= my_list[i - 1]:
        counts += 1
    else:
        counts = 1
    maxi_counts = max(maxi_counts, counts)
print(maxi_counts)
