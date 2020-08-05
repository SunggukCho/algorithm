#이진탐색
def binary_search(arr, key):
    start = 0
    end = len(arr)
    while start <= end:
        middle = (start+end) // 2
        #경우의 수 1. key값과 middle이 같은 경우
        if arr[middle] == key:
            return True, middle

        #경우의 수 2. key값이 middle보다 큰 경우
        #end를 미들보다 작게 만들어준다
        elif arr[middle] > key:
            end = middle - 1

        #경우의 수 3. key값이 middle보다 작은 경우
        #start를 middle보다 크게 만들어준다
        else:
            start = middle + 1
    return False, -1

arr = [ 2, 4, 7, 9, 11, 19, 23]
key = 19
print(binary_search(arr, key))