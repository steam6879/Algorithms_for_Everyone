# def max_profit(prices): #low calculation speed
#     n = len(prices)
#     max_profit = 0
#
#     for i in range(0, n - 1):
#         for j in range(i + 1, n):
#             profit = prices[j] - prices[i]
#
#             if profit > max_profit:
#                 max_profit = profit
#
#     return max_profit

def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_price= prices[0]

    for i in range(1, n):
        profit = prices[i] - min_price

        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
