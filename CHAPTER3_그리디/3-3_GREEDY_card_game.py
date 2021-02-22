import time

start_time = time.time()
array=[]
min = 0
n, m = map(int, input().split())
for col in range(n):
    array.append(list(map(int,input().split())))
    array[col].sort()
    if (min < array[col][0]):
        min = array[col][0]
print(min)
finish_time = time.time()
print("소요 시간은", finish_time-start_time)
# 소요시간 8.9 모범답안이랑 비슷비슷

