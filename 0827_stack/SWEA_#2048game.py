def game(arr, dir):
    #1. sorting
    ## Right
    M = len(arr)
    for i in range(M):
        


T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    N = int(N)
    arr = [input().split() for _ in range(N)]

    print(game(arr, M))