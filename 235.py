def div_ans(num, level):
    if(num == 1):
        print(level)
        return
    if(num%2 == 0):
        num = num//2
        div_ans(num, level+1)
    elif(num%2 == 1):
        num = num//3
        div_ans(num, level+1)

def main():
    num = int(input())
    div_ans(num, 0)

if(__name__ == '__main__'):
    main()
