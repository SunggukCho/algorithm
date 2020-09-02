"""
1. 입력값에 따라서 일단 해당 위치에 돌을 놓는다
2. 돌주변의 8방향을 탐색한다.
3. 내가 놓은 돌과 같은 색이 나올 때까지 탐색해보고 나오면 그 사이에 있는 모든 돌들의 색을 바꾼다
4. 아니면 그냥 두고 다른 방향을 다시 탐색한다.
"""
import sys; sys.stdin = open('오셀로.txt','r')

def check(arr, i, stone):
    global N
    r = board[i][0]-1
    c = board[i][1]-1
    #일단 요청 장소에 값 부터 삽입
    arr[r][c] = board[i][2]
    # 8방 탐색
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    reverse = []        #변화시킬 돌
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        while True:
            if nr < 0 or nc < 0 or nr >= N or nc >= N:  # 범위 벗어난 경우 초기화, break
                reverse = []
                break
            if arr[nr][nc] == 0:  # 빈 칸을 만난경우 reverse를 초기화
                reverse = []
                break
            if arr[nr][nc] == stone:  # 같은 색을 만났으므로 break
                break
            else:               # 조건에 부합하는 돌의 좌표를 reverse에 추가한다.
                reverse.append((nr, nc))
            nr, nc = nr + dr[k], nc + dc[k]  #nr과 nc를 한 칸 씩 더 간 좌표로 갱신한다.
        for row, col in reverse:  # 뒤집어준다.
            if stone == 1:
                arr[row][col] = 1
            else:
                arr[row][col] = 2
    return arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    #N은 판 크기, M은 플레이어가 돌 놓는 수
    #초기세팅 - 가운데에 돌 4개 놓기
    arr = [[0]*N for _ in range(N)]
    start = N//2-1
    for i in range(2):
        arr[start+i][start+i] = 2
    arr[start+1][start] = 1
    arr[start][start+1] = 1

    board = []
    for i in range(M):
        y, x, z = map(int, input().split())  #y, x, z 행, 렬, 돌 색
        temp = [x, y, z]
        board.append(temp)

    #결과 체크
    for i in range(M):
        result = check(arr, i, board[i][2])
    #출력
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if result[i][j] == 1:
                black += 1
            elif result[i][j] == 2:
                white += 1
            #핵심 포인트 : else가 아니라 elif다.
            #게임이 모두 흑돌과 백돌로 놓이지 않고 0이 남아있는 상태에서 끝날 수도 있음
            #이것 때문에 2시간 날림 ㅠ
    print('#{} {} {}'.format(tc, black, white))