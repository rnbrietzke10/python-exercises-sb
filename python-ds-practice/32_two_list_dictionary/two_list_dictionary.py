def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    my_dictionary = {}
    idx = 0
    for item in keys:
        if len(keys) == len(values):
            my_dictionary[item] = values[idx]
            idx += 1
        elif len(keys) > len(values):
            if len(values) > idx:
                my_dictionary[item] = values[idx]
                idx += 1
            else:
                my_dictionary[item] = None
        elif len(keys) < len(values):
            if len(keys) > idx:
                my_dictionary[item] = values[idx]
                idx += 1
            else:
                break
    return my_dictionary

