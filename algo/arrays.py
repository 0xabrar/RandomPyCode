def largestNumber(self, A):
    maxlen = len(str(max(A)))
    if all(v == 0 for v in A):
        return '0'
    return ''.join(sorted((str(v) for v in A), reverse=True,
                      key=lambda i: i*(maxlen * 2 // len(i))))
    
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