
def foo(n):
    cnt = 0
    if(n==0):
        return 0
    cnt = (n%10)**2
    return cnt + foo(int(n/10))
def main():
    n = input()
    print(foo(int(n)))

if(__name__ == '__main__'):
    main()