import time

start_time = time.time()

n,m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수 중에 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

finish_time = time.time()
print("소요 시간은", finish_time-start_time)
# 소요시간 8.8