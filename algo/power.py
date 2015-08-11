import math

def power_of_two(n):
	return n > 0 and (n & (n-1) == 0)

def power_of_two_log(n):
	return n > 0 and math.log(n, 2) % 1 == 0 

