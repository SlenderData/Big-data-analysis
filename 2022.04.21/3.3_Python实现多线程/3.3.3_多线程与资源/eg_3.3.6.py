# 一个子线程 A 把一个全局的列表 words 进行升序的排列
# 另外一个 D 线程把这个列表进行降序的排列
import threading
import time

lock = threading._RLock()
words = ["a", "b", "d", "b", "p", "m", "e", "f", "b"]


def increase():
    global words
    for count in range(5):
        lock.acquire()
        print("A acquired")
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] < words[i]:
                    t = words[i]
                    words[i] = words[j]
                    words[j] = t
        print("A ", words)
        time.sleep(1)
        lock.release()


def decrease():
    global words
    for count in range(5):
        lock.acquire()
        print("D acquired")
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] > words[i]:
                    t = words[i]
                    words[i] = words[j]
                    words[j] = t
        print("D ", words)
        time.sleep(1)
        lock.release()


A = threading.Thread(target=increase)
A.setDaemon(False)
A.start()
D = threading.Thread(target=decrease)
D.setDaemon(False)
D.start()
print("The End")
