line = input()

nums = line.split()

N = int(nums[0])
K = int(nums[1])

cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            print(i)
if cnt < K:
    print(0)
