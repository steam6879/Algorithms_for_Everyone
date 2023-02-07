# #easy version
# def find_ins_idx(r, v):
#     for i in range(len(r)):
#         if v < r[i]:
#             return i;
#     return len(r)
#
# def ins_sort(a):
#     result = []
#     while a:
#         value = a.pop(0)
#         ins_idx = find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#     return result
#
# d = [2, 4, 5, 1, 3]
# print(ins_sort(d))


#general version
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print("d =", d)
