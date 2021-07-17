result = {}

# key = 'abc'
# result[key] = 123
# result['abc']

# 1. 문장마다 입력 받아서 공백이 올 때마다 한 단어씩 나누기
# 2. 나눈 단어들을 변수에 저장한 뒤 dictionary의 key로 쓰기
# 3. 각 key들이 몇번씩 반복되는지 dictionary에 저장해서 아스키코드 순으로 출력하기

while True:
    result = {}
    str1 = input()
    if str1.strip() == "END":
        break
    split_str = str1.split()
    for word in split_str:
        if result.get(word) is None:
            result[word] = 0
        result[word] += 1
    sorted_keys = sorted(result.keys())
    for key in sorted_keys:
        print(key, ":", result[key])




