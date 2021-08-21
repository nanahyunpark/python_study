ans = 1

def mul_ans(num):
    global ans
    tmp = num % 10
    if(num == 0):
        print(ans)
        return
    if(tmp == 0):
        tmp = 1
    ans *= tmp
    mul_ans(num // 10)

def main():
    num = input().split()
    mul_ans(int(num[0]) * int(num[1]) * int(num[2]))

if(__name__ == '__main__'):
    main()
