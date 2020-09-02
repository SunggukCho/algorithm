import sys
sys.stdin = open('matrix_input.txt', 'r')
"""
풀이 접근
1. 0이 아닌 수를 발견하면 그 자리에서 오른쪽과 아래쪽으로 탐색을 시작
2. 0이 나올 때까지 탐색을 하고, 탐색을 끝마치면 중복 탐색을 방지하기 위해 0으로 바꾼다.
3. 이때 0이 아닌 부분의 가로와 세로 길이를 리스트에 넣는다. 
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())    #행렬 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    matrix = []

    for i in range(N):
        for j in range(N):
            k = 1
            l = 1
            if arr[i][j] != 0:              #0이 아닌 수를 발견하면
                arr[i][j]=0                 #0으로 바꿔 넣는다 (중복탐색 방지)
                while arr[i][j+k] != 0:     #0이 나올 때까지 열의 길이를 센다
                    arr[i][j+k] = 0
                    k += 1
                while arr[i+l][j] != 0:     #0이 나올 때까지 행의 길이를 센다
                    arr[i+l][j] = 0
                    l += 1
                for r in range(k):          #해당 행렬에 숫자 값이 남지 않도록 0으로 모두 없앤다.
                    for c in range(l):
                        arr[i+ c][j + r] = 0
                m = []
                m.append(l)
                m.append(k)
                matrix.append(m)

    #순서 정하기 - 가로x세로가 큰 순서대로 정렬(버블소트)
    for j in range(len(matrix)-1):
        for i in range(len(matrix)-1):
            size = matrix[i][0] * matrix[i][1]
            next_size = matrix[i+1][0] * matrix[i+1][1]

            if size > next_size:
                matrix[i], matrix[i+1] = matrix[i+1], matrix[i]

            if size == next_size:
                if matrix[i][0] > matrix[i+1][0]:
                    matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]

    matrix_num = len(matrix)
    numbers = str(matrix_num)+' '
    for i in matrix:
        for j in i:
            numbers = numbers + str(j) + ' '

    print('#{} {}'.format(tc, numbers))