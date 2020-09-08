import sys; sys.stdin = open('miro.txt','r')

def dfs(sr, sc):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    s = []      #스택
    #1. 탐색시작점 스택에 넣기
    s.append([sr, sc])
    while len(s) != 0:
        n = s.pop()
        #2. 새로운 탐색 좌표 계산(4방 탐색)
        for k in range(4):
            nr = n[0] + dr[k]
            nc = n[1] + dc[k]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                #3. 도착점인지 체크
                if arr[nr][nc] == 3:
                    return 1            #찾음!
                elif arr[nr][nc] == 0:
                    s.append([nr,nc])
                    arr[nr][nc] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]

    sr, sc = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:              #탐색시작
                sr, sc = i, j               #출발점 찾기

    result = dfs(sr,sc)
    print(result)
