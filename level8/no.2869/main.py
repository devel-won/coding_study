import math

A, B, V = list(map(int, input().split()))

print(math.ceil((V-B)/(A-B)))
