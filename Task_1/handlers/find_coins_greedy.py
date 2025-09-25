def find_coins_greedy(coins, target):
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        if target >= coin:
            num = target // coin
            result[coin] = num
            target -= coin * num

    return result if target == 0 else {}
