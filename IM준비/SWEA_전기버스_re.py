"""
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
"""
"""
풀이
1. 끝에 도착했는가? 했으면 return 1, 아니면 0
2. 현재 정류소 인가? 정류소이고 현재 남은 에너지가 다음 정류장까지 갈 수 있는가?
3. 현재 정류소가 아닌가? 남은 에너지로 다음 정류장까지 갈 수 있는가?
"""

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 1
    stations = []
    loc = 1 #현재위치
    energy = K
    while loc <= N:
        print(loc, energy, stations)
        if loc == N:                        #끝 도착
            ans = 1
            break
        elif loc != N and energy <= 0:                     #에너지 고갈
            ans = 0
            break
        if loc not in arr:
            if energy == 0:
                ans = 0  # retire
                break
            else:
                energy -= 1
                loc += 1
                continue
        elif loc in arr:
            idx = arr.index(loc)
            if idx+1 != len(arr):
                next_station = arr[idx+1]
            #남은 에너지로 N까지 갈 수 있는가?
            if N-loc < energy:
                ans = 1
                break
            else:
                #다음 정류소 - 현재위치 > energy?
                if next_station - loc < energy:
                    # 이번 정류소 스킵
                    energy -= 1
                    loc += 1
                else:
                    # 이번 정류소에서 충전
                    stations.append(loc)
                    energy = K
                    loc += 1
                    continue


    if ans == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, len(stations)))