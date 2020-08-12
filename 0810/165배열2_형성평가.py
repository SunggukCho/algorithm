arr = [[0 for i in range(5)] for i in range(5)]

for i in range(len(arr)):
    for j in range(5):
        if i%2 == 0:
            arr[j][i] = 1

for i in range(1, 5):
    for j in range(5):
        if j == 0:
            arr[i][j] = arr[i-1][j+1]
        elif j == 4:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
print(arr)