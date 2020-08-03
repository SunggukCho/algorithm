def counting_sort(A, B, k):
    C = [0] * k
    #카운팅
    for i in range(0, len(B)):
        C[A[i]] += 1
    #누적
    for i in range(1, len(C)):
        C[i] += C[i-1]

    #소트
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= A[i]

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
print(a)
print(b)

result = counting_sort(a, b, 5)
print(result)