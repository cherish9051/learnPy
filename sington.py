import time
import threading


class A:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in A.__instance:
            A.__instance[cls] = object.__new__(A)
            return A.__instance[cls]
        else:
            return A.__instance[cls]


class B:
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(B, "_instance"):
            B._instance = B(*args, **kwargs)
        # with B._instance_lock:
        #     if not hasattr(B, "_instance"):
        #         B._instance = B(*args, **kwargs)
        return B._instance


def sington(cls):
    _instance = {}

    def __singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return __singleton


@sington
class C:
    def __init__(self, x=1):
        self.x = x


def task(arg):
    obj = B.instance()
    print(time.time(), obj)


if __name__ == "__main__":
    c1 = C(10)
    c2 = C(2)
    print(c1, c2)
    print(c1.x)
