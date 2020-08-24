T = input()

word = 0
for i in T:
    if i == ' ':
        word += 1
if T[0] == ' ':
    word -= 1
if T[-1] == ' ':
    word -= 1

print(word+1)