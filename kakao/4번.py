n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
min_fare = 0
visited = [0]*(n+1)
new_fares = []
for i in fares:
    if i[0] != i[1]:
        j = [i[1], i[0], i[2]]
        new_fares.append(i)
        new_fares.append(j)

def solution(n, s, a, b, fares):







    answer = 0
    return answer

def dfs(v):
    global min_fare, a
    visited[v] = 1
    print(v)
    if v == a:
        print(v, '도착')
        return
    else:
        for i in new_fares:
            if v == i[0] and visited[i[1]] == 0:
                min_fare += i[2]
                dfs(i[1])
    return
dfs(s)
