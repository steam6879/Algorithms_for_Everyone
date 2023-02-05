# #최대값 구하기
# def find_max(list):
#     n = len(list)
#     max_num = 0
#
#     for i in range(n):
#         if list[i] > list[max_num] :
#             max_num = i
#
#     return max_num
#
# a = [12, 45, 71, 15, 35, 64, 51, 28]
# print(find_max(a))

#동명이인 찾기
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range (0, n - 1):
        for j in range (i + 1, n):
            if a[i] == a[j]:
                result.add(a[j])
    return result

name = ["Tom", "Jerry", "Mike", "Jerry", "Kerry", "Kim", "Kim"]
print(find_same_name(name))
print("exit")