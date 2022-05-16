def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_counts = {}
    for char in phrase:
        if letter_counts.get(char) == None:
            letter_counts[char] = 1
        else:
            letter_counts[char] = letter_counts.get(char) + 1
    return letter_counts
    