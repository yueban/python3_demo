# coding=utf-8

# # _thread module is deprecated
# import time
# import _thread


# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print('%s: %s' % (threadName, time.ctime(time.time())))


# try:
#     _thread.start_new_thread(print_time, ('Thread-1', 2))
#     _thread.start_new_thread(print_time, ('Thread-2', 4))
# except:
#     print('Error: thread start failed')

# while 1:
#     pass


# import threading
# import time

# threadLock = threading.Lock()


# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay

#     def run(self):
#         threadLock.acquire()
#         print('%s started' % self.name)
#         print_time(self.name, self.delay, 3)
#         print('%s stoped' % self.name)
#         threadLock.release()


# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print('%s: %s' % (threadName, time.ctime(time.time())))
#         counter -= 1


# thread1 = MyThread(1, 'Thread-1', 1)
# thread2 = MyThread(2, 'Thread-2', 2)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# print('main thread exit')


# multi-thread process queue tasks
import queue
import threading
import time

threadLock = threading.Lock()
exitFlag = 0


class Worker(threading.Thread):
    def __init__(self, id, name, taskQueue):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.taskQueue = taskQueue

    def run(self):
        print('worker started: %s' % self.name)
        processTask(self.name, self.taskQueue)
        print('worker stoped: %s' % self.name)


def processTask(workerName, taskQueue):
    while not exitFlag:
        threadLock.acquire()
        if not taskQueue.empty():
            task = taskQueue.get()
            print('%s processing %s' % (workerName, task))
            threadLock.release()
        else:
            threadLock.release()
        # worker have a rest to let other workers get the threadLock
        time.sleep(1)


# declare variable
tasks = queue.Queue(10)
workers = []

# create & start workers
for i in range(1, 4):
    worker = Worker(i, 'worker-%s' % i, tasks)
    worker.start()
    workers.append(worker)

# add tasks
threadLock.acquire()
for i in range(1, 11):
    tasks.put('task-%s' % i)
threadLock.release()

# wait all tasks processed
while not tasks.empty():
    pass

# notify workers to stop work
exitFlag = 1

# wait all workers stop work
for worker in workers:
    worker.join()

print("main thread exit")
