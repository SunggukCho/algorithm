"""
풀이접근
1. 주어지는 높이 이하의 위치는 모두 0으로 변경
2. 이후 이중 for문을 돌면서, 사방탐색 DFS를 실시하고, DFS가 다 끝나면 return
3. DFS가 실행되는 횟수를 cnt로 체크
"""
import sys
sys.setrecursionlimit(100000)
def dfs(r,c):
    global cnt
    if G[r][c] == 1 or arr[r][c] == 0:
        cnt+=1
        return
    G[r][c] = 1
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        while nr < N and nc < N and nr >= 0 and nc >= 0:
            if arr[nr][nc] != 0 and G[nr][nc] == 0:
                dfs(nr,nc)
            else:
                break

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
G = [[0]*N for _ in range(N)]

max_height = 0
for i in arr:
    for j in i:
        if j > max_height:
            max_height = j

result = 1
flag = 1
while flag < max_height:
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= flag:
                arr[i][j] = 0
    for l in range(N):
        for m in range(N):
            dfs(l,m)
    ans = N*N-cnt
    if result < ans:
        result = ans
    flag+=1
    G = [[0] * N for _ in range(N)]

print(result)
