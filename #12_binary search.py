def binary_search(a, x):    #이분탐색 알고리즘
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

d = [1, 6, 9, 23, 28, 34, 58, 71]
print(d)
print(binary_search(d, 28))

