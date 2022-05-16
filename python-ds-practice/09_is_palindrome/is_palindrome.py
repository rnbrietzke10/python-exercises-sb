def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco ca t')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_list = list(phrase.lower())
    while phrase_list.count(' ') != 0:
        idx = phrase_list.index(' ')
        phrase_list.remove(" ")
    remove_spaces_phrase = ''.join(phrase_list)
    phrase_list.reverse()
    reversed_phrase =  ''.join(phrase_list)
    
    if reversed_phrase == remove_spaces_phrase:
        return True
    else:
        return False