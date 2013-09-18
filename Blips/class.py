
#A class which templates a list of integers.

class Numberlist:
    
    def __init__(self, num_list):
        self.num_list = num_list
    
    def sum(self):
        """ (self) -> int
        
        Return the sum of the list.
        
        >>> n1 = Numberlist([1, 2, 5, 1, 4, 3, 3])
        >>> n1.sum()
        19
        """
        
        sum = 0
        
        for x in self.num_list:
            sum += x
        return sum
        
    def mean(self):
        """ (self) -> float
        
        Return the average of the list as a float.
        
        >>> n1 = Numberlist([1, 2, 5, 1, 4, 3, 3])
        >>> n1.mean()
        2.7142857142857144
        
        """
        sum = self.sum()
        return (sum / len(self.num_list))
        
    def min(self):
        """ (self) -> int
        
        Return the minimum number in the list.
        
        >>> n1 = Numberlist([1, 2, 5, 1, 4, 3, 3])
        >>> n1.min()
        1
        """
        
        return min(self.num_list)
        
        
    def max(self):
        """ (self) -> int
        
        Return the maximum number in the list.
        
        >>> n1 = Numberlist([1, 2, 5, 1, 4, 3, 3])
        >>> n1.max()
        5
        """
        return max(self.num_list)
        
    def num_unique(self):
        """ (self) -> int
        
        Return the number of unique elements in the list.
        
        >>> n1 = Numberlist([1, 2, 5, 1, 4, 3, 3,10])
        >>> n1.num_unique()
        6
        """
        
        #set removes duplicates
        unique_set = set(self.num_list)
        return len(unique_set)