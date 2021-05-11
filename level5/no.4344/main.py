N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    len_A = A[0]
    mean_value = sum(A[1:])/len_A
    mean_over_A = len(list(filter(lambda x: x > mean_value, A[1:])))
    print(f"{'%0.3f'%round(mean_over_A/len_A*100, 3)}%")
