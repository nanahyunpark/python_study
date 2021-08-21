dice_num = None # input
target_sum = None # input

dice_num_list = []


def dice(level, dice_sum):
    if level == dice_num-1:
        if (target_sum - dice_sum) >= 1 and (target_sum - dice_sum) <= 6:
            for value in dice_num_list:
                print(value, end=" ")
            print(target_sum - dice_sum, end=" ")
            print()
        # print out , dice_num_list
        return
    
    elif level < dice_num:
        # dice(level+1, dice_sum + __ )
        for i in range(1, 7):
            dice_num_list[level] = i
            if dice_sum+i <= target_sum:
                dice(level+1, dice_sum + i)
            else:
                break
    

def main():
    global dice_num, target_sum
    # input
    dice_num, target_sum = map(int, input().split())
    for i in range(0, dice_num-1):
        dice_num_list.append(0)
    dice(0, 0)
    # pass

if(__name__ == '__main__'):
    main()