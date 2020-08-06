import sys
sys.stdin = open('partial_set.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, M = map(int, input().split())
    # N = 부분집합 원소의 갯수
    # M = 부분집합의 합
    L = len(A)

    cnt = 0
    for i in range(1 << L):                     #비트연산으로 부분집합 전체 구하기
        temp = []
        for j in range(L):                      #각 부분집합을 temp에 append
            if i & (1 << j):
                temp.append(A[j])
        if len(temp) == N and sum(temp) == M:   #temp의 len가 N과 같고, temp값의 합이 M인 경우 cnt +=1을 해준다
            cnt += 1

    print('#{} {}'.format(tc, cnt))
