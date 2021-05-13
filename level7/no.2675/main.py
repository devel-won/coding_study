T = int(input())

for i in range(T):
    R, S = input().split()
    print(''.join(list(map(lambda x: x * int(R), list(S)))))
