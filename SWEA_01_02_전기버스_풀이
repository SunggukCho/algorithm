'''
K=3
3 10 5
1 3 5 7 9  -> 3씩이므로 1 3 5 7 9 이동에 문제 없음
3 10 5
1 3 7 8 9  -> 3과 7사이를 넘지 못함

1. 정류장 사이 간격이 k보다 작으면 가능, k보다 크면 불가능 -> 0
2. 마지막 충전 위치 저장 last
3. 충전 없이 현재위치로 올 수 없다면 last + k 가 현 위치 보다 작으면
   이전 충전소에서 충전을 해야함
1
3 10 5
1 3 5 7 9
'''

def find(v, k, n, m):
    v.insert(0, 0)    #0번 인덱스에 0을 넣음
    v.append(n)       #끝에 데이터를 넣음

    last = 0          #마지막 충전 했던 위치
    cnt = 0           #충전횟수
    for i in range(1, m+2):
        #충전기 사이가 k보다 멀면 종점 못감 -> 0 return
        if v[i] > v[i-1]+k:
            return 0
        if v[i] > last+k:
            last = v[i-1]    #현 위치 직전의 충전기에서 충전
            cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    #K: 한 번에 갈 수 있는 정류장 수
    #N: 종점
    #M: 충전기 설치 정류장 수
    K, N, M = map(int, input().split())
    v = list(map(int, input().split()))
    print(find(v, K, N, M))
