def fast(src):
    if len(src) <= 1:
        return src
    # 左>右
    middle = src[len(src) // 2]
    print(len(src), middle)

    left = [i for i in src if i > middle]
    middle_val = [i for i in src if i == middle]
    right = [i for i in src if i < middle]
    return fast(left) + middle_val + fast(right)


if __name__ == "__main__":
    to_be_sort = [1, 6, 34, 55, 0, 2, 2, 4, 6, 7]
    # to_be_sort1 = [1, 5, 3,1]
    print(fast(to_be_sort))
