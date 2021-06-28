my_2d_list = []

rows_num = 3
cols_num = 5

print(my_2d_list)

for row_num in range(rows_num):
    my_2d_list.append([])
    print(len(my_2d_list), my_2d_list)
    for col_num in range(cols_num):
        my_2d_list[-1].append(row_num)

print(my_2d_list)

for row_num in range(rows_num):
    for col_num in range(cols_num):
        print(my_2d_list[row_num][col_num], end='')
    print()