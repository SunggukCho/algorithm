'''
BOJ_#15685드래곤커브
https://www.acmicpc.net/problem/15685


'''
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#
N = int(input())
MAP = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    MAP[x][y] = 1
    move = []       #해당 x,y 좌표에서 앞으로 이동해야할 방향들의 모음
    move.append(d)
    print(x, y, d, g, move)
    for _ in range(g):  #세대 수 만큼 반복
        temp = []
        print(len(move))
        for i in range(len(move)):
            temp.append((move[-i-1]+1) % 4)
            print('temp', temp)
        move.extend(temp)
    print('move', move)
    for j in move:
        nx = x+dx[j]
        ny = y+dy[j]
        MAP[nx][ny] = 1
        x, y = nx, ny
ans = 0
for i in range(100):
    for j in range(100):
        if MAP[i][j]:
            if MAP[i+1][j] and MAP[i][j+1] and MAP[i+1][j+1]:   #한 점을 기준으로 오른쪽/아래/대각선 체크해서 있으면 조건만족
                ans += 1
print(ans)
