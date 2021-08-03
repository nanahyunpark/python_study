
def power_nums(nums):
    print("(", nums[0], " - ", nums[1], ") ^ 2 = ", (nums[0]-nums[1])**2, sep="")
    print("(", nums[0], " + ", nums[1], ") ^ 3 = ", (nums[0]+nums[1])**3, sep="")

def main():
    nums = input().split()
    for index, value in enumerate(nums):
        nums[index] = int(nums[index])
    power_nums(nums)

if(__name__ == '__main__'):
    main()