"""
3
1 01:10
2 21:10
2 31:30
"""
T = int(input())
scores = []
for i in range(T):
    str_team, str_time = input().split()
    team = int(str_team)
    min, sec = str_time.split(':')
    time = int(min)*60 + int(sec)
    scores.append([team, time])
scores.insert(0, [0, 0])
scores.append([team, 2880])
one = two = 0
stamp = [0]*2880
for i in range(len(scores)-1):
    if scores[i][0] == 1:
        one += 1
    elif scores[i][0] == 2:
        two += 1
    if one > two:
        for j in range(scores[i][1], scores[i+1][1]):
            stamp[j] = 1
    elif one < two:
        for j in range(scores[i][1], scores[i+1][1]):
            stamp[j] = 2
    else:
        continue

one_cnt = stamp.count(1)
two_cnt = stamp.count(2)
one_min, one_sec = divmod(one_cnt, 60)
two_min, two_sec = divmod(two_cnt, 60)
# if one_sec == 0:
#     one_sec = '00'
# elif two_sec == 0:
#     two_sec = '00'

print("%02d:%02d"%(int(one_min), one_sec))
print("%02d:%02d"%(int(two_min), two_sec))


# print('{}:{}'.format(one_min, one_sec))
# print('{}:{}'.format(two_min, two_sec))
