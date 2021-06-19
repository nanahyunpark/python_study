a = int(input())
b = int(input())
c = int(input())

num = a*b*c

for i in range(0, 10):
    print(num.count(str(i)))
