import math
import time

def do_something():
    count = 0
    while count < 10:
       time.sleep(1)
       count = count + 1

# 시작시간
start = time.time()

do_something()

# 종료시간
end = time.time()

print(end - start)
