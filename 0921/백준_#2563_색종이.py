T = int(input())
dots = [list(map(int, input().split())) for _ in range(T)]
Map = [[0]*101 for _ in range(101)]
for i in range(10):
    for j in range(10):
        for k in dots:
            R, C = k[0], k[1]
            if Map[100-(C+i)][(R+j)] == 0:
                Map[100-(C+i)][(R+j)] = 1
            else: continue

ans = 0
for i in range(101):
    for j in range(101):
        if Map[i][j] == 1:
            ans += 1
print(ans)