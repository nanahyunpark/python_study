 
cows_num = int(input())
 
cows_list = []
 
for cow_num in range(cows_num):
    postion, infected = map(int, input().split())
    cows_list.append([postion, infected])
 
cows_list.sort()
 
min_offset = None
 
for cow_num, cow in enumerate(cows_list):
    if cow_num + 1 == len(cows_list):
        break
     
    if cows_list[cow_num+1][1] != cow[1]:
         
        offset = cows_list[cow_num+1][0] - cow[0]
        # print(offset)
        if min_offset is None or min_offset > offset:
            min_offset = offset
     
# print(cows_list)
# print(min_offset)
 