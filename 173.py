def get_subtract(n1, n2):
    
    if(n1 < n2):
        n1, n2 = n2, n1
    ans = n1**2 - n2**2
    print(ans)

def main():
    n = input().split()
    get_subtract(int(n[0]), int(n[1]))


if(__name__ == '__main__'):
    main()