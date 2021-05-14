print(sum(map(lambda x: 8 if x == 'S' else 9 if x == 'V' else 10 if x in 'YZ' else int((ord(x)-ord('A'))/3) + 3, list(input()))))
