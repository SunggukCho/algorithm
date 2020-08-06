import sys
sys.stdin = open('binary.txt', 'r')

def binary(X, r):
    cnt = 0
    l = 1
    while l <= r:
        c = int((l + r) / 2)
        if X == c:
            return cnt
            break
        elif X > c:
            l = c
            cnt += 1
        elif X < c:
            r = c
            cnt += 1
    return False

T = int(input())
for tc in range(1, T+1):
    # 변수 할당
    r, A, B = map(int, input().split())
    #r: 전체 페이지 수
    #A: A가 찾을 페이지
    #B: B가 찾을 페이지

    cnt_A = binary(A, r)
    cnt_B = binary(B, r)

    if cnt_A > cnt_B:                       #cnt가 클수록 오래 걸린것이므로 반대로 출력한다.
        print('#{} {}'.format(tc, "B"))
    elif cnt_A < cnt_B:
        print('#{} {}'.format(tc, "A"))
    else:
        print('#{} {}'.format(tc, 0))
