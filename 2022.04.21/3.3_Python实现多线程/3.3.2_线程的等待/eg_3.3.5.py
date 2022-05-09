# 在一个子线程启动另外一个子线程
# 并等待子线程结束后才继续执行
import threading
import time
import random


def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))


def test():
    r = threading.Thread(target=reading)
    r.setDaemon(True)
    r.start()
    r.join()
    print("test end")


t = threading.Thread(target=test)
t.setDaemon(False)
t.start()
t.join()
print("The End")
