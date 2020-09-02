#부분집합의 합이 10인 부분집합의 개수 찾기
N = 10      #원소의 집합
K = 10      #부분집합의 합

arr = [i+1 for i in range(N)]
A = [0]*N
cnt = 0

def subset(k):
    global cnt
    if k == N:
        if sum(A) == K:
            cnt += 1
            print('부분집합: {} {}개'.format(A, cnt))
    else:
        A[k] = 0
        subset(k+1)
        A[k] = 1
        subset(k+1)

print(subset(0))
