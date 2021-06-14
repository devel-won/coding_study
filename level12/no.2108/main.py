import sys

T = int(sys.stdin.readline())

a = []

for _ in range(T):
    a.append(int(sys.stdin.readline()))

a.sort()

mean = round(sum(a)/T)
mid = a[(T-1)//2]
set_a = list(set(a))
set_a.sort()

dic = dict(zip(set_a, [0 for _ in range(len(set_a))]))

for i in a:
    dic[i] += 1

result = 0
count = 0
max_count = 0

for x, y in dic.items():
    if y > max_count:
        max_count = y
        count = 0
        result = x
    elif y == max_count:
        count += 1
        if count < 2:
            result = x

size = abs(a[-1] - a[0])

print(mean)
print(mid)
print(result)
print(size)
