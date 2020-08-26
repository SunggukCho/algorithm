#실행시간이 굉장히 빠르다

def leng(arr):
    result = 0
    for i in range(0, 100):
        for j in range(0, 100):
            forw, backw = j, j + 1
            count = 0
            while forw >= 0 and backw < 100 and arr[i][forw] == arr[i][backw]:
                count += 2
                forw -= 1
                backw += 1
            if count > result:
                result = count
            forw, backw = j, j + 1
            count = 0
            while forw >= 0 and backw < 100 and arr[forw][i] == arr[backw][i]:
                count += 2
                forw -= 1
                backw += 1
            if count > result:
                result = count
            forw, backs = j - 1, j + 1
            count = 1
            while forw >= 0 and backw < 100 and arr[i][forw] == arr[i][backw]:
                count += 2
                forw -= 1
                backw += 1
            if count > result:
                result = count
            forw, backw = j - 1, j + 1
            count = 1
            while forw >= 0 and backw < 100 and arr[forw][i] == arr[backw][i]:
                count += 2
                forw -= 1
                backw += 1
            if count > result:
                result = count
    return result


for t in range(0, 10):
    n = int(input())
    hang = [input() for _ in range(100)]
    print(f"#{n} {leng(hang)}")