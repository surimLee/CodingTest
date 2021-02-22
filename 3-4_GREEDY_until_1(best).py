# N이 100억 이상의 큰 수가 되는 경우 빠르게 동작하려면
# N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식으로 작성 가능

import time
start_time = time.time()

n, k = map(int, input().split())
result = 0

while True:
    # (N == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)

    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)

finish_time = time.time()
print("소요 시간은", finish_time-start_time)

# 100000000 11
# 36
# 소요 시간은 8.429372787475586