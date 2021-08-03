
def foo(n):
    if(n==0):
        return 0
    return n + foo(n-1)
def main():
    n = input()
    print(foo(int(n)))

if(__name__ == '__main__'):
    main()