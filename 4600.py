n, k = input().split()

nums = []

n = int(n)
k = int(k)


nums = input().split()

for index, num in enumerate(nums):
    nums[index] = int(num)
#위 enumerate 는 형변환을 위해 for문 안에서 사용됨
#for문이 끝난 뒤 nums를 출력하였을 때 index와 value가 함께 나오지 않는 이유는 위 for문에서 쓰인 후 버려졌기 때문

nums.sort()
#작은 값부터 정렬
nums.reverse()
#반대로
ans = 0
for index in range(k):
    ans = ans + nums[index]
for i in range(k):
    ans = ans - i
print(ans)

