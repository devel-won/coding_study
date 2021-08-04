import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
# B = 연산자 , + - x / 개수만큼 저장됨
B = list(map(int, sys.stdin.readline().strip().split()))

B_list = []

for index, count in enumerate(B):
    B_list.extend([index] * count)

min_value = -1000000000
max_value = 1000000000

# 주어진 숫자 자리는 바꿀 수 없음
# 순서대로 계산됨
# 최댓값, 최솟값 구하기
# / 연산자 결과는 정수만 사용


def cal(x, y, operator):
    if operator == 0:
        return x + y
    elif operator == 1:
        return x - y
    elif operator == 2:
        return x * y
    else:
        return x//y


# for 문을 통해서 B_list 값들을 하나씩 선택해서 cal 함수에 넣고 하나씩 연산하고 최대값, 최솟값 구하기
def dfs(in_list, value, n):
    if n == N-1:
        return cal(value, A[n], in_list[0])
    else:
        for i in range(len(in_list)):
            tmp_list = in_list.copy()

            for j in dfs(tmp_list[j:], n+1):
                return [in_list[i]] + j

# 숫자 3개
# 연산자 2개
# in_list = 연산자 리스트
# n을 1로 넣고 +1씩 해서 3까지 맞추는 걸로