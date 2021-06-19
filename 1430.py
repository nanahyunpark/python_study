a = int(input())
b = int(input())
c = int(input())

num = a*b*c

str_num = str(num)

for i in range(0, 10):
    print(str_num.count(str(i)))
