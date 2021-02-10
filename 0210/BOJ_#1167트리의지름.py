'''
BOJ_#1167트리의지름
https://www.acmicpc.net/problem/1167
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

'''
v = int(input())
tree = [[] for _ in range(v)]
arr = [list(map(int, input().split())) for _ in range(v)]
for i in arr:
    vertex = i.pop(0)
    for j in range(0, len(i)-1, 2):
        i[j], i[j+1]



