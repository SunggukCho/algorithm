def check(sr, sc, fr, fc):            #행렬 구역을 모두 처리
    check = [0 for _ in range(10)]
    for i in range(sr, fr):
        for j in range(sc, fc):
            if check[sudoku[i][j]] == 0:
                check[sudoku[i][j]] += 1
            else:
                return 0
    for j in range(1, len(check)):
        if check[j] == 0:
            return 0
    return 1


for tc in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    cnt = 1
    for i in range(9):
        if check(i, 0, i+1, 9) == 0:    #행
            cnt = 0
            break
        if check(0, i, 9, i+1) == 0:    #열
            cnt = 0
            break
    for i in range(0, 7, 3):            #시작점설정, 3칸씩 확인
        for j in range(0, 7, 3):
            if check(i, j, i+3, j+3) == 0:
                cnt = 0
                break
        if cnt == 0:
            break

    print('#{} {}'.format(tc, cnt))