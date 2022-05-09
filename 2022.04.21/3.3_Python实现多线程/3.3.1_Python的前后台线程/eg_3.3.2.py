# 启动一个前台线程
import threading
import time
import random


def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))


r = threading.Thread(target=reading)
r.setDaemon(True)
r.start()
print("The End")
