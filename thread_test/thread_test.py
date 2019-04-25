#!/usr/bin/python3
# -*- coding:utf-8 -*-

import queue
import threading
import time

exitFlag = 0
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["one", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("关闭线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        # print("process_data lock acquire {name}".format(name=thread_name))
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            print("process_data lock acquire {name} release".format(name=thread_name))
            queueLock.release()
        time.sleep(1)


if __name__ == '__main__':
    print("workQueue.empty:", workQueue.empty())

    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    queueLock.acquire()
    # for word in nameList:
    #     workQueue.put(word)
    queueLock.release()

    while not workQueue.empty():
        pass

    # exitFlag = 1

    for t in threads:
        t.join()

    print("退出线程")
    # threading.Thread.start(process_data)
    # threading.Thread.start()
