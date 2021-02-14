'''
BOJ_#1167트리의지름
https://www.acmicpc.net/problem/1167
스택 방법이 아닌 재귀 방법으로 시도했으나 역시나 시간초과....
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

'''
import sys; sys.setrecursionlimit(100000)
import copy

def dfs(v, ans):
    global maxV
    if ans > maxV:
        maxV = ans
    if visited[v]:
        return
    visited[v] = 1
    if len(tree2[v]) == 0:
        return
    for i in range(len(tree2[v])):
        if visited[tree2[v][i][0]-1] == 0:
            pre = tree2[v][i][1]
            ans += pre
            dfs(tree2[v][i][0]-1, ans)
            ans -= pre
    return

v = int(input())
tree = [[] for _ in range(v)]
arr = [list(map(int, input().split())) for _ in range(v)]
for i in arr:
    vertex = i.pop(0)
    for j in range(0, len(i)-1, 2):
        tree[vertex-1].append([i[j], i[j+1]])

maxV = 0
for i in range(len(tree)):
    ans = 0
    tree2 = copy.deepcopy(tree)
    visited = [0]*v
    dfs(i, ans)

print(maxV)
