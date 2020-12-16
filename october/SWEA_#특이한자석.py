"""
0번 index: 답
1번 자석의 붙어있는 부분: index 2
2번: index 2, 6
3번: index 2, 6
4번: index 6
"""
def rotate(idx, turn):
    #1. 회전 하는지 안하는지 체크 (magnet[2]와 다음 magnet[6]이 다르면 True)
    turnOrNot = [0]*4
    turnOrNot[idx-1] = turn
    #오른쪽방향
    for i in range(idx - 1, 3):
        if magnets[i][2] == magnets[i+1][-2]:
            break
        else:
            turnOrNot[i+1] = 1
    #왼쪽방향
    for i in range(idx-1, 0, -1):
        if magnets[i][6] == magnets[i-1][2]:
            break
        else:
            turnOrNot[i-1] = 1
    #2. 회전의 방향 1, -1로 맞춰주기
    for j in range(len(turnOrNot)):
        if turnOrNot[j] != 0:
            if abs((idx-1)-j) == 1:
                turnOrNot[j] = -turn
            elif abs((idx-1)-j) == 2:
                turnOrNot[j] = turn
            elif abs((idx - 1) - j) == 3:
                turnOrNot[j] = -turn

    #3. 회전 방향에 따라 magnet회전시키기
    ## 1. 시계방향 (1) -> 맨 뒤에꺼를 뽑아서 1번 으로 insert
    ## 2. 반시계방향 (-1) -> 맨 앞에꺼를 뽑아서 맨 뒤로 append
    for k in range(4):
        if turnOrNot[k] == 1:
            last = magnets[k].pop()
            magnets[k].insert(0, last)
        elif turnOrNot[k] == -1:
            first = magnets[k].pop(0)
            magnets[k].append(first)

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        idx, turn = map(int, input().split())
        rotate(idx, turn)

    ans = 0
    for i in range(4):
        if magnets[i][0] == 1:
            ans += 2 ** i

    print('#{} {}'.format(tc, ans))
