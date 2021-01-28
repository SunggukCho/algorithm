'''
5 150   #지름길 갯수N, 고속도로 길이D
0 50 10 #지름길 시작, 도착, 길이
0 50 20
50 100 10
100 151 10
110 140 90

풀이
재귀로 하나씩 찾아간다.
현재 위치를 하나씩 땡기면서, 지름길을 하나씩 다 체크해본다
- 지름길이 이득이 없거나
- 누적이동거리가 D보다 크거나
- 그냥 고속도로로 달린거보다 크면 탈락(return)
'''
def find(loc, sum_dist):
    global minV
    if loc == D:    #도착
        if sum_dist < minV:
            minV = sum_dist
        return
    if loc > D:     #넘어가면 X
        return
    if sum_dist > D:
        return

    for i in fast_roads:
        s, e, d = i[0], i[1], i[2]
        if loc < s:     #지름길의 시작점까지 최단거리를 찾아서 간다.
            find(s, sum_dist + s-loc)
        elif loc == s:  #지름길의 시작점이 현 위치라면
            if (e-s) > d:       #지름길이 이득#이동거리에는 +d
                find(e, sum_dist + d)   #출발위치는 e로 이동
            else:       #지름길이 노이득 #그냥 고속도로로 이동
                find(e, sum_dist + (e-s))
        else:   #현 위치부터 지름길이 없다면 끝까지 이동
            find(D, sum_dist + (D-loc))


N, D = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]
fast_roads = sorted(roads, key=lambda x: x[0])  #sorting

minV = D
find(0, 0)
print(minV)
