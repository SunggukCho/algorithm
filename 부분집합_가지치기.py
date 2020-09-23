def powerset(n, k, cursum): #n: 원소갯수, k:현재 depth
    global total
    if cursum >10: return
    total+=1                #출력횟수
    if n == k:
        print(n, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum + arr[k])
        A[k] = 0
        powerset(n, k+1, cursum)    #다음 요소 포함여부 결정


total = 0
arr = [1,2,3]
N=len(arr)
A = [0]*N

#print(total)
print(powerset(N,0,0))