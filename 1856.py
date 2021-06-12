line = input()

nums = line.split()

n = int(nums[0])
m = int(nums[1])

board = []

for row in range(n):
    board.append([0] * m)

num = 1
for row in range(n):
    if row % 2 == 0: # when the line is an even number
        for col in range(m): # 0~4
            board[row][col] = num # In the place of (row, col), inset num
            num += 1 # increase num by 1
    if row % 2 == 1:
        for col in range(m-1, -1, -1):
            board[row][col] = num
            num += 1
            
for row in board:
    for col in row:
        print(col, end = ' ') 
    print()