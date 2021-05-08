A = int(input())

result = "A" if (90 <= A <= 100) \
    else "B" if (80 <= A <= 89) \
    else "C" if (70 <= A <= 79) \
    else "D" if (60 <= A <= 69) \
    else "F"

print(result)