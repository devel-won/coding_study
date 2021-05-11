N = int(input())

B = list(map(int, input().split()))
max_B = max(B)

print(sum(list(map(lambda x: x/max_B * 100, B)))/N)
