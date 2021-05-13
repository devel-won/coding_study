S = list(input().upper())

max_count = 0
result = '?'

for i in set(S):
    x = S.count(i)

    if max_count < x:
        max_count = x
        result = i
    elif max_count == x:
        result = '?'

print(result)
