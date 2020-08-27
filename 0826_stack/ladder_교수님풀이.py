import sys
sys.stdin = open('ladder.txt', 'r')

def search(r, c):       #r = row, c = column
    # delta. 왼, 오, 아래
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    N = 100
    num = ladder[r][c]                             #현재위치
    visited = [[0]*100 for _ in range(100)]        #방문배열

    while True:
        if num == 2: return True        #찾음
        if r == 99: return False        #못찾음

        for k in range(3):
            nr = r + dr[k]              #새로운 좌표(new row)
            nc = c + dc[k]              #새로운 컬럼(new col)

            #체크사항: 범위를 벗어나지 않는지, 이미 방문했었는지
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if ladder[nr][nc] == 0: continue
            if visited[nr][nc] == 1: continue
            r = nr                      #갱신
            c = nc                      #갱신
            num = ladder[nr][nc]        #갱신
            visited[nr][nc]=1           #방문 표시 남기기
            break                       #for 문 빠져나가기

T = 10
for tc in range(1, T+1):
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if ladder[0][i] == 1:       #시작점 찾기. 0행 순회-> 1인 곳을 찾아서 시작
            result = search(0, i)            #1인 곳의 좌표를 넘겨주고 탐색
        if result:
            cnt = i
    print('#{} {}'.format(tc, cnt))