"""
Write a function to find the rectangular intersection of two given love 
rectangles.

Love rectangles are always "straight" and never "diagonal." 
More rigorously: each side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:

  my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}

Your output rectangle should use this format as well.
"""

# Solution 1: 
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

    # initialize output as empty dict
    overlap = {}

    # calculate overlap's left as right most of two lefts
    overlap['left_x'] = max(rectA['left_x'], rectB['left_x'])

    # calculate width as left most of two right's minus overlaps's left
    overlap['width'] = min(rectA['left_x'] + rectA['width'],
                       rectB['left_x'] + rectB['width']) - overlap['left_x']

    # calculate overlap's bottom as higher of two bottoms
    overlap['bottom_y'] = max(rectA['bottom_y'], rectB['bottom_y'])

    # calculate height as bottom most of two tops minus overlap's bottom
    overlap['height'] = min(rectA['bottom_y'] + rectA['height'],
                        rectB['bottom_y'] + rectB['height']) - overlap['bottom_y']

    # account for no overlaps:
    if overlap['height'] <= 0 or overlap['width'] <= 0:
        return "There is no overlap"

    else:
        return overlap


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"


