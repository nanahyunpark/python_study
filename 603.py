# 공백을 포함한 문장을 입력 받아서 홀수 번째 단어를 차례로 출력하는 프로그램을 작성하시오. 문장의 길이는 100자 이하이다.

# I like you better than him.

# I
# you
# than

line = input()

words = line.split()
# words = line.split(sep = None) # None = 공백 / sep = 나눌곳

# print(words)

# for word in words: # 다 꺼내오는
#     print(word)

index = 0
while index < len(words): #len = array 안에 몇개가 들어있는지
    print(words[index])
    index += 2