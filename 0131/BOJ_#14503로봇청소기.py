'''
유형: 구현, 시뮬레이션
현재 위치를 청소한다.
현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''
# 방향은 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 방향 바꿔주기
def change(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

def find(r,c,d):
    cnt = 1
    x = r
    y = c
    arr[x][y] = 2
    while(True):
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]
            # 유효 범위 안에 있고, 빈칸이라면
            if(0<=nx<n and 0<=ny<m and arr[nx][ny] == 0):
                cnt += 1
                x = nx
                y = ny
                arr[nx][ny] = 2
                d = dc
                empty = 1
                break
        # 4방향 모두 탐색 후 모든 칸이 청소가 되었다면
        if(empty == 0):
            # 후진
            if(d == 0):
                x += 1
            elif(d == 1):
                y -= 1
            elif(d == 2):
                x -= 1
            elif(d == 3):
                y += 1
            # 후진하려는 칸이 벽이라면 stop
            if(arr[x][y] == 1):
                break
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = find(r,c,d)
print(res)
