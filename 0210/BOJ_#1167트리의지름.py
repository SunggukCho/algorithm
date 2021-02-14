'''
BOJ_#1167트리의지름
https://www.acmicpc.net/problem/1167
문제를 풀다가 김구현 교수님과의 매터모스트 토크로 인해 집중력이 흐트러져 버렸지만 오랜만에 즐거운 대화 나눴음 ㅎㅎ
처음에는 DFS로 계속 파고드는 방식으로 진행했었더니, 그냥 지름이 아니라 그래프로 연결된 지점을 탐색하는 최대값을 구해버렸다.
이후 ~로 수정해서 진행하는 와중에 팀원의 헬프요청이 와서 또 샛길로 빠졌다.

흠.... 그래서 그런지 망했다.
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

'''
from collections import deque
import copy

def dfs(v, ans):
    maxV = 0
    Q = deque()
    visited[v] = 1
    for i in tree2[v]:
        Q.append(i)
    while len(Q):
        V, E = Q.popleft()
        for i in tree2[V-1]:
            NV, NE = i[0], i[1]
            if visited[NV-1] == 0:
                visited[NV-1] = 1

                Q.append([NV, NE+ans])
                if NE+ans > maxV:
                    maxV = NE+ans
    return maxV


v = int(input())
tree = [[] for _ in range(v)]
arr = [list(map(int, input().split())) for _ in range(v)]
for i in arr:
    vertex = i.pop(0)
    for j in range(0, len(i)-1, 2):
        tree[vertex-1].append([i[j], i[j+1]])

res = 0
for i in range(len(tree)):
    ans = 0
    tree2 = copy.deepcopy(tree)
    visited = [0]*v
    answer = dfs(i, ans)
    if answer > res:
        res = answer
print(res)
