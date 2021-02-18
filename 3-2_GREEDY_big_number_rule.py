import time

# <input>
# 5 8 3
# 2 4 5 4 5
# <output>
# 46

# N, M, K = 5, 8, 3
# list = [2, 4, 5, 4, 6]

# N = 배열의 크기
# M = 숫자를 더해야 하는 횟수
# K = 연속해서 더할 수 있는 횟수


# 답안
start_time = time.time()
result = 0
count = 0
N, M, K = map(int, input().split())
data = map(int, input().split())

# 큰수 법칙에 따른 답 도출
sorted_list = sorted(data, reverse = True)

for _ in range(M) :
    if count == K :
        result += sorted_list[1]
        count = 0
    else :
        result += sorted_list[0]
        count += 1

print(result)
finish_time = time.time()
print("소요시간 : ", finish_time-start_time)


# 모법 답안(평범)
start_time = time.time()
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

while True :
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
finish_time = time.time()
print("소요시간 : ", finish_time-start_time)


# 모범 답안(수학적 접근)
start_time = time.time()
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m//(k+1)+(m%(k+1)))
result = first*count + second*(m-count)
print(result)
finish_time = time.time()
print("소요시간 : ", finish_time-start_time)
