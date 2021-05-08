A = int(input())

result = 1 if ((A % 4 == 0 and (A % 100 != 0 or A % 400 == 0))) else 0

print(result)