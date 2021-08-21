
def foo(n):
    if(n<=0):
        return
    foo(n-2)
    print(n, end=" ")
    return
def main():
    n = input()
    foo(int(n))

if(__name__ == '__main__'):
    main()