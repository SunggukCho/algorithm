#델타를 이용한 2차 배열 탐색
## 인덱스 체크 필수!
## 방문 체크 필수!

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

K = len(arr)
L = len(arr)

#시계방향 상하좌우 체크
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
"""
for x in range(K):          # x순회
    for y in range(L):      # y순회
        for i in range(4):  # 상하좌우 체크
            testX = x + dx[i]
            testY = y + dy[i]
            # 인덱스체크
            if testX >= 0 and testX < L and testY >= 0 and testY < K:
                print(arr[testX][testY], end = ' ')
"""

#강사님 풀이
#시계방향 상하좌우 체크
dr = [0, 0, -1, 1]      #row
dc = [-1, 1, 0, 0]      #column
for i in range(4):
    nr = 1 + dr[i]
    nc = 1 + dc[i]
    print(arr[nr][nc])
