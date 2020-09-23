"""
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
"""
def powerset(n, k):
    global N, result, temp
    if n == N:
        for i in range(N):
            if bit[i]:
                temp += arr[i]
        result.add(temp)
        temp = 0
        return
    bit[n] = 0
    powerset(n+1, k)
    bit[n] = 1
    powerset(n+1, k+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bit = [0] * N
    arr = list(map(int, input().split()))
    result = set()
    temp = 0
    powerset(0,0)

    print('#{} {}'.format(tc, len(result)))
