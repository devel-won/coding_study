import math

T = int(input())

for _ in range(T):
    H, W, N = list(map(int, input().split()))

    print((N % H if N % H != 0 else H)*100 + math.ceil(N/H))
