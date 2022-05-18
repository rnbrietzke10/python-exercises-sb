def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0
    for x in range(len(matrix)):
        total += matrix[x][x]
    length = len(matrix) - 1
    for x in range(len(matrix)):
        total += matrix[length][x]
        length -= 1
    print(total)

# [33,  1,  2,  3,  4]     Diagonal Top Left to Bottom Right:
# [ 5,  6,  7,  8,  9]         33 + 6 + 2 + 8 + 9
# [33,  1,  2,  3,  4]
# [ 5,  6,  7,  8,  9]     Diagonal Bottom Left to Top Right:
# [ 5,  6,  7,  8,  9]         5 + 6 + 2 + 8 + 4

# Indexes
# 33         6         2         8          9
# [0][0]    [1][1]    [2][2]    [3][3]     [4][4]

# 5         6         2         8          4
# [4][0]    [3][1]    [2][2]    [1][3]     [0][4]

