'''
https://www.acmicpc.net/problem/15686
#BOJ_#15686 치킨배달
모든 경우의수를 다 돌아서 최소값 구하긴 했는데,
시간초과 안나온게 용한듯... 더효율적인 방법은 뭐가 있을까
'''
from itertools import combinations
def distance(r, c, x, y):
    dist = abs(r-x)+abs(c-y)
    return dist


N, M = map(int, input().split())    #M은 최대 치킨집의 갯수
MAP = [list(map(int, input().split())) for _ in range(N)]

houses = [] #집
total_stores = [] #치킨집
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            houses.append([i, j])
        elif MAP[i][j] == 2:
            total_stores.append([i, j])
        else:
            continue

# 상점의 조합을 구한다 -> 치킨집의 수가 M보다 크면 그냥 M개의 상점이라 생각
if len(total_stores) < M:
    M = len(total_stores)

#가능한 상점 조합
stores = list(combinations(total_stores, M))
ans = 999999
for i in stores:
    minV = 999999
    result = []
    for j in houses:
        tmp = 999999
        for k in i:
            dist = distance(j[0], j[1], k[0], k[1])
            if dist < tmp:
                tmp = dist
        result.append(tmp)
    if sum(result) < minV:
        minV = sum(result)
        if minV < ans:
            ans = minV
print(ans)
