import sys
sys.stdin = open('matrix_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    #행렬 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            width = 0
            height = 0
            if arr[i][j] != 0:
                dx = j
                while True:
                    dx += 1
                    if dx >= N:
                        break
                    if arr[i][dx]:
                        width += 1
                    else:
                        break
                print(width)


