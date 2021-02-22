import time
start_time = time.time()

n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k :
    # N이 K로 나누어 떨어지지 않는다면 N에서 1빼기
    while n % k != 0:
        n -= 1
        result += 1

    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

finish_time = time.time()
print("소요 시간은", finish_time-start_time)

# 100000000 11
# 36
# 소요 시간은 5.0705554485321045