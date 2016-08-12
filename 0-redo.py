# 1: Apple Stocks
# Runtime: O(n)
# Space: O(1)
# Edge Cases: prices fall all day, less than two prices, negatives ok, 0's ok
def get_max_profit(arr):
    """Returns max profit from stock prices list

        >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        >>> get_max_profit(stock_prices_yesterday)
        6

        >>> get_max_profit([10, 9, 8, 7, 6, 5, 4])
        -1

    """

    if len(arr) < 2:
        raise Exception("Must have more than two prices")

    buy_price = arr[0]
    max_profit = arr[1] - buy_price

    for price in arr[1:]:
        profit = price - buy_price
        max_profit = max(max_profit, profit)
        buy_price = min(buy_price, price)

    return max_profit


# 2: Product all ints except
# Runtime: 
# Space: 
# Edge Cases: 
def 






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"