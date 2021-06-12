line = input()

nums = line.split()

n = int(nums[0])
m = int(nums[1])

# range

# print(list(range(5))) 0부터 5 전까지
# print(list(range(1, 5))) - 1부터 4까지
# print(list(range(1, 5, 2))) - 2 간격으로

num = 1
for row in range(n): 
    for columnn in range(m):
        print(num, end = ' ')
        num += 1
    print()