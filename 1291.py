# 구구단

def get_multiplication(n1, n2):
    num_mul = n1
    if(n1 < n2):
        for i in range(1, 10):
            for j in range(0, (n2-n1)+1):
                print(num_mul, " * ", i, " = ", end="", sep="")
                if(num_mul*i < 10):
                    print(" ", end="")
                print((num_mul*i), "   ", end="", sep="")
                num_mul = num_mul + 1
            print()
            num_mul = n1
    if(n1 > n2):
        for i in range(1, 10):
            for j in range(0, (n1-n2)+1):
                print(num_mul, " * ", i, " = ", end="", sep="")
                if(num_mul*i < 10):
                    print(" ", end="")
                print((num_mul*i), "   ", end="", sep="")
                num_mul = num_mul - 1
            print()
            num_mul = n1
    if(n1 == n2):
        for i in range(1, 10):
            print(num_mul, " * ", i, " = ", end="", sep="")
            if(num_mul*i < 10):
                print(" ", end="")
            print((num_mul*i), "   ", sep="")


def main():
    while(True):
        n = input().split()
        n[0] = int(n[0])
        n[1] = int(n[1])
        if(n[0] <= 9 and n[0] > 1 and n[1] <= 9 and n[1] > 1):
            break
        print("INPUT ERROR!")
    get_multiplication(int(n[0]), int(n[1]))


if(__name__ == '__main__'):
    main()