# #easy version
# def quick_sort(a):
#     n = len(a)
#
#     if n <= 1:
#         return a
#
#     pivot = a[-1]   #기준 설정
#     g1 = []
#     g2 = []
#
#     for i in range(0, n - 1):
#         if a[i] < pivot:
#             g1.append(a[i])
#         else:
#             g2.append(a[i])
#
#     return quick_sort(g1) + [pivot] + quick_sort(g2)
#
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# print(quick_sort(d))

#general version
def quick_sort_sub(a, start, end):   #범위를 지정하여 정렬하는 재귀 호출 함수.
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[end] = a[end], a[i]

    quick_sort_sub(a, start, i-1)   #기준값보다 작은 그룹을 재귀 호출로 다시 정렬.
    quick_sort_sub(a, i + 1, end)   #기준값보다 큰 그룹을 재귀 호출로 다시 정렬.

def quick_sort(a):
     quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print("d =", d)