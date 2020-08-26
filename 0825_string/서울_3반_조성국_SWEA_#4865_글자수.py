
T = int(input())
for tc in range(1, T+1):
    N = list(input())
    M = list(input())
    arr_x = [0 for _ in range(26)]
    arr_y = [0 for _ in range(26)]

    for i in N:
        idx = ord(i)-66
        arr_x[idx] += 1

    for j in M:
        idx = ord(j) - 66
        arr_y[idx] += 1

    max_arr_y = []
    for k in range(len(arr_x)):
        if arr_x[k] != 0:
            max_arr_y.append(arr_y[k])
        else:
            max_arr_y.append(0)
    print('#{} {}'.format(tc, max(max_arr_y)))