def perm(k):    #k는 선택한 원소값이 sel 배열에 들어갈 위치를 의미함
    if k == N:
        print(sel)
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                sel[k] = arr[i]     #sel의 k값에 arr[i]를 넣어준다
                visited[i] = 1      #사용했으니 visited[i]에 1넣어줌
                perm(k+1)           #이 작업을 재귀로 반복한다
                visited[i] = 0      #이 부분이 제일 중요! 현재 선택을 취소쉬켜서 다시 뒤로 돌아갈 수 있도록 하는 것임
                #sel은 어차피 덮어 씌워지므로, 초기화 할 필요가 없다.

arr = [1,2,3]
N = len(arr)
sel = [0]*N
visited = [0]*N

perm(0)
