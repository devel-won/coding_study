S = list(map(ord, list(input())))

for i in range(ord('a'), ord('z')+1):
    try:
        print(S.index(i), end=' ')
    except:
        print(-1, end=' ')
