from cgi import print_arguments


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_freq = {}
    nums1 = [int(num) for num in str(num1)]
    nums2 = [int(num) for num in str(num2)]
    for num in nums1:
        if num not in num_freq:
            num_freq[num] = nums1.count(num)
    for key in num_freq.keys():
        if nums2.count(key) != num_freq[key]:
            return False
    return True
        
    