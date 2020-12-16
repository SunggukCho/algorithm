import sys; sys.stdin = open('code.txt', 'r')

def translator(arr):
    #이진수를 10진수로 변환
    code_dict = {
        0: [0, 0, 0, 1, 1, 0, 1],
        1: [0, 0, 1, 1, 0, 0, 1],
        2: [0, 0, 1, 0, 0, 1, 1],
        3: [0, 1, 1, 1, 1, 0, 1],
        4: [0, 1, 0, 0, 0, 1, 1],
        5: [0, 1, 1, 0, 0, 0, 1],
        6: [0, 1, 0, 1, 1, 1, 1],
        7: [0, 1, 1, 1, 0, 1, 1],
        8: [0, 1, 1, 0, 1, 1, 1],
        9: [0, 0, 0, 1, 0, 1, 1],
    }
    for i in range(10):
        if code_dict[i] == arr:
            result = i
            break
    return i


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = []
    for i in range(N):
        code = list(map(int, input()))
        codes.append(code)

    # 뒤에서 처음 1나오는 것을 flag로 설정
    flag = 0
    for code in codes:
        for i in range(len(code)-1, 0, -1):
            if code[i] == 1:
                flag = i
                break

    # flag에서 56자씩(secrets) 자르고 그 중에 7자씩(secret) 자름.
    secrets = []
    code = []
    for i in codes:
        if sum(i) != 0:
            code = i
    for j in range(flag, flag-56, -7):
        if code[j] == 1:
            secret = []
            for k in range(7):
                secret.insert(0, code[j-k])
            secrets.append(secret)

    #secrets는 현재 거꾸로 들어와있음
    odd = []
    even = []
    for k in range(len(secrets)):
        if k % 2 == 0:
            ans = translator(secrets[k])
            even.append(ans)
        else:
            ans = translator(secrets[k])
            odd.append(ans)
    result = sum(odd)*3 + sum(even)
    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(odd)+sum(even)))
    else:
        print('#{} {}'.format(tc, 0))
