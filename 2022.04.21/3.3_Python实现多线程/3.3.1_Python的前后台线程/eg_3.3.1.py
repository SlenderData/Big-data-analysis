# 在主线程中启动一个子线程执行 reading 函数
import threading
import time
import random


def reading():
    for i in range(10):
        print("reading", i)
        time.sleep(random.randint(1, 2))


r = threading.Thread(target=reading)
r.setDaemon(False)
r.start()
print("The End")
