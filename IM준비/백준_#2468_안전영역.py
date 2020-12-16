"""
풀이접근
1. 주어지는 높이 이하의 위치는 모두 0으로 변경
2. 이후 이중 for문을 돌면서, 사방탐색 DFS를 실시하고, DFS가 다 끝나면 return
3. DFS가 실행되는 횟수를 cnt로 체크
특징
1. 기본 지형 정보를 arr에 담았고, G는 arr와 똑같은 크기이지만 모두 0인 인접행렬을 만들어 visited여부만 체크해줬다.
"""
import sys
sys.setrecursionlimit(100000)
def dfs(r,c):                               #내가 갈 수 있는 길은 모두 다 가고 가고나서 흔적을 남기겠다.
    global cnt
    if G[r][c] == 1 or arr[r][c] == 0:      #이미 방문했던 곳이거나, 침수된 곳이면
        cnt+=1                              #cnt+=1
        return                              #하고 빠져나와라
    G[r][c] = 1                             #처음 간 곳이면 흔적 남겨라
    dr = [-1,0,1,0]                         
    dc = [0,1,0,-1]

    for i in range(4):                      #사방으로 탐색해라
        nr = r+dr[i]
        nc = c+dc[i]
        while nr < N and nc < N and nr >= 0 and nc >= 0:
            if arr[nr][nc] != 0 and G[nr][nc] == 0:
                dfs(nr,nc)                  #조건에 맞으면 재귀
            else:
                break

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]#지도정보
G = [[0]*N for _ in range(N)]       #arr와 동일 크기의 인접행렬

max_height = 0              #가장 높은 지대의 높이
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
            if arr[i][j] <= flag:   #지대가 현재 flag보다 낮으면 모두 0처리
                arr[i][j] = 0
    for l in range(N):
        for m in range(N):          #바뀐 arr를 기준으로 모든 지역 dfs탐사
            dfs(l,m)
    ans = N*N-cnt
    if result < ans:                #result가 현재 ans보다 작으면 result를 ans로 대체해서 최대값 찾기
        result = ans
    flag+=1
    G = [[0] * N for _ in range(N)] #G값 초기화

print(result)
