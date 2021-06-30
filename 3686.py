cow_list = []

cows_num = int(input())

for cow_num in range(cows_num):
    cow = input().split()
    # cow[0] = int(cow[0])
    # cow[1] = int(cow[1])
    # for index, num in enumerate(cow):
    #     cow[index] = int(num)
    cow = list(map(int, cow))
    cow_list.append(cow)

    #1.offset

cow_offset = 0
min = None
cow_list.sort()

for index, cow in enumerate(cow_list):
    if index == len(cow_list)-1:
        break
    if cow[1] != cow_list[index+1][1]:
        offset = cow_list[index+1][0] - cow[0]  
        if min is None:
            min = offset
        if min > offset:
            min = offset
not_infected = 0
    #2.처음부터 감염 아니여도 되는 소
    #3.감염된 소 - 2.
for index, cow in enumerate(cow_list):
    if index == len(cow_list)-1:
        break
    if cow[1] != 0 and cow_list[index+1][1] == 1:
        #소가 감염이 됐고 다음 index의 소도 감염되었을 때
        if cow_list[index+1][0] - cow_list[index][0] < min:
            #그 둘의 차이가 감염범위에 포함 되는지
            not_infected = not_infected + 1
infected = 0
#전체 감염된 소 값 구하기
for cow in cow_list:
    if cow[1] == 1:
        infected = infected + 1

ans = infected - not_infected

print(ans)

