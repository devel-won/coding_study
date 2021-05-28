x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

print(sum(set(x_list))*2 - sum(x_list), sum(set(y_list))*2 - sum(y_list))
