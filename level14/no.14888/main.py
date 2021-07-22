import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
# B = 연산자 , + - x / 개수만큼 저장됨
B = list(map(int, sys.stdin.readline().strip().split()))

# 주어진 숫자 자리는 바꿀 수 없음
# 순서대로 계산됨
# 최댓값, 최솟값 구하기
# / 연산자 결과는 정수만 사용
