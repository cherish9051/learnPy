#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/12        hao.zhang15      1.0         None
"""

from functools import wraps


def decorate1(func):
    print("func", func)

    def inner(*args, **kwargs):
        print("befor func")
        result = func(*args, **kwargs)
        print("after func")
        return result

    return inner


def decorate2(func=None, default=""):
    print("func2", func, default)

    def decorate(func):
        def inner(*args, **kwargs):
            print("decorate arg:", default)
            print("befor func")
            result = func(*args, **kwargs)
            print("after func")
            return result

        return inner

    if func is None:
        return decorate
    else:
        return decorate(func)


@decorate1
def func1(*args, **kwargs):
    print("i am func1：", args, kwargs)


@decorate2(default="default args")
def func2(*args, **kwargs):
    print("i am func2：", args, kwargs)


# 等同于先执行decorate2()=>decorate, 然后执行@decorate, 同时因为闭包的原因上下文中已经包含default=""这个变量
@decorate2()
def func3(*args, **kwargs):
    print("i am func3：", args, kwargs)


@decorate2
def func4(*args, **kwargs):
    print("i am func4：", args, kwargs)


if __name__ == "__main__":
    print("@@@@@@@")
    func1()
    print("----------")
    func2(1, 2, 3, {"key": "value"})
    print("@@@@@@@")
    func3(1, 2, 3, {"key": "value"})
    print("@@@@@@@")
    func4(1, 2, 3, {"key": "value"})
