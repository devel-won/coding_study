A = (int(input()) - 1) / 6
count = 0

while A > 0:
    count += 1
    A -= count

print(count + 1)
