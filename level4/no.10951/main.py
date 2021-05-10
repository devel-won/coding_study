import sys

while True:
    try:
        A, B = list(map(int, sys.stdin.readline().split()))
        print(A + B)
    except:
        break
