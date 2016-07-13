"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.

"""

# Solution 1: Brute force
def get_products_1(arr):
    """Returns new list with products of all other integers

    >>> get_products_1([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    # instantiate an output list
    output = [1] * len(arr)

    # loop over indecies
    for idx in range(len(arr)):

        # multiply by all ints before idx
        for i in arr[:idx]:
            output[idx] *= i

        # mulitply by all ints after idx
        for i in arr[idx+1:]:
            output[idx] *= i

    return output

# Analysis: Yuck. O(n^2)


# Solution 2: Keep track of multiplications already done (memorization)
def get_products_2(arr):
    """Returns new list with products of all other integers

    >>> get_products_2([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    products_before_idx = [1] * len(arr)
    products_after_idx = [1] * len(arr)

    # start at 1 and move forward through list
    product = 1
    for idx in range(len(arr)):
        products_before_idx[idx] = product
        product *= arr[idx]

    # start over for going backward
    product = 1
    for idx in range(len(arr)-1,-1,-1):
        products_after_idx[idx] *= product
        product *= arr[idx]

    # mulitply before and after to get output
    output = []

    for idx in range(len(arr)):
        output.append(products_before_idx[idx] * products_after_idx[idx])

    return output

# Analysis: O(n) products before, O(n) products after, O(n) output: O(n) runtime
# Space takes three lists the same size as the input


# Solution 3: Get rid of one of the lists (the after one - combine with output)
def get_products_3(arr):
    """Returns new list with products of all other integers

    >>> get_products_3([1, 7, 3, 4])
    [84, 12, 28, 21]

    """
    # make a list to store products and be the eventual output
    products = []

    # start at product = 1 for zero'th index, because no previous ints
    product = 1
    # loop over the indecies of the list
    for idx in range(len(arr)):
        # append the running product to the output list, starting at 1
        products.append(product)
        # increment the product to include the value at the current int
        product *= arr[idx]

    # re-initialize the product at 1 to find products of ints AFTER idx
    product = 1
    # loop backwards over indecies to calculate prodcuts of ints after
    for idx in range(len(arr)-1,-1,-1):
        # first, multiply current value (all products before idx) by current 
        # product of all the ints afterward
        products[idx] *= product
        # then, increment product to include the value at current idx
        product *= arr[idx]

    return products

# Analysis: O(2n) runtime -> O(n)
# Space: only created one new list, O(n) space!


# Solution 4: Edge cases
# 1) Only one number? This won't. Work. Can raise an exception. 
# 2) Any zeros? Well, the only numer that wouldn't be zero would be that index.
# It will still work fine with zeros.  
def get_products_4(arr):
    """Returns new list with products of all other integers

    >>> get_products_4([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_4([1, 0, 3])
    [0, 3, 0]

    """
    # Edge case of list containing only one int
    if len(arr) < 2:
        raise Exception("Can't multiply without other numers!")

    # make a list to store products and be the eventual output
    products = []

    # start at product = 1 for zero'th index, because no previous ints
    product = 1
    # loop over the indecies of the list
    for idx in range(len(arr)):
        # append the running product to the output list, starting at 1
        products.append(product)
        # increment the product to include the value at the current int
        product *= arr[idx]

    # re-initialize the product at 1 to find products of ints AFTER idx
    product = 1
    # loop backwards over indecies to calculate prodcuts of ints after
    for idx in range(len(arr)-1,-1,-1):
        # first, multiply current value (all products before idx) by current 
        # product of all the ints afterward
        products[idx] *= product
        # then, increment product to include the value at current idx
        product *= arr[idx]

    return products



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"