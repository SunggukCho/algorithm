# 한강 조망권 문제
"""
풀이 순서
현재 나의 기준에서 왼쪽, 오른쪽으로 두 칸씩을 체크
그 중에서 내가 제일 크면 view 확보
"""
T = 10

for i in range(T):
    num = int(input())                                                   #테스트 자료 갯수 받기
    test = list(map(int, input().split()))                               #입력 테스트 리스트에 넣기
    result = 0

    for j in range(2, num - 2):
        top = max(test[j - 2], test[j - 1], test[j + 1], test[j + 2])    #기준 값의 앞 뒤 두 개씩 중 최대값 구하기
        if test[j] > top:                                                #만약 기준 값이 나머지 네 개의 최대값보다 크다면
            diff = test[j] - top                                         #기준값과 최대값만큼의 차이만큼은 view확보하므로 result에 추가
            result += diff

    print(f'#{i + 1} {result}')

