"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am 
local time. The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the 
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock 
yesterday.

No "shorting" - you must buy before you sell. You may not buy and sell in the 
same time step (at least 1 minute must pass).

"""

# Solution 1: Brute force - try every combination, keep track of max
def get_max_profit_1(prices):
    """Returns the maximum profit

    >>> get_max_profit_1([10, 7, 5, 8, 11, 9])
    6

    """

    # keep track of max
    max_profit = 0

    # iterate through list of prices, keep track of index, too
    for idx, buy_price in enumerate(prices):
        # calculate profits for prices after current price
        for sell_price in prices[idx+1:]:
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Analysis: 
# Runtim O(n) to run through buy_prices, and O(n-1) for sell prices. 
# Still O(n^2) for nested loop. 

# Solution 2: Greedy algorithm. Profit will only be greater if buy_price is 
# lower than one already used
def get_max_profit_2(prices):
    """Returns the maximum profit

    >>> get_max_profit_2([10, 7, 5, 8, 11, 9])
    6

    """

    # start with the first price available for purchase
    buy_price = prices[0]

    # find the max profit from the first buy (O(n))
    max_profit = max([prices[i] - buy_price for i in range(1,len(prices))])

    # go through prices and repeat above process, if price < buy_price
    for idx, price in enumerate(prices[1:]):
        if price < buy_price:
            max_profit = max(prices[idx:]) - price
            buy_price = price

    return max_profit

# Analysis:
# Still O(n^2)


# Solution 3: 
def get_max_profit_3(prices):
    """Returns the maximum profit

    >>> get_max_profit_3([10, 7, 5, 8, 11, 9])
    6

    """
    # instantiate variables to track min price, max profit
    min_price = prices[0]
    max_profit = 0

    # iterate over list ONCE
    for price in prices:
        # make sure we're buying at the lowest price we've seen so far
        if price < min_price:
            min_price = price
        # or: min_price = min(min_price, price)
        # calculate potential profit from current price
        profit = price - min_price
        # keep track of profit
        if profit > max_profit:
            max_profit = profit
        # or: max_profit = max(max_profit, profit)

    return max_profit

# Analysis:
# Runtime is O(n) b/c only go through list once!

# What about edge cases?
# 1) Prices don't change
# 2) Prices go down all day
# In Solution #3, profit would correctly return 0. OK. 
# But what if prices go down all day? Return 0? No. Return negative? OK. 

# Solution 4: Edge case of prices falling all day
def get_max_profit_4(prices):
    """Returns the maximum profit

    >>> get_max_profit_4([10, 7, 5, 8, 11, 9])
    6

    >>> get_max_profit_4([10, 9, 8, 7, 6, 5, 4])
    -1

    >>> get_max_profit_4([10])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "1-apple-stocks.py", line 122, in get_max_profit_4
        raise Exception("Can't have profit with only one price!")
    Exception: Can't have profit with only one price!


    """
    # now the list has to be at least two long, or max_profit will error
    if len(prices) < 2:
        raise Exception("Can't have profit with only one price!")

    # instantiate variables to track min price, max profit
    min_price = prices[0]

    # initialize max_profit differently, not to zero. 
    # The algorithm still works now, even for negatives. 
    # It will find the smallest negative. 
    max_profit = prices[1] - prices[0]

    # iterate over list ONCE, starting at second price (already did first one).
    # calculate profit first, then update min_price, incase prices fall all day.
    for price in prices[1:]:
        # calculate potential profit from current price
        profit = price - min_price
        # keep track of profit
        max_profit = max(max_profit, profit)
        # make sure we're buying at the lowest price we've seen so far
        min_price = min(min_price, price)

    return max_profit



if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"




