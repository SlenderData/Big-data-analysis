# 主线程启动一个子线程并等待子线程结束后才继续执行
import threading
import time
import random


def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))


t = threading.Thread(target=reading)
t.setDaemon(False)
t.start()
t.join()
print("The End")
