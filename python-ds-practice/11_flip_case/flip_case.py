from cmath import phase


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ''
    for char in phrase:
        # print(char)
        # print(to_swap.swapcase())
        if char == to_swap.swapcase() or char == to_swap:
            char.swapcase()
            new_phrase = new_phrase + char.swapcase()
        else:
            new_phrase = new_phrase + char
    return new_phrase
    
