"""
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
"""
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(6):          #첫 3개 나올때까지는 어차피 triplet이나 run 안나오니까 그냥 player1, 2에 넣음
        if i%2 == 0:
            player1.append(arr[i])
        else:
            player2.append(arr[i])
    rests = [arr[k+6] for k in range(6)]
    p1_tri, p1_run, p2_tri, p2_run = 0, 0, 0, 0
    ans = 0
    cnt = 0
    while p1_tri+p1_run+p2_tri+p2_run == 0: #네 개 값 중에 하나라도 먼저 나오면 끝, 만약 끝까지 안나오면(len(player1)+len(player2)==12) 종료
        player1.sort()
        player2.sort()
        #1. player1 에서 triplet or run이 있는지 체크. 없으면 rests.pop(0)을 append 해준다.
        if ans != 1 and ans != 2:
            for i in range(0, len(player1)-2):
                if player1[i]==player1[i+1]==player1[i+2]:
                    p1_tri += 1
                    ans = 1
                    break
                elif player1[i]+1 == player1[i+1] and player1[i+1] +1 == player1[i+2]:
                    p1_run += 1
                    ans = 1
                    break
                else:
                    if i == len(player1)-3 and len(rests) != 0:
                        player1.append(rests.pop(0))

        # 2. player2 에서 triplet or run이 있는지 체크. 없으면 rests.pop(0)을 append 해준다.
        if ans != 0:
            break
        else:
            for i in range(0, len(player2) - 2):
                if player2[i] == player2[i+1] == player2[i+2]:
                    p2_tri += 1
                    ans = 2
                    break
                elif player2[i] + 1 == player2[i+1] and player2[i+1] + 1 == player2[i+2]:
                    p2_run += 1
                    ans = 2
                    break
                else:
                    if i == len(player2)-3 and len(rests) != 0:
                        player2.append(rests.pop(0))
        cnt += 1
        if cnt >= 4:
            break
    print('#{} {}'.format(tc, ans))
