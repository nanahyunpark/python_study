def get_square(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i*j, end=" ")
        print()
    # return num

def main():
    n = int(input())
    get_square(n)

if(__name__ == '__main__'):
    main()