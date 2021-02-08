'''
#BOJ_#17143낚시왕
https://www.acmicpc.net/problem/17143
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5

풀이접근
1. 상어들의 위치, 속력, 크기 좌표값으로 1초 뒤 상황을 구한다.
2. 1초 뒤 상황에서 같은 좌표에 혼자만 있는지 아니면 여러 마리가 같이 있는지 체크한다.
3. 혼자만 있으면 continue, 같이 있으면 크기(z)별로 비교해서 큰 놈만 남기고 나머지는 삭제
4. 상어끼리의 교통 정리가 되었으면, 낚시왕이 현 위치에서 아래로 내려와서 가장 가까운 상어를 잡는다.(이놈의 크기(z)만 result에 추가)
'''
from collections import deque
dr = [-1, 0, 1, 0]  #북동남서
dc = [0, 1, 0, -1]

def move(shark, MAP):
    for i in range(len(shark)):
        r, c, d, s, z = shark[i]
        r = r-1 #배열 idx이므로 1씩 빼줌
        c = c-1 #배열 idx이므로 1씩 빼줌
        nr = r + s * dr[d-1]
        nc = c + s * dc[d-1]

        if d == 1 or d == 3:
            if 0 <= nr < R: #정상범위
                pass
            else:           #비정상범위라면
                if nr < 0:  #nr이 0보다 작을 때는 절대값으로 변환
                    nr = abs(nr)
                if (nr // (R-1)) % 2 == 0:    #nr을 (행-1)로 나눈 몫이 2의 배수라면, 여러번 반복하더라도 원 위치로 복귀하고 위로 올라감
                    d = 3
                    nr = 0 + (nr % (R-1))
                else:                           #그렇지 않다면, 아래로 내려감
                    d = 1
                    nr = (R-1) - (nr % (R-1))
        else:
            if 0 <= nc < C:
                pass
            else:
                if nc < 0:
                    nc = abs(nc)
                if (nc // (C-1)) % 2 == 0:    #nc을 (열-1)로 나눈 몫이 2의 배수라면, 여러번 반복하더라도 원 위치로 복귀하고 오른쪽으로감
                    d = 2
                    nc = 0 + (nc % (C-1))
                else:                           #아니면 왼쪽으로감
                    d = 4
                    nc = (C-1) - (nc % (C-1))
        MAP[r][c] = 0                           #기존 상어 위치 변경
        MAP[nr][nc] = [s, d, z]                 #새로운 상어 위치 반영
        shark[i] = [nr+1, nc+1, s, d, z]


R, C, M = map(int, input().split())
MAP = [[0] * (C) for _ in range(R)]
sharks = deque()

for m in range(M):
    r, c, s, d, z = map(int, input().split())
    MAP[r-1][c-1] = [s, d, z]
    sharks.append([r, c, s, d, z])




