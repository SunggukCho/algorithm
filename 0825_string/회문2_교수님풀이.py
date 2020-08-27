def find(row, start, end):
    global cnt
    len = end-start+1
    half = len//2 if len % 2 == 0 else (len//2)+1
    s = []                              #stack
    for i in range(start, start+half):
        s.append(map[row][i])
    if len % 2 == 1:                    #길이가 홀수이면 stack에서 하나 버리고 비교함
        s.pop()
    if len != 1:
        for i in range(start+half, end+1):    #start에서 하프 지난 만큼부터 시작해서 끝까지 체크
            if s.pop() != map[row][i]:        #map[row][i]: 현재위치, 이것과 스택에서 뺀 값이 같지 않으면 바로 빠져나와라
                return
    #회문 발견
    if cnt < len:
        cnt = len  

T = 10
N = 100
for tc in range(1,T+1):
    pass