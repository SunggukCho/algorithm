import sys
sys.stdin = open('matri_input.txt', 'r', encoding='utf-8-sig')
#
# 답
# 11 10 8 4 7
# 15 11 17 9 12
# 9 11 10 10 12
# 9 21 11 10 7
# 5 10 11 16 8
arr = [list(map(int, input().split())) for _ in range(5)]

N = len(arr)
M = len(arr[0])

# 순서 -> 상, 우, 하, 좌
dr = [-1, 0, 1, 0]      #row
dc = [0, 1, 0, -1]      #column
#
for i in range(0, N):
    for j in range(0, M):
        sum = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            #새로운 좌표가 범위를 벗어나면 스킵!
            if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr):
                #SKIP. 무시하고 다음 스텝으로 넘어가라
                continue
            #계산 -> 이웃한 요소와의 차의 절대값
            sum += abs(arr[i][j] - arr[nr][nc])
        print(sum, end =' ')
    print()