"""
Instructions:

 - from lab01 import KeyWorsd
 - create two instance of the class (one 'sample1.txt' and other 'sample2.txt'
 - call comparison method between two objects
 - call topN method on each object and print the results
 
"""

from lab01 import KeyWords

keys = KeyWords('sample1.txt')
keys2 = KeyWords('sample2.txt')

keys.remove_common(keys2)

print(keys.topN(10))
print(keys2.topN(10))

