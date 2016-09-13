"""
Imagine you landed a new job as a cashier...
Your quirky boss found out that you're a programmer and has a weird request 
about something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make amount of money with coins of the available
denominations.

"""

# # Solution 1: bottom up solution, using memorization
# def num_ways(amt, coins):
#     """Determines the number of ways to make amt with denom's in coins list
#     FIXME: this code doesn't work b/c of a KeyError... but you get the point. 
#     """

#     # instantiate a dict to track ways of making smaller denominations
#     # this variable is outside the scop of recurser, but inside num_ways. 
#     # ways[total] = number of ways to make total
#     ways = {}

#     def recurser(amt_left, dens_left, ways):
#         """Function for recursing"""

#         # check if problem has been solved already:
#         memo_key = str((amt_left, dens_left))
#         if ways[memo_key]:
#             return ways[memo_key]

#         # base cases: 
#         # reach amount perfectly, increment ways
#         if amt_left == 0:
#             return 1

#         # overshoot amount. oops!
#         if amt_left < 0:
#             return 0

#         # no more coins
#         if not coins:
#             return 0

#         current_den, amt_left = dens_left[0], dens_left[1:]

#         # initialize solution counter 
#         num_ways = 0

#         # for each amount divisible by current denomination up to the total 
#         # amount, find ways to make remainder with coin values available. 
#         while amt_left >= 0:
#             num_ways += recurser(amt_left, current_den, ways)
#             amt_left -= current_den

#         # save the solution
#         ways[memo_key] = num_ways

#         return num_ways

#     return recurser(amt, coins, ways)

# # Analysis:
# # Runtime O(n*m) (m is length of coins list, n is amt)
# # Space same as above


# Recursive, top down strategy
def num_ways_recursive(amt, coins):
    """Determines the number of ways to make amt with denom's in coins list

    >>> num_ways_recursive(4, [1, 2, 3])
    4

    """

    # base case: hit correct amount
    if amt == 0: 
        return 1

    # base case: overshot amt
    if amt < 0:
        return 0

    # base case: no more denominations:
    if not coins:
        return 0

    # progress towards base case
    # grab one of the coins from the list to work with, removing it from list
    current_den, coins = coins[0], coins[1:]

    # initialize tracker
    num_ways = 0

    # loop, counting ways, until hi base case
    while amt >= 0:
        num_ways += num_ways_recursive(amt, coins)
        amt -= current_den

    return num_ways

# Analysis


"""
We can start by making a list ways_of_doing_n_cents, where the index is the 
amount and the value at each index is the number of ways of getting that amount.

This list will take O(n)O(n) space, where nn is the size of amount.

To further simplify the problem, we can work with only the first coin in 
denominations, then add in the second coin, then the third, etc.

What would ways_of_doing_n_cents look like for just our first coin: 1 cent? 
Let's call this ways_of_doing_n_cents_1.

  ways_of_doing_n_cents_1 = [
    1,  # 0c:  no coins
    1,  # 1c:  1 1c coin
    1,  # 2c:  2 1c coins
    1,  # 3c:  3 1c coins
    1,  # 4c:  4 1c coins
    1,  # 5c:  5 1c coins
]

Now what if we add a 2c coin?

  ways_of_doing_n_cents_1_2 = [
    1,    # 0c:  no change
    1,    # 1c:  no change
    1+1,  # 2c:  new [(2)]
    1+1,  # 3c:  new [(2,1)]
    1+2,  # 4c:  new [(2,1,1), (2,2)]
    1+2,  # 5c:  new [(2,1,1,1), (2,2,1)]
]

How do we formalize this process of going from ways_of_doing_n_cents_1 
to ways_of_doing_n_cents_1_2?
"""

# Solution 3: bottom up iterative - the good way
def make_change(amt, coins):
    """Determines the number of ways to make amt with denom's in coins list

    >>> make_change(4, [1, 2, 3])
    4

    """

    # initialize a histogram of ways of making chage for amount n
    ways_of_doing_n_cents = [0] * (amt + 1)
    # no coins has one solution
    ways_of_doing_n_cents[0] = 1  
    
    # work through each denomination available
    for coin in coins:
        
        # find ways to make each amount in histogram with current coin
        # no ways below value of coin, only need to go up to max amount 
        for total in range(coin, amt + 1):

            # remainder is the amount we need to make minus the current coin
            remainder = total - coin

            # populate the histogram
            # this line will be hit for each total between coin and amt
            # and it will be hit for each coin in coins
            ways_of_doing_n_cents[total] += ways_of_doing_n_cents[remainder]

            # will look like:
            # ways to make *total* += ways (*total* - *coin*)

            # coin = 1c, progress through *totals*
            # ways to make 1c += ways to make (1-1 = 0) = 0 + 1 = 1
            #   [1, 1, 0, 0, 0]
            # ways to make 2c += ways to make (2-1 = 1) = 0 + 1 = 1
            #   [1, 1, 1, 0, 0]
            # ways to make 3c += ways to make (3-1 = 2) = 0 + 1 = 1
            #   [1, 1, 1, 1, 0]
            # ways to make 4c += ways to make (4-1 = 3) = 0 + 1 = 1
            #   [1, 1, 1, 1, 1]

            # coin = 2c, progress through *totals*
            # ways to make 2c += ways to make (2-2 = 0) = 1 + 1 = 2
            #   [1, 1, 2, 1, 1]
            # ways to make 3c += ways to make (3-2 = 1) = 1 + 1 = 2
            #   [1, 1, 2, 2, 1]
            # ways to make 4c += ways to make (4-2 = 2) = 1 + 2 = 3
            #   [1, 1, 2, 2, 3]

            # coin = 3c, progress through *totals*
            # ways to make 3c += ways to make (3-3 = 0) = 2 + 1 = 3
            #   [1, 1, 2, 3, 3]
            # ways to make 4c += ways to make (4-3 = 1) = 3 + 1 = 4
            #   [1, 1, 2, 3, 4]

    return ways_of_doing_n_cents[amt]



def redo_num_ways(amt, coins):
    """Determines the number of ways to make amt with denom's in coins list

    >>> redo_num_ways(4, [1, 2, 3])
    4

    """
    # ways is the number of ways to make amount at each index
    ways = [0] * (amt + 1)
    ways[0] = 1

    for coin in coins: 

        for value in range(coin, amt+1):

            # Ex: coin = 2, value = 3, ways = [1, 1, 2, 1, 1]
            # Ex: remainder = 3 - 2 = 1
            # Ex: ways[3] = ways[3] + ways[1] = 1 + 1 = 2
            remainder = value - coin
            ways[value] += ways[remainder]

    return ways[amt]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"





