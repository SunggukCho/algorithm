def distance(r, c, x, y):
    dist = abs(r-x)+abs(c-y)
    return dist


def powerset(n, k):
    global minV
    if n == k:
        groupA = []
        groupB = []
        Q_A = []
        Q_B = []
        for i in range(len(people)):
            if A[i] == 1:
             groupA.append(people[i])
            elif A[i] == 0:
             groupB.append(people[i])

        for i in range(len(groupA)):
            tmp_dist = distance(exitA[0], exitA[1], groupA[i][0], groupA[i][1])
            Q_A.append(tmp_dist)
        for i in range(len(groupB)):
            tmp_dist = distance(exitB[0], exitB[1], groupB[i][0], groupB[i][1])
            Q_B.append(tmp_dist)
        Q_A.sort()
        Q_B.sort()
        ansA = 0
        ansB = 0
        if len(Q_A) != 0:
            if Q_A[0] + len(Q_A) > Q_A[-1]:
                ansA = Q_A[0] + len(Q_A)
            else:
                ansA = Q_A[-1] + 1
        if len(Q_B) != 0:
            if Q_B[0] + len(Q_B) > Q_B[-1]:
                ansB = Q_B[0] + len(Q_B)
            else:
                ansB = Q_B[-1] + 1
        minV = min(minV, max(ansA, ansB))
        return minV

    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    people = []
    exit = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                people.append([i, j])
            elif MAP[i][j] == 2:
                exit.append([i, j])

    exitA = exit[0]
    exitB = exit[1]

    N = len(people)
    A = [0] * N

    minV = 999999
    powerset(N, 0)
    print('#{} {}'.format(tc, minV))
