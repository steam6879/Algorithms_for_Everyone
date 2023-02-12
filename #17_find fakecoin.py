def weigh(a, b, c, d):
    fake = 29

    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1

    return 0

# def find_fakecoin(left, right):   #순차 탐색으로 찾기 ;오래걸림.
#     for i in range(left + 1, right + 1):
#         result = weigh(left, left, i, i)
#
#         if result == -1:
#             return left
#
#         elif result == 1:
#             return i
#
#     return -1

def find_fakecoin(left, right): #절반씩 나눠서 탐색 ;빠른 계산 속도.
    if left == right:
        return left

    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half - 1
    g2_right = g2_left + half - 1

    result = weigh(g1_left, g1_right, g2_left, g2_right)

    if result == -1:
        return find_fakecoin(g1_left, g1_right)

    elif result == 1:
        return find_fakecoin(g2_left, g2_right)

    else:
        return right

n = 100
print(find_fakecoin(0, n - 1))