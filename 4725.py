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

cnt = 0
for index in range(len(prefix_sum_nums)):
    partial_left_sum = prefix_sum_nums[index] # Split in the middle (left)
    partial_right_sum = prefix_sum_nums[-1] - prefix_sum_nums[index] # Split in the middle (right)

    if partial_left_sum == partial_right_sum:
        for left_index in range(0, index):
            partial_left_sum2 = prefix_sum_nums[left_index]

            # partial_right_sum2 = prefix_sum_nums[index] - prefix_sum_nums[left_index] # similar concept

            print('check1', partial_left_sum2)
            print('check2', partial_right_sum2)

        for right_index in range(index+1, index, -1):
            # partial_left_sum2 = prefix_sum_nums[right_index] - prefix_sum_nums[index]

            partial_right_sum2 = prefix_sum_nums[-1] - prefix_sum_nums[right_index]

            print('check2', partial_left_sum2)
            print('check2', partial_right_sum2)
            