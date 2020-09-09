#선택정렬
def selection_sort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[min], a[i] = a[i], a[min]

arr = [64, 25, 10, 22, 11]
selection_sort(arr)
print(arr)