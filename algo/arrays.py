"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""
def largestNumber(self, A):
    maxlen = len(str(max(A)))
    if all(v == 0 for v in A):
        return '0'
    return ''.join(sorted((str(v) for v in A), reverse=True,
                      key=lambda i: i*(maxlen * 2 // len(i))))

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
"""
def maxSubArray(self, A):

	#negatives extra check
	if all(v < 0 for v in A):
	    return max(A)

	max_a = 0
	max_b = 0	
	# b empties to 0 when sequence is bad (not best)
	for x in A:
	    max_b = max(max_b + x, 0)
	    max_a = max(max_a, max_b)
	return max_a

"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.
"""
def repeatedNumber(self, A):
    
    n = len(A)
    
    sum_actual = sum(x for x in A)
    sum_n = n*(n+1)/2
    
    a_minus_b = sum_actual - sum_n
    
    inter_a = n*(n+1)*(2*n+1)/6
    inter_b = sum(x**2 for x in A)
    
    multi = inter_b - inter_a
    a_plus_b = multi/a_minus_b
    
    a = (a_minus_b + a_plus_b) / 2
    b = a_plus_b - a
    return [a, b]

"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.
"""
def nextPermutation(self, a):
    
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        sorting = sorted(a)
        return sorting
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        
    a[i+1:] = reversed(a[i+1:])  
    return a