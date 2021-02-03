A형 대비 2번 #1

# 문제 까먹기 전에. 배열에서 1은 집
# 도로 한 줄로 쫙 건설해서 제일 멀리 떨어진 집의 거리가 가장 짧은 경우
# r이랑 c라고 쓰면서도 칼럼이 기억 안 나서 axis라고 했네 ㅋㅋ

# 가로 도로 건설(모든 i에서)
def rowBuild(r):
    global result

    # 가로에 집 있으면 불능
    if sum(arr[r]):
        return
    # 현 도로에서 최장거리
    length = 0
    for k in range(num):
        length = max(length, abs(house[k][0] - r))

    # 이 경우는 생각해보니까 안 나오네 너무 빨리 푼 듯
    if length == 0:
        return

    if length < result:
        result = length


# 세로 도로 건설(모든 j에서)
def axisBuild(c):
    global result
    for k in range(H):
        if arr[k][c]:
            return

    length = 0
    for k in range(num):
        length = max(length, abs(house[k][1] - c))

    if length == 0:
        return

    if length < result:
        result = length


# i == 0에서 시작하는 우하 대각선 (j == W-1 에선 안 함)
def rowDownBuild(c):
    global result
    k = 0
    while c < W and k < H:
        if arr[k][c]:
            return
        k += 1
        c += 1

    # 각 대각선 별로 diff 값이 다름
    diff = k - c

    length = 0
    for k in range(num):
        # 집 역시 y좌표 - x좌표는 특정함
        # 최단 거리를 구할때 대각선이 무한히 길다고 가정하고
        # 대각선 방향으로 일직선 거리가 최단거리
        length = max(length, abs((house[k][0]-house[k][1])-diff))

    if length == 0:
        return

    if length < result:
        result = length


# j == 0 에서 우하 대각선 (i == H-1에선 안 함)
def axisDownBuild(r):
    global result
    k = 0
    while r < H and k < W:
        if arr[r][k]:
            return
        k += 1
        r += 1
    diff = r - k

    length = 0
    for k in range(num):
        length = max(length, abs((house[k][0] - house[k][1]) - diff))

    if length == 0:
        return

    if length < result:
        result = length

# j == 0 에서 우상 대각선 (i == 0에선 안 함)
def axisUpBuild(r):
    global result
    k = 0
    while 0 <= r and k < W:
        if arr[r][k]:
            return
        k += 1
        r -= 1
    diff = r - k

    length = 0
    for k in range(num):
        length = max(length, abs((house[k][0] - house[k][1]) - diff))

    if length == 0:
        return

    if length < result:
        result = length


# i == H-1 에서 우상 대각선 (j == W-1에선 안 함)
def rowUpBuild(c):
    global result
    k = H - 1
    while c < W and 0 <= k:
        if arr[k][c]:
            return
        k -= 1
        c += 1
    diff = k - c

    length = 0
    for k in range(num):
        length = max(length, abs((house[k][0] - house[k][1]) - diff))

    if length == 0:
        return

    if length < result:
        result = length


T = int(input())

for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = []
    # 집 위치 알아둠
    house = []
    for i in range(H):
        row = list(map(int, input().split()))
        for j in range(W):
            if row[j]:
                house.append((i, j))
        arr.append(row)

    # 집 갯수
    num = len(house)

    # 최장 거리는 99임. 즉 100은 나올 수 없는 거리
    result = 100
    for i in range(H):
        rowBuild(i)
        if i != 0:
            axisUpBuild(i)
        if i != H - 1:
            axisDownBuild(i)

    for j in range(W):
        axisBuild(j)
        if j != W - 1:
            rowDownBuild(j)
            rowUpBuild(j)

    # 100은 못 나오므로 도로를 못 만든 것
    if result == 100:
        result = -1

    print("#{} {}".format(tc, result))