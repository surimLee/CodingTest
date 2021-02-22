import time

# 답안
start_time = time.time()
n = int(input())
a, b, c, d = 0, 0, 0, 0  # 10, 50, 100, 500원의 개수

d = n // 500
c = (n // 100) % 5
b = (n // 50) % 2
a = (n % 100) % 50 // 10

print("500원", d, "개, 100원", c, "개, 50원", b, "개, 10원 ", a,"개")
print("거슬러 줘야 할 동전의 최소 개수 : ", a+b+c+d)

finish_time = time.time()
print("소요시간 : ", finish_time-start_time)

# 모범정답
start_time = time.time()
n = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print ("거슬러 줘야 할 동전의 최소 개수 : ", count)
finish_time = time.time()
print("소요시간 : ", finish_time-start_time)