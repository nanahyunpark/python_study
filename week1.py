# 파이썬 입력은 모두 string
#프린트 디폴드 = \n spilt default = 공백


# acsl : Python3
# usaco : C/C++ - Python3
# csap, Csap-a, csap-p : Java


# 입력
# 연산
  # 조건
  # 반복
# 출력

# 문자열 처리

# scanf("%d", &num); # scanf 이름 가진 함수, scanf(...)
# input () , invoke

# pointer -> 주소 : 주소는 고정된 형태/크기 ( 값을 담는 그릇 : 변수 )

# input:
# 3 5
# output:
# 8

array1 = [1, 2, 3, 4]
print(array1)

my_str = 'AAB ABC AB CD'

results = my_str.split(' ')
print(results)

results = input().split() # 3 5 -> 3, 5
num1 = results[0]
num2 = results[1]

# num1, num2 = input().split()

num1 = int(num1) # type casting, 형 변환 int('123 45') -> 12345
num2 = int(num2)
print(num1 + num2)

num3 = input()
num4 = input()
num3 = float(num3)
num4 = float(num4)
print(num3+num4)

my_str = str('abc')
print(my_str)


line1 = input()  # input 이름을 가진 함수
line2 = input()  # input 이름을 가진 함수

print(line1+line2)
# 3+5
# 3 + 5

# 변수, 변수
print(line1, end = '출력의 마지막')
# print(end='\n')
print(line2, end = '\n')


