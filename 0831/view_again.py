import sys; sys.stdin = open('view_input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr= list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            top = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            diff = arr[i]-top
            result += diff

    print(result)