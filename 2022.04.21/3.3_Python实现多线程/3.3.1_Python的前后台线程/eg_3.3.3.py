# 前台与后台线程
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
    print("test end")


t = threading.Thread(target=test)
t.setDaemon(False)
t.start()
print("The End")
