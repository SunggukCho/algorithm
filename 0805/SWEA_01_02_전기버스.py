import sys
sys.stdin = open('sample_input_bus.txt', 'r')                      #파일로 input받기

T = int(input())
for tc in range(1, T + 1):
    k, n, m = map(int, input().split())     #k = 최대 이동거리, n = 정류장 수, m = 정류장 수
    arr = list(map(int, input().split()))   #정류장만 있는 곳을 arr 만들어주기 [ 1, 3, 5, 7, 9]

    stop = [0]*n                   #일단 정류소 배열에 0 집어넣고

    for i in range(m):             #m을 순회하면서 정류소가 있는 곳에 1을 넣어준다 [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        stop[arr[i]] = 1

    j = 0
    loc = 0                    #현재위치
    loc2 = k                   #현재위치에서 k만큼 더 간 가상위치
    cnt = 0                    #충전 횟수

    while 1:
        if loc2 >= n:          #loc2가 배열의 끝에 도착하거나 넘어가면, 도착완료!
            print("#{} {}".format(tc, cnt))
            break
        if stop[loc2] == 1:    #k만큼 떨어진 lo2에 1이 있다면, 여기까지는 충전 없이 갈 수 있고 여기서 충전하면 된다.
            cnt += 1  # Find the Gas station
            loc = loc2
            loc2 += k
        else:                  #k만큼 떨어진 loc2에 1이 없다면 loc2를 하나 줄여서 다시 검사해본다. 이 과정은 loc과 loc2가 같아질때까지 반복한다.
            loc2 -= 1
            if loc2 == loc:    # 만약 loc2가 loc과 같아진다면, 그 사이에 충전소가 없다는 것이므로 더 이상 진행할 수 없다.
                print("#{} {}".format(tc, 0))
                break
