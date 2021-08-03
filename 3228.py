#1. 학생수와 각 학생의 점수들을 입력 받는다
#2. 각 학생의 점수들 중 최대값과 최소값을 구한다
#3. 최대 점수와 최소 점수를 뺀 값을 출력한다


def get_difference(max_score, min_score):
    print(max_score-min_score)

def get_min(scores):
    return min(scores)

def get_max(scores):
    return max(scores)

def input_handler():
    stu_num = int(input())
    scores = input().split()
    for index, num in enumerate(scores):
        scores[index] = int(num) 
    return scores

def main():
    scores = input_handler()
    min_score = get_min(scores)
    max_score = get_max(scores)
    get_difference(max_score, min_score)


if __name__ == '__main__':
    main()

