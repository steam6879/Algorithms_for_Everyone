'''
def fact(n):    #팩토리얼 그냥 이용
    f = 1
    for i in range(n):
        f = f * (n - i)

    return f
print(fact(5))
'''

def fact(n):    #재귀함수 이용
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
