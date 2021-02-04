'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

그래프에서 사이클이 없는 노드들의 갯수를 구하는 문제
DFS로 탐색을 하면서 처음 진입한 노드로 돌아오지 않는 노드들을 한 배열에 모아두고 그 갯수를 출력
-> 시간초과
이 방식은 모든 그래프에서 DFS순회를 끝까지 다 돌고 사이클의 갯수를 찾기 때문에 시간초과가 난다.
'''
from collections import deque
def dfs(v):
    visited[v] += 1
    Q = deque()
    if chosen[v-1] != v:
        Q.append(chosen[v-1])
    else:
        return v
    while len(Q):
        next = Q.popleft()
        if visited[next] == 0:
            visited[next] += 1
            if chosen[next-1] != next:
                Q.append(chosen[next-1])
    return next


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    chosen = list(map(int, input().split()))

    result = 0
    for i in range(1, n+1):
        visited = [0]*(n+1) #방문배열
        ans = dfs(i)
        print(i, ans)
        if i != ans:
            result += 1
    print(result)
