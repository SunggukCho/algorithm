'''
https://www.acmicpc.net/problem/15686
#BOJ_#15686 치킨배달
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
result = []
if len(total_stores) > M:
    minTmp = 999999
    for i in range(1, M+1):
        store = list(combinations(total_stores, i))
        for j in range(len(store)):
            minV = 999999
            tmp = []
            for k in range(len(houses)):
                dist = distance(houses[k][0], houses[k][1], store[j][i-1][0], store[j][i-1][1])
                tmp.append(dist)
            print(store[j], tmp)
            if sum(tmp) < minTmp:
                minTmp = sum(tmp)
        result.append(minTmp)
else:
    result = []
    stores = total_stores
    for i in range(len(houses)):
        minV = 999999
        for j in range(len(stores)):
            dist = distance(houses[i][0], houses[i][1], stores[j][0], stores[j][1])
            if dist < minV:
                minV = dist
        result.append(minV)
print(sum(result))
