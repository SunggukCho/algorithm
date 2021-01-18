n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    num = arr.pop(0)
    arr_set = set(arr)
    maxN = maxV = 0
    for j in arr_set:
        if maxV < arr.count(j):
            maxV = arr.count(j)
            maxN = j
            if maxV > num / 2:
                ans = maxN
                break
            else:
                ans = "SYJKGW"

    print(ans)
