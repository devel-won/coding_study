import sys

N = int(sys.stdin.readline().strip())

A = [i for i in range(1, N+1)]
count_value = 0


def check(result_list, r):
    for i in range(1, r):
        if (result_list[i] == result_list[0] - i) or (result_list[i] == result_list[0] + i):
            return 0
    return 1


def d(in_list, r):
    global count_value
    for i in range(len(in_list)):
        if r == 1:
            yield [in_list[i]]
        else:
            tmp_list = in_list.copy()
            tmp_list.pop(i)
            for j in d(tmp_list, r-1):
                tmp2_list = [in_list[i]] + j
                if check(tmp2_list, r):
                    yield tmp2_list


result = d(A, N)

for i in result:
    count_value += 1

print(count_value)
