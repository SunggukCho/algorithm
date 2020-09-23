def subset(n, k):
    if n == N:
        #출력
        for i in range(N):
            if bit[i]:
                print(arr[i], end=' ')
        print()
        return
    #선택, 비선택
    bit[n] = 0  #비선택
    subset(n+1, k)
    bit[n] = 1  #선택
    subset(n+1, k+1)


arr = [1,2,3]       #선택할 원소가 모인 배열
N = len(arr)

bit = [0] * N       #원소 선택여부 저장
subset(0,0)         #부분집합 함수 호출
