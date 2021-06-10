N = int(input())

all_list = []

for i in range(N * 1000):
    s = str(i)
    if s.count("666") > 0:
        all_list.append(s)

print(all_list[N-1])
