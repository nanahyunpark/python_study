
def get_number(num):
    result = 0
    for i in range(1, num+1):
        result += i
    return result
def main():
    num = int(input())
    number = get_number(num)
    print(number)

if __name__ == '__main__':
    main()

