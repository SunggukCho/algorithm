import sys; sys.stdin = open('pizza.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        #N 화덕 크기 #M피자 갯수
    #cheese
    arr = list(map(int, input().split()))
    pizza = []                              

    for i in range(len(arr)):               #나중에 찾기 위해서 치즈와 idx를 같이 표기해야함.
        pizza.append([i+1, arr[i]])

    Q = [pizza[i] for i in range(N)]        #화덕 크기 N에 맞춰서 Q를 만들고, 못들어간 친구들은 R에 넣어줌
    #아직 화덕에 안들어간 피자 모음
    R = []
    for i in pizza:                         #pizza 중에서 화덕크기가 작아 못들어간 친구들
        if i not in Q:
            R.append(i)

    while True:
        temp = Q.pop(0)                     #하나 뽑아서 확인하기
        if temp[1] // 2 == 0:               #뽑은 수의 치즈를 반으로 줄여봤을 때 0이라면
            if len(R) != 0:
                elem = R.pop(0)             #R이 0이 아니면 아직 남아있는거니까 다시 화덕에 넣어준다.
                Q.append(elem)              #회전의 의미로 화덕의 뒤에 append해준다.
            elif len(R) == 0 and len(Q) == 1:#R이 비어있고, Q가 하나만 남았다면 이게 답이다.
                ans = Q[0][0]                #이때의 Q[0][0]은 처음 pizza의 idx를 나타낸다.
                break                       #반복문 종료
        else:                               #뽑은 수의 치즈를 반으로 줄여봤을 때 0이 아니라면, 치즈양 반으로 줄여서 다시 넣기
            temp[1] = temp[1]//2
            Q.append([temp[0], temp[1]])    #회전의 의미로 Q의 뒤에 넣어준다.

    print('#{} {}'.format(tc,ans))
