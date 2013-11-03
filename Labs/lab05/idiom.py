def dot_prod(v: list, u: list) -> float:
    """return the dot product v.u
    precondition: v and u must have the same number of elements and length
    greater than 0

    >>> dot_prod([1, 2], [3, 4])
    11
    """
    return sum([x * y for x, y in zip(v, u) if v.index(x) == u.index(y)])


def matrix_vector_prod(M: list, v: list) -> list:
    """return Mv --- product of M with v
    precondition: vectors in M must be of same length as v both M and v are
    non-empty

    >>> matrix_vector_prod([[1, 2], [3, 4]], [2, 3])
    [8, 18]
    """
    return [dot_prod(x, v) for x in M]


def squares_build_list(n: int) -> list:
    """list the squares of first n natural numbers

    >>> squares_build_list(6)
    [0, 1, 4, 9, 16, 25]
    """
    squares = []
    for x in range(n):
        squares.append(x ** 2)
    return squares


def squares_use_comp(n: int) -> list:
    """list squares of first n natural numbers

    >>> squares_use_comp(6)
    [0, 1, 4, 9, 16, 25]
    """
    return [x ** 2 for x in range(n)]


def squares_use_gen(n: int) -> list:
    """sequence of squares of first n natural numbers

    >>> list(squares_use_gen(6))
    [0, 1, 4, 9, 16, 25]
    """
    return (x ** 2 for x in range(n))


def pythagorean_triples(n: int) -> list:
    """List triples (x, y, z) with x^2 + y^2 = z^2
    and x < y < z < n are natural numbers

    >>> pythagorean_triples(6)
    [(3, 4, 5)]
    """
    return [(i, j, k) for i in range(n) for j in range(n) for k in range(n)
            if (i ** 2 + j ** 2 == k ** 2) and i < j < k]


if __name__ == '__main__':
    import doctest
    from time import time
    doctest.testmod()

    n = 1000000
    start = time()
    squares_build_list(n)
    print("squares_build_list({}) takes {} seconds"
          .format(n, time() - start))

    start = time()
    squares_use_comp(n)
    print("squares_use_comp({}) takes {} seconds"
          .format(n, time() - start))

    start = time()
    squares_use_gen(n)
    print("squares_use_gen({}) takes {} seconds"
          .format(n, time() - start))
