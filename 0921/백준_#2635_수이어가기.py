"""
주의사항.
무조건 1부터 완전탐색 해야함. 1일 경우에도 최대가 되는 경우가 있음.
처음 for문 돌릴 때 range내부의 범위가 중요.
"""
N = int(input())
max_len = 0
final_result = []
for k in range(1, N+1):
    result = [N]
    i = 0
    ans = N
    while ans >=0:
        i += 1
        if i == 1:
            ans = k
            result.append(k)
        else:
            ans = result[i-2] - result[i-1]
            if ans >=0:
                result.append(ans)
    if len(result) >= max_len:
        max_len = len(result)
        final_result=result
print(max_len)
for i in final_result:
    print(i, end=' ')
