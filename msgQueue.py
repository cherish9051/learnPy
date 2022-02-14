from multiprocessing import Queue, Process, JoinableQueue
import time
import random
import queue


def consumer(name, q:Queue):
    while True:
        msg = q.get()
        if msg is None: break
        time.sleep(random.randint(1,2))
        print("{0}消费了msg：{1}".format(name, msg))

def producer(name, q:Queue):
    for i in range(10):
        print("{0}生产了msg：{1}".format(name, str(i)))
        q.put(str(i))

def consumer1(name, q:JoinableQueue):
    while True:
        msg = q.get()
        # if msg is None: break
        time.sleep(random.randint(1,2))
        print("{0}消费了msg：{1}".format(name, msg))
        q.task_done()


def producer1(name, q:JoinableQueue):
    for i in range(10):
        print("{0}生产了msg：{1}".format(name, name + str(i)))
        q.put(name +str(i))
    q.join()

if __name__ == '__main__':
    q = JoinableQueue(30)
    p1 = Process(target=producer1, args=("kevin", q) )
    p2 = Process(target=producer1, args=("zhang", q) )
    c1 = Process(target=consumer1, args=("lily", q) )
    c2 = Process(target=consumer1, args=("lucy", q) )
    c3 = Process(target=consumer1, args=("lucy2", q) )
    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()
