import sys
sys.stdin = open('sudoku_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    new_arr = []
    #1. 행 우선순회
    for i in range(9):
        sum_row = 0
        for j in range(9):
            num = arr[i][j]
            sum_row += num
        if sum_row == 45:
            new_arr.append(1)
        else:
            new_arr.append(0)

    #2. 열 우선순회
    for i in range(9):
        sum_c = 0
        for j in range(9):
            num2 = arr[j][i]
            sum_c += num2
        if sum_c == 45:
            new_arr.append(1)
        else:
            new_arr.append(0)

    #3. 격자 순회
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum_rec = 0
            for k in range(3):
                for l in range(3):
                    num3 = arr[i+k][j+l]
                    sum_rec += num3
            if sum_rec == 45:
                new_arr.append(1)
            else:
                new_arr.append(0)

    #for i in new_arr:

    if 0 in new_arr:
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))