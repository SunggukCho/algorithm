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

#호창's counting sort
def counting_sort(input_array, max_num):
    # counting_sort는 입력받는 숫자의 최댓값을 알아야 한다!
    # 각 인덱스에 해당되는 숫자의 갯수를 세어 담을 counting_array 설정
    # 0부터 max_num까지의 숫자를 담아야 하므로 배열의 크기는 max_num+1로 설정
    counting_array = [0] * (max_num + 1)
    # input_array에서 개별 요소들을 세, counting_array에 입력하자
    for num in input_array:
        counting_array[num] += 1
    # counting_array의 내용물을 갯수에서 좌표값으로 업데이트하자
    for i in range(1, max_num + 1):
        counting_array[i] += counting_array[i - 1]
    # output_array를 생성하자!
    # input_array만큼의 길이를 가진 리스트를 생성, 이 리스트에는 아직 입력되지 않은 칸에 -1 입력!
    output_array = [-1] * (len(input_array))
    # input_array에서의 숫자를 하나씩 짚어가며, counting_array를 참조해서 해당 값이 가진 좌표값을 찾는다.
    # 이 좌표값을 반영하여 해당 숫자를 output_array에 입력하고, 좌표값은 하나 줄여준다.
    for num in input_array:
        index = counting_array[num]
        # output_array는 0부터 시작하므로, index아닌 index-1임에 집중!
        output_array[index - 1] = num
        counting_array[num] -= 1
    return output_array