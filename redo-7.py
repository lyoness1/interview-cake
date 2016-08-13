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
        
        # for use in calculating mode
        self.histogram = [0] * 111

        assert temps is None or isinstance(temps, list), "temps must be a list"
        if temps:
            for temp in temps:
                assert isinstance(temp, int), "All temperatures must be ints"
                self.histogram[temp] += 1

        # instantiate master temp list
        self.temps = temps

        # for mode
        self.max_occurances = max(self.histogram)
        self.mode = self.histogram.index(max_occurances)

        # initialize helper attributes
        if not temps:
            self.max = None
            self.min = None
            self.len = 0
            self.sum = 0
            self.mean = None
        else:
            self.max = max(temps)
            self.min = min(temps)
            self.len = len(temps)
            self.sum = sum(temps)
            self.mean = float(self.sum) / self.len


    def insert(self, temp):
        assert isinstance(temp, int), "All temps must be ints"

        # add temp to master list
        self.temps.append(temp)

        # update max, min
        self.max = max(self.max, temp)
        self.min = min(self.min, temp)

        # update mean
        self.len += 1
        self.sum += temp
        self.mean = float(self.sum) / self.len

        # update mode
        self.histogram[temp] += 1
        if histogram[temp] > self.max_occurances:
            self.max_occurances = self.histogram[temp]
            self.mode = temp
        

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