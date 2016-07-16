"""
While Queen Elizabeth has a limited number of types of cake, she has an 
unlimited supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British pounds

You brought a duffel bag that can hold limited weight, and you want to make off 
with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples 
and a weight capacity, and returns the maximum monetary value the duffel bag can
hold.

Weights and values may be any non-negative integer. Yes, it's weird to think 
about cakes that weigh nothing or duffel bags that can't hold anything. 
But we're not just super mastermind criminals, we're also meticulous about 
keeping our algorithms flexible and comprehensive.
"""


# Solution 1: works, but won't always be optimal (second doc test tails)
def steal(types, capacity):
    """Takes a list of cake types (kg's, value) and bag capacity, returns maximum

        >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
        >>> capacity    = 20
        >>> steal(cake_tuples, capacity)
        555

        >>> cake_tuples = [(3, 40), (5, 70)]
        >>> capacity    = 9
        >>> steal(cake_tuples, capacity)
        110

    """
    
    # calculate price per kilo (O(n) time and space):
    costs = []
    for kilo, price in types:
        costs.append((float(price/kilo), kilo, price))

    # Sort, to get most cost efficient, by weight: O(nlg(n)) time
    costs.sort()

    # initialize variable 
    capacity_left = capacity
    # initialize variable to track output profit
    max_profit = 0

    while capacity_left >= 0:

        # need cakes to steal cakes
        if not costs:
            return max_profit

        # start with the most expensive cake by weight
        current_cake = costs[-1]

        # keep adding expensive cakes until no longer possible
        while capacity_left >= current_cake[1] and current_cake[1] != 0:
            max_profit += current_cake[2]
            capacity_left -= current_cake[1]

        # if not enough room, go to next cake
        costs.pop()

    return max_profit



# Solution 2: bottom up, storing optimal outputs for each capacity up to cap.
def steal_better(types, capacity):
    """Takes a list of cake types (kg's, value) and bag capacity, returns maximum

        >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
        >>> capacity    = 20
        >>> steal_better(cake_tuples, capacity)
        555

        >>> cake_tuples = [(3, 40), (5, 70)]
        >>> capacity    = 9
        >>> steal_better(cake_tuples, capacity)
        120

    """

    # initialize a histogram of max values for each capacity
    max_values_at_n_capacity = [0] * (capacity + 1)

    # iterate over every stealable weight
    for stolen_weight in range(capacity + 1):

        # initialize max profit for output
        max_profit_at_weight = 0
        
        # iterate over cakes
        for kilo, price in types:

            if kilo <= stolen_weight:

                # for each stealable weight, calculate available weight left
                remaining_weight = stolen_weight - kilo

                # calculate max profit value at n weight capacity
                max_value_for_cake = (price +
                        max_values_at_n_capacity[remaining_weight])

                # pick the bigger value: running max or newly calculated max
                max_profit_at_weight = max(max_value_for_cake,
                                                    max_profit_at_weight)

        max_values_at_n_capacity[stolen_weight] = max_profit_at_weight



    return max_values_at_n_capacity[capacity]








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"







