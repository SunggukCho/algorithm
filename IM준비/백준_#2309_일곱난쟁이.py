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

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
total = sum(dwarfs)

break_tool = True
fakes = set()
for i in range(9):
    for j in range(i+1,9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k==i or k==j: continue
                else:
                    print(dwarfs[k])
            break_tool = False
        if break_tool == False:
            break
    if break_tool == False:
        break