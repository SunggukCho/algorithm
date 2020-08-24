T = input()
T = T.lower()
set_T = set(T)
list_T = list(T)

result = {}

# 중복을 피하기 위해 set 사용. set을 순회하면서 list의 count()메소드로 문자 개수 세기
for i in set_T:
    key = i
    value = list_T.count(i)
    tmp = {key: value}
    result.update(tmp)

#values 의 최댓값 구하기 max()함수 사용.
keys = list(result.keys())
values = list(result.values())
max_value = max(values)

#최대값을 구하고 최대값의 갯수가 2개 이상인지 알아보기
max_val_num = 0
for i in values:
    if i == max_value:
        max_val_num += 1

#만약 최댓값의 갯수가 2개 이상이면 '?'출력
if max_val_num >= 2:
    print('?')
    
#만약 최댓값의 index를 활용해서 key 값을 구하고 그 문자를 대문자로 표현하는 upper()메소드 사용
elif max_val_num == 1:
    idx = values.index(max_value)
    key = keys[idx]
    print(key.upper())