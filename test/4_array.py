

def ArrayChallenge(arr):
    min_price = arr[0]
    max_profit = 0


    for price in arr:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


print(ArrayChallenge([44, 30, 24, 32, 35, 30, 40, 38, 15]))
