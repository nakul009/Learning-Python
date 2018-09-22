import queue   # Importing Queue  Package in Python
Q = queue.Queue(maxsize=10)   # Intialize a queue of size 10 #'
Q.put(9)  # put first element in Queue
Q.put(19)  # put 2nd element in queue
Q.put(20)
print(Q.qsize())
for i in range(0, Q.qsize()):
    print(Q.get())
