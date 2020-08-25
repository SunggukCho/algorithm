Str = input()
count = [0 for _ in range(26)]


# 65 ~ 90 대문자
# 97 ~ 122 소문자
for ch in Str:
    if ord(ch) <= 90:               #대문자
        n = ord(ch)-ord('A')
    elif ord(ch)>= 97:              #소문자
        n = ord(ch)-ord('a')
    count[n] += 1

max = 0
maxidx = 0
for i in range(len(count)):         #count 배열에서 최대값 찾기
    if max < count[i]:
        max = count[i]
        maxidx = i
    
cnt_max = 0
for c in count:                     #만약 count내에 max값이 두 개 이상이면 ?출력하려고 함. 따라서 cnt_max가 2이상이면 나가리
    if c == max:
        cnt_max += 1
    
ans = ''
if cnt_max > 1:
    ans = '?'
else:
    ans = chr(maxidx+65)
print(ans)


