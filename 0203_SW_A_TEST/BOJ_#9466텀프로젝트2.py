'''
자체 사이클인 노드는 제외
사이클 생성될 때 마다 v_visited값을 return해서 집합에 추가
해당 정점이 사이클 집합에 포함되어 있으면 DFS 하지 않도록
-> 이렇게 해도 시간초과.... ㄷㄷ
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''

from collections import deque
def dfs(v, visited, v_visited):
    global flag
    visited[v] += 1
    v_visited.append(v)
    Q = deque()
    if chosen[v] == v:
        flag = True
        return v_visited
    else:
        Q.append(chosen[v])
    while len(Q):
        next = Q.popleft()
        if next not in v_visited:
            v_visited.append(next)
        else:
            flag = True
            return v_visited
        if visited[next] == 0:
            visited[next] = 1
            if chosen[next] != next:
                Q.append(chosen[next])
    return v_visited


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    chosen = list(map(int, input().split()))
    chosen.insert(0, 0) # 맨 앞에 한 칸 0 넣어주기

    result = set()  #사이클 정점들의 집합
    for i in range(1, n+1):
        if i in result:
            continue
        visited = [0]*(n+1)
        v_visited = []
        flag = False
        dfs(i, visited, v_visited)
        if flag == True:
            tmp = set(v_visited)
            result.update(tmp)
    print(n-len(result))
