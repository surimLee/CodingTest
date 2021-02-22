import time
start_time = time.time()

n, k = map(int, input().split())
count = 0

while(n>1):
    if n%k == 0 :
        n /= k
        count += 1

    else :
        n -= 1
        count += 1

print(count)

finish_time = time.time()
print("소요 시간은", finish_time-start_time)

# 100000000 11
# 36
# 소요 시간은 2.0167369842529297
# 모범답안보다 더 빠름