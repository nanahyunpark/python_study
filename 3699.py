# 1. 테스트 케이스 개수 입력 받기
# 2. 1에서 입력 받은 값만큼 
    # 3. 의상 개수 N개 입력 받기 
    # 4. N 줄 만큼 들어오는 의상 이름과 종류 입력 받기 ex) hat headgear (의상 이름, 의상 종류)
    # 5. 나올 수 있는 최대 의상 조합 개수 구하기 (한 조합에는 의상이 최소 1개 들어가야함
    #                                    한 조합에 같은 의상 종류는 한개씩만 들어갈 수 있음)


case_num = int(input())
costume_dict = {}
costume_name = []
ans = 1

for i in range(0, case_num):
    costume_dict = {}
    N = int(input())
    if N == 0:
        print(0)
        continue
    for j in range(0, N):
        costumes = input().split()
        costume_name = costumes[0]
        costume_type = costumes[1]
        if costume_dict.get(costume_type) is None:
            costume_dict[costume_type] = []
        costume_dict[costume_type].append(costume_name)
        ans = 1
    for key in costume_dict:
        value = set(costume_dict[key])
        # print("**" , key, value, len(value), costume_dict)
        ans *= len(value) + 1
    ans = ans - 1
    print(ans)


# 포함 배제의 원리를 이용: (종류 별 개수 + 1 (안 입는 경우)) 모두 곱한 뒤, 모두 안 입는 경우 1가지 빼기