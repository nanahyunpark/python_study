import math

N = input()
N = int(N)

# for i in range(N):
#     if i*i == N:
#         print(i)
#         break
#     if i*i <= N:
#         if (i+1)*(i+1) >= N:
#             print(i)

ans = 0
for exp in range(32, -1, -1):
    num = 2**exp
    if (ans + num)**2 <= N:
        ans += num
    pass
print(ans)