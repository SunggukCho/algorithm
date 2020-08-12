N, M = map(int, input().split())

for i in range(1, N+1):
    for j in range(1, M+1):
        if i % 2 == 1:
            print(j + (i-1)*5, end = ' ')
        else:
            print(i*5-j+1, end = ' ')
    print()