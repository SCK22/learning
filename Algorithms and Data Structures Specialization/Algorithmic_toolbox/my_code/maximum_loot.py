# python3

from sys import stdin

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    max_loot = 0
    for price in prices:
        max_price_ind = prices.index(max(prices))
        if capacity >= weights[max_price_ind]:
            capacity = capacity - weights[max_price_ind]
            max_loot = max_loot + (weights[max_price_ind] * prices[max_price_ind])
            prices.remove(prices[max_price_ind])
            weights.remove(weights[max_price_ind])
        else:
            max_loot = max_loot + (capacity * prices[max_price_ind])
            prices.remove(prices[max_price_ind])
            weights.remove(weights[max_price_ind])
            capacity = 0
    return max_loot


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
