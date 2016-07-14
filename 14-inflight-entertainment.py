# two movies only
# different movies
# optomize runtime over memory

def perfect_time(flight_time, lengths):
    """Picks two movies with runtime equal to flight lengths

        >>> perfect_time(120, [45, 60, 70, 40, 60, 110, 80, 130])
        [[60, 60], [40, 80]]

    """

    # make list to store outputs
    possibilities = []
    seen = set()

    # account for multiples (runtime n)
    splits = lengths.count(flight_time/2)
    if splits > 1:
        possibilities.append(
            [flight_time/2, flight_time/2] *
            (splits * (splits-1) / 2)  # splits cho0se 2 combos
        )
        seen.add(flight_time/2)

    # making set improves lookup time
    lengths = set(lengths)

    # find working combos in runtime n
    for length in lengths:
        remainder = flight_time - length
        if remainder in lengths and remainder not in seen:
            possibilities.append([length, remainder])
            seen.add(length)
            seen.add(remainder)


    return possibilities


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
