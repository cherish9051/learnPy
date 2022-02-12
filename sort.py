#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/12        hao.zhang15      1.0         None
"""


# https://www.cnblogs.com/djdjdj123/p/11919760.html


def fastSort(src):
    if len(src) <= 1:
        return src
    # 左>右
    middle = src[len(src) // 2]
    # print(len(src), middle)

    left = [i for i in src if i > middle]
    middle_val = [i for i in src if i == middle]
    right = [i for i in src if i < middle]
    return fastSort(left) + middle_val + fastSort(right)


def popSort(src):
    for i in range(0, len(src)):
        for j in range(i + 1, len(src)):
            if src[i] < src[j]:
                src[i], src[j] = src[j], src[i]
    return src


def cntSort(src):
    tmp = [0] * (max(src) + 1)
    dst = []
    for i in src:
        tmp[i] += 1
    for i in range(len(tmp)-1, -1, -1):
        if tmp[i] >= 1:
            dst.extend([i] * tmp[i])
    return dst


def printSort(func, *args, **kwargs):
    print(func.__name__, func(*args, **kwargs))


if __name__ == "__main__":
    to_be_sort = [1, 6, 34, 55, 0, 2, 2, 4, 6, 7]
    printSort(fastSort, to_be_sort)
    printSort(popSort, to_be_sort)
    printSort(cntSort, to_be_sort)
