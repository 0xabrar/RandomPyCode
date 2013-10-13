def bin_rep(n: int) -> str:
    """
    Produce the binary string representing non-negative integer n
    in binary.

    >>> bin_rep(0)
    '0'
    >>> bin_rep(1)
    '1'
    >>> bin_rep(5)
    '101'
    """
    return str(n % 2) + bin_rep(n // 2) if (n // 2) != 0 else str(n)


def find_num(SL: 'SearchList', n: int) -> bool:
    """ Return True if n is in SL, False otherwise.

    >>> lister = [5, [2, [1, None, None], [3, None, None]], [6, None, None]]
    >>> find_num(lister, 2)
    True
    >>> find_num(lister, -1)
    False
    >>> find_num(lister, 5)
    True

    """

    if SL is None:
        return False
    if (SL[0] == n):
        return True

    return find_num(SL[1], n) if n < SL[0] else find_num(SL[2], n)


def freeze(X: object) -> object:
    """
    If X is a list, return a new list with equivalent contents, and
    recursively treat the contents of X as you treated X itself...
    If X is not a list, return X itself.

    >>> L1 = [1, [2, 3], 4]
        >>> L2 = freeze(L1)
        >>> L1 is L2
        False
        >>> L1[1] is L2[1]
        False
        >>> L1 == L2
        True
        >>> L1[1] == L2[1]
        True

    """

    if not (isinstance(X, list)):
        return X

    listed = []	
    for x in X:
        listed.append(freeze(x))
    return listed

if __name__ == '__main__':

    import doctest
    doctest.testmod()
