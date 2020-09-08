def comb(n,r):
    #n원소 index, r:어디에 넣을지
    if r == N:          #조합 다고름
        print(sel)
        return
    elif n >= len(arr):
        return
    sel[r] = arr[n]
    comb(n+1, r+1)      #r위치의 원소 선택한 경우
    comb(n+1, r)        #r위치의 원소 선택 안함

arr = [1,2,3]
N = 2
sel = [0]*N
comb(0,0)