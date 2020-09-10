import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)  #10^8 까지 늘림.

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r, c, cnt):
    global dist
    if dist < cnt:
        dist = cnt
    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:continue
        if matrix[nr][nc] == matrix[r][c]+1:
            dfs(nr, nc, cnt+1)

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cnt1 = 0
    maxr = maxc = 0
    for r in range(N):
        for c in range(N):
            dist = 0        #이번 탐색에서 최대 거리(dist) 찾기
            dfs(r,c,1)      #시작좌표 r, c, 거리
            if cnt1 < dist: #이번탐색으로 알아온 거리가 길면 갱신
                cnt1 = dist
                maxr = r
                maxc = c
            elif cnt1 == dist and matrix[r][c] < matrix[maxr][maxc]:
                #거리가 같을 경우, 방에 적힌 값이 작을 때만 갱신
                maxr = r
                maxc = c
    print('#{} {} {}'.format(tc, matrix[maxr][maxc], cnt1))