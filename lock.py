import threading
import random
import time

gMoney = 1000
glo = threading.Lock()
gTotaltime = 10
gTime = 0


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100, 1000)
            glo.acquire()
            if gMoney >= money:
                gMoney -= money
                print("{}消费了{}元，当前剩余{}元".format(threading.current_thread(), money, gMoney))
            else:
                print("{}准备消费{}元，当前剩余{}元，不足，不能消费".format(threading.current_thread(), money, gMoney))
            if gTime >= gTotaltime and money > gMoney:
                glo.release()
                break
            glo.release()
            time.sleep(0.7)


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            Money = random.randint(100, 700)
            glo.acquire()
            if gTime == gTotaltime:
                glo.release()
                break
            gMoney += Money
            print("{}生产了{}元钱，剩余{}元钱".format(threading.current_thread(), Money, gMoney))
            gTime += 1
            glo.release()
            time.sleep(0.5)


def main():
    for x in range(3):
        t1 = Producer(name="生产者")
        t1.start()

    for i in range(5):
        t = Consumer(name="消费者")
        t.start()


if __name__ == '__main__':
    main()
