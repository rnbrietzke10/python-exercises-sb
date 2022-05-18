def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    min_key = None
    max_key = None
    key_size = 0
    max_key_size = 0
    min_key_size = 0
    for key in d.keys():
        if type(key) == str:
            key_size = len(key)
        else:
            key_size = key
        if min_key == None and max_key == None:
                min_key_size = key_size
                max_key_size = key_size
                min_key = key
                max_key = key
        elif key_size > max_key_size:
            max_key_size = key_size
            max_key = key
        elif key_size < min_key_size:
            min_key_size = key_size
            min_key = key
    return (min_key, max_key)