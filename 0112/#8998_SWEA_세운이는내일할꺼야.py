"""
2
1
5 9
3
2 8
1 13
3 10
"""
def take_second(elem):
    return elem[1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    maxD = 0
    for _ in range(N):
        task, day = map(int, input().split())
        arr.append([task, day])
        if day > maxD:
            maxD = day

    new_arr = sorted(arr, key=take_second, reverse=True)
    add = 0
    for i in range(len(new_arr)-1):
        diff = new_arr[i][1] - new_arr[i+1][1]
        if diff >= new_arr[i][0]:   #같거나 크면 문제 안됨
            continue
        else:                       #더 작으면 그때부터 task를 시작하는 일정이 빨라져야 함.
            add += new_arr[i][0]-diff
    ans = new_arr[-1][1] - new_arr[-1][0] - add
    print('#{} {}'.format(tc, ans))
