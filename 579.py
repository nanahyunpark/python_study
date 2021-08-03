
def sort_nums(nums):
    nums.sort()
    nums.reverse()
    return nums

def main():
    n = input()
    nums = input().split()
    for index, value in enumerate(sort_nums(nums)):
        nums[index] = int(nums[index])
    for index, value in enumerate(sort_nums(nums)):
        print(value, end=" ")

if(__name__ == '__main__'):
    main()