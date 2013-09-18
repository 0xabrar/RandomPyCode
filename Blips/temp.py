def is_reverse_pair(s1, s2):
    """ (str, str) -> bool
    
    Return True if and only if s1 and s2 are a reverse pair
    
    >>> is_reverse_pair('racecar', 'racecar')
    True
    >>> is_reverse_pair('race', 'word')
    False
    
    """
    
    return (s1[::-1] == s2)

def print_reverse_pairs(wordlist):
    """ (list of str) -> None
    
    Accepts a list of strings and prints out the reverse pairs in the 
    given list, each pair on a line.
    
    >>>print_reverse_pairs(['hole','temp','me'])
    oloh
    pmet
    em
    >>> print_reverse_pairs(['thismustbereversed'])
    desreverebtsumsiht
    
    """

    for word in wordlist:
        print (word[::-1])
        
#testing for the two functions
print (is_reverse_pair('racecar', 'racecar'))
print (is_reverse_pair('race', 'word'))

print_reverse_pairs(['hole','temp','me'])
print_reverse_pairs(['thismustbereversed'])