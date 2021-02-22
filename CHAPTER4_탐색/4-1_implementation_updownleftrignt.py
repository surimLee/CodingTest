import time
start_time = time.time()

n = int(input())
x = 1
y = 1
direction = list(input().split())

for i in range(len(direction)) :
    if (direction[i]=='R'):
        if (y < n):
            y += 1
    elif (direction[i]=='L'):
        if (y > 1):
            y -= 1
    elif (direction[i] == 'U'):
        if (x > 1) :
            x -= 1
    elif (direction[i] == 'D'):
        if (x < n):
            x += 1
print (x, y)

finish_time = time.time()
print("소요 시간은", finish_time-start_time)

# 5
# R R R U D D
# 3 4
# 소요 시간은 14.15898060798645