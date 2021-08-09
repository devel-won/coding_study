import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

B_list = []

for index, count in enumerate(B):
    B_list.extend([index] * count)

min_value = 1000000000
max_value = -1000000000


def cal(x, y, operator):
    if operator == 0:
        return x + y
    elif operator == 1:
        return x - y
    elif operator == 2:
        return x * y
    else:
        return int(x/y)


def dfs(in_list, value, n):
    global max_value
    global min_value

    if n == N-2:
        result = cal(value, A[n+1], in_list[0])
        if result > max_value:
            max_value = result
        if result < min_value:
            min_value = result
    else:
        for i in range(len(in_list)):
            tmp_list = in_list.copy()
            del tmp_list[i]
            dfs(tmp_list, cal(value, A[n+1], in_list[i]), n+1)


dfs(B_list, A[0], 0)

print(max_value)
print(min_value)
