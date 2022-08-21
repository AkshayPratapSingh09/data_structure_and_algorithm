import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
import time
start_time = time.time()

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

recur_sum(10)
seconds = time.time() - start_time
print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
