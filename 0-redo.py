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


# 3: Highest Product of Three
# Runtime: O(n)
# Space: O(1)
# Edge Cases: zeros, negatives, not sorted
def get_highest_product_of_3(arr):
    """Returns the highest product of three integers from arr

        >>> get_highest_product_of_3([1, 2, 3, 4, 5])
        60

        >>> get_highest_product_of_3([-10, -10, 0, 1, 2, 3])
        300

        >>> get_highest_product_of_3([-3, -3, -1, -5, -2])
        -6

    """

    if len(arr) < 3:
        raise Exception("Must have at least three integers")

    max_product_3 = arr[0] * arr[1] * arr[2]
    max_product_2 = arr[0] * arr[1]
    highest = arr[0]
    lowest = arr[0]
    min_product_2 = arr[0] * arr[1]

    for num in arr[2:]:
        # max product of 3 is updated first, against new num
        max_product_3 = max(max_product_3,
                            min_product_2 * num,
                            max_product_2 * num)

        # update remaining variables
        max_product_2 = max(max_product_2, highest * num, lowest * num)
        min_product_2 = min(min_product_2, lowest * num, highest * num)
        highest = max(highest, num)
        lowest = min(lowest, num)
        

    return max_product_3


# 4: Hi Cal
# Runtime: O(nlg(n)) so sort
# Space: O(n) for output list
# Edge Cases: not sorted, just touching, engulfed second times, etc.
def condense_meeting_times(arr):
    """Returns a lsit of tuples when everyone is avilable

        >>> condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        [(0, 1), (3, 8), (9, 12)]

        >>> condense_meeting_times([(1, 2), (2, 3)])
        [(1, 3)]

        >>> condense_meeting_times([(1, 5), (2, 3)])
        [(1, 5)]

        >>> condense_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)])
        [(1, 10)]

    """

    # O(nlg(n)) to sort by start times
    arr.sort()

    output = []

    first_start, first_stop = arr[0]

    for curr_start, curr_stop in arr[1:]:

        # no overlap: update output, reassign first start/stop
        if curr_start > first_stop:
            output.append((first_start, first_stop))
            first_start, first_stop = curr_start, curr_stop

        # overlap: 
        else: 
            first_stop = max(first_stop, curr_stop)

    # still have to add last condensed time
    output.append((first_start, first_stop))

    return output


# 5: Number of Ways to Make Change
# Runtime: O(n*m) where n is amt and m is length of coins list
# Space: O(n) for memo
# Edge cases: 
def num_ways(amt, coins):
    """Returns the number of ways to make amt from denominations in coins list

        >>> num_ways(4, [1, 2, 3])
        4

    """

    # initialize histogram of ways to make *idx* amt for use of memoization
    memo = [0] * (amt+1)
    # making no change has one solution: no coins
    memo[0] = 1

    # use each denomination
    for coin in coins: 
        
        # update each value in memo from current coins value through amt
        for value in range(coin, amt+1):
            
            # use the current coin, update value's count with ways to make rmdr
            remainder = value - coin
            memo[value] += memo[remainder]

    return memo[amt]


# 6: Rectangular Love
# Runtime: O(1) - just four calculations
# Space: O(1) - even though we make a new dict output?
# Edge cases: share edge, no overlap, complete contained
def find_intersection(rectA, rectB):
    """Returns the intersection of two rectangles

    >>> rectA = {
    ...     'left_x': 1,
    ...     'bottom_y': 1,
    ...     'width': 4,
    ...     'height': 3
    ...     }
    >>> rectB = {
    ...     'left_x': 3,
    ...     'bottom_y': 3,
    ...     'width': 4,
    ...     'height': 4
    ...     }

    >>> find_intersection(rectA, rectB)
    {'width': 2, 'left_x': 3, 'bottom_y': 3, 'height': 1}

    """

    # find left of intersection
    left_x = max(rectA['left_x'], rectB['left_x'])

    # find bottom of interserction
    bottom_y = max(rectA['bottom_y'], rectB['bottom_y'])

    # find width of intersection as min of two right sides
    right_side = min(rectA['left_x'] + rectA['width'],
                     rectB['left_x'] + rectB['width'])
    width = right_side - left_x

    # find height of intersection as min of two tops
    top = min(rectA['bottom_y'] + rectA['height'],
              rectB['bottom_y'] + rectB['height'])
    height = top - bottom_y

    # account for no overlap
    if height <= 0 or width <= 0:
        return "There is no overlap"

    intersection = {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

    return intersection


# 7: Temp Tracker
"""
    >>> Temps = TempTracker([60, 80, 70])
    >>> Temps.insert(70)
    >>> Temps.get_max()
    80
    >>> Temps.get_min()
    60
    >>> Temps.get_mean()
    70.0
    >>> Temps.get_mode()
    70

"""

class TempTracker:
    def __init__(self, temps=None):
        assert temps is None or isinstance(temps, list), "temps must be a list"
        self.histogram = [0] * 111
        if temps:
            for temp in temps:
                assert isinstance(temp, int), "All temperatures must be ints"
                self.histogram[temp] += 1
        self.temps = temps
        if temps:
            self.max = max(temps)
            self.min = min(temps)
            self.len = len(temps)
            self.sum = sum(temps)
        else:
            self.max = None
            self.min = None
            self.len = 0
            self.sum = 0
        if self.sum != 0:
            self.mean = float(self.sum) / self.len
        else: 
            self.mean = None
        self.mode = self.histogram.index(max(self.histogram))


    def insert(self, temp):
        assert isinstance(temp, int), "All temps must be ints"
        self.temps.append(temp)
        self.max = max(self.max, temp)
        self.min = min(self.min, temp)
        self.len += 1
        self.sum += temp
        self.mean = float(self.sum) / self.len
        self.histogram[temp] += 1
        self.mode = self.histogram.index(max(self.histogram))

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"