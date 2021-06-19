n = int(input())
nums = input().split()

for index, num in enumerate(nums):
    nums[index] = int(num)

print(nums)

prefix_sum_nums = []

prefix_sum = 0
for num in nums:
    prefix_sum = prefix_sum + num
    print(prefix_sum_nums)
    prefix_sum_nums.append(prefix_sum)

print(prefix_sum_nums)

partial_sum = prefix_sum_nums[m] - prefix_sum_nums[n-1]

partial_sum = 0

for index in range(n, m):
    partial_sum += nums[index]