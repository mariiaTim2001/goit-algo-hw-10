def find_min_coins(coins, target):
    coins.sort()
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_used = [-1] * (target + 1)

    for coin in coins:
        for amount in range(coin, target + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                coin_used[amount] = coin

    if dp[target] == float('inf'):
        return {}

    result = {}
    while target > 0:
        coin = coin_used[target]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        target -= coin

    return result