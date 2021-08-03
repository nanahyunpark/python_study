#1. 학생 수와 방 마다 최대 인원수 입력 받기
#2 학생 수 만큼 성별과 학년 입력 받기
#3. 필요한 방 개수 출력하기


def input_handler():
    stu_male = [0,0,0,0,0,0]
    stu_female = [0,0,0,0,0,0]
    info = input().split()
    stu_num = int(info[0])
    max_ppl = int(info[1])
    for i in range(0, stu_num):
        stu = input().split()
        for index, num in enumerate(stu):
            stu[index] = int(num) 
        if stu[0] == 1:
            stu_male[stu[1]-1] += 1
        if stu[0] == 0:
            stu_female[stu[1]-1] += 1
    return max_ppl, stu_male, stu_female

def get_rooms(max_ppl, stu_gender):
    rooms = 0
    for index, value in enumerate(stu_gender):
        rooms += value//max_ppl
        if value%max_ppl != 0:
            rooms += 1
    return rooms

def main():
    max_ppl, stu_male, stu_female = input_handler()
    ans = 0
    ans += get_rooms(max_ppl, stu_male)
    ans += get_rooms(max_ppl, stu_female)
    print(ans)

if __name__ == '__main__':
    main()