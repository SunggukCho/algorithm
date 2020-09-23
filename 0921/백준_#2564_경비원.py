"""
풀이접근
1. 동근 위치가 왼쪽인지, 오른쪽인지 파악.
2. 왼쪽 혹은 오른쪽이면 중앙으로부터 얼마나 떨어져 있는지 파악
3. 타겟도 왼쪽인지, 오른쪽인지 파악.
4. 동근이가 중앙으로부터 떨어져 있는 거리와 타겟이 중앙으로부터 떨어져 있는 거리를 비교
5.
"""
R, C = map(int, input().split())    #가로 ,세로
N = int(input())                    #고객 수
targets = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split())) #동근 출발 위치

results = []
for i in targets:
    if start[0] == 1:
        if start[0] == i[0]:
            ans = abs(start[1] - i[1])
            results.append(ans)
        elif i[0] == 2:
            Left = start[1]+i[1]+C
            Right = R-start[1]+R-i[1]+C
            if Left >= Right:
                results.append(Right)
            else:
                results.append(Left)
        elif i[0] == 3:
            ans = i[1]+start[1]
            results.append(ans)
        elif i[0] == 4:
            ans = i[1]+R-start[1]
    elif start[0] == 2:
        if start[0] == i[0]:
            ans = abs(start[1] - i[1])
            results.append(ans)
        elif i[0] == 1:
            Left = start[1] + i[1] + C
            Right = R - start[1] + R - i[1] + C
            if Left >= Right:
                results.append(Right)
            else:
                results.append(Left)
        elif i[0] == 3:
            ans = C-i[1]+start[1]
            results.append(ans)
        elif i[0] == 4:
            ans = C-i[1]+R-start[1]
            results.append(ans)
    elif start[0] == 3:
        if start[0] == i[0]:
            ans = abs(start[1] - i[1])
            results.append(ans)
        elif i[0] == 1:
            ans = start[1]+i[1]
            results.append(ans)
        elif i[0] == 2:
            ans = C-i[1]+start[1]
            results.append(ans)
        elif i[0] == 4:
            Left = start[1] + i[1] + C
            Right = R - start[1] + R - i[1] + C
            if Left >= Right:
                results.append(Right)
            else:
                results.append(Left)
    elif start[0] == 4:
        if start[0] == i[0]:
            ans = abs(start[1] - i[1])
            results.append(ans)
        elif i[0] == 1:
            ans = start[1]+R-i[1]
            results.append(ans)
        elif i[0] == 2:
            ans = C-start[1]+R-i[1]
            results.append(ans)
        elif i[0] == 3:
            Left = start[1] + i[1] + C
            Right = R - start[1] + R - i[1] + C
            if Left >= Right:
                results.append(Right)
            else:
                results.append(Left)
answer = sum(results)
print(answer)