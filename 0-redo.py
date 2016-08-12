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
# Runtime: O(2n) --> O(n)
# Space: O(n) for output list
# Edge Cases: zeros, two zeros, length 1
def get_products(arr):
    """Returns an array of products of all integers except at index

        >>> get_products([1, 7, 3, 4])
        [84, 12, 28, 21]

        >>> get_products([0, 1, 2, 3])
        [6, 0, 0, 0]

        >>> get_products([0, 0, 1])
        [0, 0, 0]

        >>> get_products([])
        [None]

    """

    # edge case: no numbers
    if not arr:
        return [None]

    # initialize output
    output = [1] * len(arr)

    # initialie product before
    product_before = 1

    # go forward, incrementing product
    for idx in range(len(arr)):
        output[idx] *= product_before
        product_before *= arr[idx]

    # initialize product after
    product_after = 1

    # for backward, incrementing product
    for idx in range(len(arr)-1, -1, -1):
        output[idx] *= product_after
        product_after *= arr[idx]

    return output













if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"