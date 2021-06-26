import sys

N = int(sys.stdin.readline().strip())

A = [i for i in range(1, N+1)]
B = [[1] * N for i in range(N)]


count_value = 0


def check2(result_list, r):
    for i in range(1, r):
        if (result_list[-1] == result_list[-1 - i] - i) or (result_list[-1] == result_list[-1 - i] + i):
            return 0
    return 1


def check(row, col):
    for i in range(N - col):
        if i == 0:
            B[row][col] = 0
        else:
            if row + i <= N - 1:
                B[row + i][col + i] = 0
            if row - i >= 0:
                B[row - i][col + i] = 0


def d(in_list, r):
    global B

    for i in range(len(in_list)):
        if r == 1:
            check(in_list[i] - 1, r - 1)
            yield [in_list[i]]
        else:
            tmp_list = in_list.copy()
            tmp_list.pop(i)
            for j in d(tmp_list, r-1):
                if B[in_list[i] - 1][r - 1]:
                    tmp2_list = j + [in_list[i]]
                    check(in_list[i] - 1, r - 1)
                    yield tmp2_list
                # tmp2_list = j + [in_list[i]]
                # check(in_list[i] - 1, r - 1)
                # if check2(tmp2_list, r):
                #     yield tmp2_list
                else:
                    B = [[1] * N for i in range(N)]


result = d(A, N)

for i in result:
    count_value += 1
    for j in i:
        print(j, end=' ')
    print()

print(count_value)
