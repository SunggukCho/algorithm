'''
BOJ_#3190뱀
https://www.acmicpc.net/problem/3190


'''
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
arr = [[0]*N for _ in range(N)] #사과 없으면 0, 사과 있으면 1표시
turn = deque()
for l in range(L):
    x, y = input().split()  #L = -1, D = +1
    if y == 'L':
        turn.append([int(x), -1])
    else:
        turn.append([int(x), 1])
# print(apple)
# print(turn)
for i in apple: #사과 있는 곳은 1로 표기
    arr[i[0]-1][i[1]-1] = 1

idx = 0
result = 0
Q = deque()     #지나가는 path
Q.append((0, 0, 1))
snake = deque() #사라져야할 path
while Q:
    r, c, d = Q.popleft()
    flag = False        #사과 먹었는지 아닌지
    if len(turn) != 0 and turn[0][0] == idx:
        time, dir = turn.popleft()
        d += dir
    arr[r][c] = 2   #2
    nr = r+dr[d]
    nc = c+dc[d]
    if nr >= N or nr <0 or nc >= N or nc < 0:   #벽에 부딪힌 경우
        result = idx
        break
    if False:    #자기 꼬리 무는 경우
        pass
    if arr[nr][nc] == 1:# 사과 발견
        flag = True

    print(r, c, d)
    for row in arr:
        print(row)
    print()

    if flag:
        arr[r][c] = 2
    else:
        arr[r][c] = 0

    Q.append((nr, nc, d))
    idx += 1
print(result+1)