"""
You decide to test if your oddly-mathematical heating company is fulfilling its 
All-Time Max, Min, Mean and Mode Temperature Guarantee.
Write a class TempTracker with these methods:

insert(), get_max(), get_min(), get_mean(), get_mode()

Optimize for space and time. Favor speeding up the getter functions 
(get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert()
function.

get_mean() should return a float, but the rest of the getter functions can 
return integers. Temperatures will all be inserted as integers. We'll record our
temperatures in Fahrenheit, so we can assume they'll all be in the range 
0..1100..110.

If there is more than one mode, return any of the modes.

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


# Solution 1:
# set max, min, mean, mode as attributes that are recalculated upon each
# insertion. This will speed up getter fn's and slow insert. 
# The other way would be to calculate upon calling a getter fn, which is slower. 
class TempTracker(object):

    def __init__(self, temps=None):
        # assert variables passed in are of correct type
        assert temps is None or isinstance(temps, list), "temps must be a list"
        if temps:
            for temp in temps:
                assert isinstance(temp, int), "All temperatures must be ints"
        # initialize variables
        self.temps = temps
        if temps:
            self.maximum = max(temps)
            self.minimum = min(temps)
            # calculate mean as float
            self.mean = float(sum(temps)) / len(temps)
            # initialize mode to first temperature
            self.mode = temps[0]
            # count the remaining temperatures and reassign mode if greater freq
            for temp in self.temps:
                if self.temps.count(temp) > self.temps.count(self.mode):
                    self.mode = temp
        else:
            self.maximum = None
            self.minimum = None
            self.mean = None
            self.mode = None

    def get_max(self):
        """Returns the maximum recorded temperature"""
        return self.maximum

    def get_min(self):
        """Returns the minimum recorded temperature"""
        return self.minimum

    def get_mean(self):
        """Returns the mean temperature record as a float"""
        return self.mean

    def get_mode(self):
        """Returns any of the most commonly recorded temperature"""
        return self.mode

    def insert(self, temp):
        """Records a new temperature. Updates attributes min, max, mean, mode"""

        # assert correct data type passed into method, then add to list
        assert isinstance(temp, int), "All temperatures must be ints"
        self.temps.append(temp)

        # initialize or update maximum
        if (not self.maximum) or (temp > self.maximum):
            self.maximum = temp

        # initialize or update minimum
        if (not self.minimum) or (temp < self.minimum):
            self.minimum = temp

        # calculate mean as float
        # time could be saved by keeping sum(temps) and len(temps) as attr's
        self.mean = float(sum(self.temps)) / len(self.temps)

        # calculating mode could go from O(n) --> O(1) by using a dict:
        # occurances[temp] = #times temp recorded
        # initialize mode to first temperature
        self.mode = self.temps[0]
        # count the remaining temperatures and reassign mode if greater freq
        for temp in self.temps:
            if self.temps.count(temp) > self.temps.count(self.mode):
                self.mode = temp


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
