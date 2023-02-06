def search_list(a, x):
    n = len(a)
    for i in range(n):
        if a[i] == x:
            return i + 1

    return -1

v = [17, 3, 34, 35, 75, 25, 63, 49]
print(search_list(v, 34))
print(search_list(v, 3))
print(search_list(v, 43))