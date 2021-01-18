n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    num = arr[0]
    arr = arr[1:]
    arr.sort()
    arr_set = set(arr)
    ans = "SYJKGW"
    for j in arr_set:
        if arr.count(j) > (num / 2):
            ans = j
            break
    print(ans)
