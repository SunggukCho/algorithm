"""
1
5 16
1 3 3 5 6
"""
#부분집합
def subset(n, k):
    global N, sum_subset, temp
    if n == N:
        for i in range(N):
            if bit[i]:
                temp+= arr[i]

        sum_subset.append(temp)
        temp = 0
        return
    bit[n] = 0
    subset(n+1, k)
    bit[n] = 1
    subset(n+1, k+1)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0]*len(arr)

    temp = 0
    sum_subset = []
    result = subset(0,0)

    # 부분집합의 모든 개수 구하고, 그 합을 구한다.
    # 그 중에서 B보다 크면서 가장 가까운 수를 구한다.
    ans = 9999
    for i in sum_subset:
        diff = i - B        #부분집합의 합에서 B를 뺀 차가 가장 작은 수(ans)를 구한다(양수만)
        if diff < 0:
            continue
        else:
            if diff < ans:
                ans = diff

    print('#%d %d' % (tc, ans))
