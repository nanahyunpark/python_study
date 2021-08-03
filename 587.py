
def foo(n):
    if(n==0):
        return
    print("recursive")
    foo(n-1)
    return
def main():
    n = input()
    foo(int(n))

if(__name__ == '__main__'):
    main()