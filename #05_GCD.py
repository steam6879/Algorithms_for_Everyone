# def gcd(a, b):    //정석
#     i = min(a, b)
#     while True:
#         if a % i == 0 and b % i == 0:
#             return i
#         i = i - 1

def gcd(a, b):  #유클리드 방식.
    print(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(3, 4))
print(gcd(60, 35))
