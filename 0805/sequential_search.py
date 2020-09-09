#완전탐색
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i+=1

    if i < n: return i
    else: return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 233
print(seq_search(arr, len(arr), key))