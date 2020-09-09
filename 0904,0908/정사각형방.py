import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)  #10^8 까지 늘림.

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def find(x,y):
    global cnt, minV
    visited[x][y] = 1
    for i in range(4):
        nr = x+dr[i]
        nc = y+dc[i]
        if nr >= 0 and nr < N and nc >= 0 and nc < N and visited[nr][nc] == 0 and arr[nr][nc] - arr[x][y] == 1:
            cnt += 1
            find(nr,nc)


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*(N) for _ in range(N)]

    cnt = 1
    result = []
    #if tc <= 8:
    for i in range(N):
        for j in range(N):
            find(i,j)
        result.append(cnt)
        cnt = 1
    print(max(result))
    #print('#{} {}'.format(tc, min_cnt))