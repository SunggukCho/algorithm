def subset(k):
    if N == k:
        #전체 부분집합 모두 보여주기
        print(A)

    else:
        A[k] = 0
        subset(k+1)
        A[k] = 1
        subset(k+1)

arr = [1,2,3]       #선택할 원소
N = len(arr)        #원소의 개수
#원소 선택 여부 저장
A = [0]*N
subset(0)           #0번 원소에서부터 선택할지 말지 결정하러 가기
