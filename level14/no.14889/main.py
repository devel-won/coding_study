import sys

N = int(sys.stdin.readline())
half_N = N//2
players = [i for i in range(N)]
MAP = []
min_value = N * 100

for i in range(N):
    A = list(map(int, sys.stdin.readline().strip().split()))
    MAP.append(A)


def dfs(input_list, output_list=[], n=0):
    if n == half_N:
        print(input_list, output_list)
    else:
        for i in input_list:
            tmp_out_list = output_list.copy()
            tmp_list = input_list.copy()
            tmp_list.remove(i)
            tmp_out_list.append(i)
            dfs(tmp_list, tmp_out_list, n + 1)



dfs(players)