#비트연산으로 부분집합 구하는 방법
arr = [1,2,3]
N = len(arr)

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end = ',')
    print()
print()
