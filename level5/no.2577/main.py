A = int(input())
B = int(input())
C = int(input())

value = list(str(A * B * C))

for i in range(10):
    print(value.count(str(i)))
