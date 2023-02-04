
def find_max(list):

    n = len(list)
    max = 0
    for i in range(n):
        if list[i] > max :
            max = list[i]

    return max

a = [112, 45, 71, 15, 35, 64, 51, 28]
print(find_max(a))
