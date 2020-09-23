"""
풀이접근
1. 4방 탐색 시, 한 칸만 가는게 아니라 끝까지 가도록 함. (While)
2. 한 곳이라도 하나라도 뚫려있다면 외부
3. 외부영역 중, 4방탐색 시 바로 옆에 0이 2개 이상이면 다음에 사라짐
함수 2개.
1. 외부인지/내부인지
2. 사라지는지 남는지
"""
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def inout(cheese, r, c):
    #out이면 1 return, in이면 0 return
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        while nr < N and nr >= 0 and nc < M and nc >= 0:
            if cheese[nr][nc]==0:
                nr = nr+dr[i]
                nc = nc+dc[i]
            elif cheese[nr][nc]:
                cnt += 1
                break
    if cnt == 4:
        return 0
    else:
        return 1

def gone(cheese, r, c):
    global disappear
    if inout(cheese, r, c) and cheese[r][c] != 0:
        cnt = 0
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < N and 0 <= nc < M and cheese[nr][nc] == 0:
                cnt += 1
                if cnt >= 2:
                    disappear.append([r,c])
                    break
    else:
        return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
G = [[0]*M for _ in range(N)]
disappear = []

cheese_count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese_count += 1

result = 0
while cheese_count > 0:
    result += 1
    for i in range(N):
        for j in range(M):
            gone(arr, i, j)
    disappear_cnt = len(disappear)
    print(disappear)
    for k in disappear:
        arr[k[0]][k[1]] = 0
    disappear = []

    cheese_count -= disappear_cnt

print(result)
