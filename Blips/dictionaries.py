def print_record(record):
    """ (dict: int -> str) -> None
    
    Takes a dictionary as an input. Keys are student numbers, values are names.
    The function will print out all records, nicely formatted.
    
    >>> record = {1234: 'Tony Stark', 1138: 'Steve Rogers'}
    >>> print_record(record)
    Tony Stark (#1234)
    Steve Rogers (#1138)
    
    """
    for x in record:
        print ("{0} (#{1})".format(record.get(x), x))
        
        
def count_occurrences(strings):
    """ ([str]) -> dict
    
    Takes a list of strings as input, and returns a dictionary with
    key/value pairs of each word and the number of occurrences of that word.
    
    >>> count_occurrences(['a', 'b', 'a', 'a', 'c', 'c'])
    {'a': 3, 'b': 1, 'c': 2}
    """
    
    frequency = {}
    
    for x in strings:
        if (x in frequency):
            frequency[x] += 1
        else:
            frequency[x] = 1
            
    return frequency
    
#testing the defined functions
record = {1234: 'Tony Stark', 1138: 'Steve Rogers'}
print_record(record)

print(count_occurrences(['a', 'b', 'a', 'a', 'c', 'c']))