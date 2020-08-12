T = int(input())

arr = [[1 for _ in range(i)] for i in range(1, T+1)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j == 0 or j == len(arr[i])-1:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

arr_reversed = sorted(arr, reverse = True)
for i in arr_reversed:
    for j in i:
        print(j, end = ' ')
    print()