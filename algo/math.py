"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
"""
def trailingZeroes(self, A):
    
    count = 0
    
    divide = 5
    while A // divide >= 1:
        count += A // divide
        divide *= 5

    return count

"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
"""
def titleToNumber(self, A):
    
    number = 0
    for x in range(len(A)):
        offset = len(A) - x - 1
        current = ord(A[x]) - ord('A') + 1
        number += (26**offset) * current 
    
    return number

