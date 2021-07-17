# 1. 5줄 모두 입력 받고 배열에 집어 넣기
# 2. 
# 3. 세로로 5글자씩 어딘가에 저장해서  차례대로 출력해야함

#input
# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

nums = []
# n1 = ""
# n2 = ["", "", "", "", ""]
n3 = []

for i in range(0,5):
    nums.append(input())

# for i in range(0,5):
#     print(nums[i])

for i in range(0,5):
    for j in range(0, len(nums[i])):
        n3.append("")
        
for i in range(0,5):
    for j in range(0, len(nums[i])):
        # if j == 0:
        #     n1 += nums[i][j]
        # if j == 1:
        #     n2[i] += nums[i][j]
        # if j == 2:
        n3[j] += nums[i][j]  

# print(n1)
# print(n2)
# print(n3)

for n in n3:
    print(n, end="")
        
