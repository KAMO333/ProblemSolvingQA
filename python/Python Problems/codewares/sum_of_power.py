def powers(n):
    """Return a list of powers of two that sum to *n*.

    The problem reduces to decomposing *n* into its binary
    representation.  For each bit set in *n* we include the
    corresponding power of two.  This handles *n* itself being a
    power of two (the list will contain only *n*) and works for any
    positive integer.
    """

    if n <= 0:
        # the original tests never exercise this, but an empty list is
        # reasonable for non-positive input
        return []

    result = []
    power = 1

    # iterate through powers of two until we exceed n
    while power <= n:
        if n & power:
            result.append(power)
        power <<= 1

    return result


print(powers(1), [1])
print(powers(5), [1, 4])
print(powers(7), [1, 2, 4])
print(powers(8), [8])
print(powers(10), [2, 8])
