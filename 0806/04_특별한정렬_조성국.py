import sys
sys.stdin = open('special.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    asc = sorted(arr)                   #오름차순 정렬
    dsc = sorted(arr, reverse = True)   #내림차순 정렬

    special_arr = []
    for j in range(5):                  #새로운 배열에 내림차순 부터 append
        special_arr.append(dsc[j])

    for k in range(5):                  #홀수 인덱스에 오름차순 insert
        n = 2*k+1
        special_arr.insert(n,asc[k])

    str_arr = ''                        #List안에 있는 값들을 순회하면서 string으로 변화하여 concatenate
    for l in special_arr:
        temp = str(l)
        str_arr += temp+' '
    print('#{} {}'.format(tc, str_arr))