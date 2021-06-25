import sys

N = int(sys.stdin.readline().strip())

A = [i for i in range(1, N+1)]
B = []
count_value = 0


# N = 5
# r = 3
# tmp = 2

# 아이디어
# check를 통해서 index가 낮은 list들 중 대각선 체크
# row에 퀸이 하나만 들어가기 때문에 1차원 행렬 사용
# column의 경우 1 ~ N까지 숫자가 하나씩 들어가기 때문에 선택하는 문제로 축소
# 섞어서 문제 해결

def check(result_list, r):
    tmp = N - r
    for i in range(1, N - r):
        if (result_list[tmp-i] == result_list[tmp] - i) or (result_list[tmp-i] == result_list[tmp] + i):
            return 1
    return 0


def d(in_list, r):
    global count_value
    for i in range(len(in_list)):
        if r == 1:
            yield [in_list[i]]
        else:
            tmp_list = in_list.copy()
            tmp_list.pop(i)
            for j in d(tmp_list, r-1):
                yield [in_list[i]] + j

result = d(A, N)

for i in result:
    for x, y in enumerate(i):
        print("test")
    print()

# 1~N까지 경우의 수 모두 구한다음 check를 통해서 n-queen 문제에서 대각선에 해당하는지 확인


print("check")

# def d(in_list, result_list, r):
#     global count_value
#
#     for i in range(len(in_list)):
#         if r == 1:
#             count_value += 1
#             yield [in_list[i]]
#         else:
#             tmp_list = in_list.copy()
#             result_list += [tmp_list.pop(i)]
#             for j in d(tmp_list, result_list, r-1):
#                 yield [in_list[i]] + j
#
#
# 1 0 0 0
# 0 0 1 0
# 0 0 0 0
# 0 1 0 0
#
# 0 1 2
# 0 3 1
#
# index
#
# [0, 0, 0, 0]
#
# [2, 4, 1, 3]