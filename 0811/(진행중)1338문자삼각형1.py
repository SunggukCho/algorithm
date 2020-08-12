# ASCII
# A : 65, Z : 90
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(0, N):
    for j in range(0, N):
        if i+j >= N-1:
            arr[i][j] = 1

print(arr)
