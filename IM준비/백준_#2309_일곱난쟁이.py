"""
20
7
23
19
10
15
25
8
13
"""
"""
풀이.
9난쟁이의 키의 합에서 임의로 두 명 키 빼서 7명의 합이 100이면 찾음.
가장 핵심은 반복문을 돌리다가 답을 찾으면 break해서 빠르게 빠져나와야함. 
안그러면 runtime error의 늪에서 빠져나올 수 없음.
"""
dwarfs = [int(input()) for _ in range(9)] #9난쟁이 키
dwarfs.sort()                             #순서대로 정렬
total = sum(dwarfs)                       #total = 9난쟁이 키의 합

break_tool = True                         #나중에 break할 때 써먹으려고 미리 설정
for i in range(9):
    for j in range(i+1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:    #핵심 로직: 전체 - 임의의 두명의 키 == 100이면 조건 충족.
            for k in range(9):                      #9명의 난쟁이 중 i,j가 아닌 것들 출력
                if k==i or k==j: continue           #i, j는 진짜 난쟁이가 아니므로 k는 i, j가 같을 때 continue로 스킵한다.
                else:
                    print(dwarfs[k])                #k가 i, j와 다르면 출력한다.
            break_tool = False                      #출력을 완료하면 break_tool을 False로 전환하고
        if break_tool == False:                     #조건문을 통해 7명을 색출해냈다면 (break_tool이 False로 전환) 이중 for문을 모두 break해서 탈출.
            break
    if break_tool == False:
        break