def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    for item in lst:
        # print(item)
        print(bool(item), item)
        # if bool(item) == False:
        #     lst.remove(item)

    return lst 