#Einstein Project
#Abrar Hussain

print "This is a puzzle fvored by Einstein. You will be asked to enter a three diit number, where the hundred's digit differs from the one's digit by at least two. The procedure will always yield 1089."

number = raw_input("Give me a number:")
reverse_number = int(number[::-1])

difference = abs(int(number) - reverse_number)

differenceString = str(difference)
reverse_difference = int(differenceString[::-1])

sum_differences = difference + reverse_difference

#all relevant information outputted to the user
print "For the number:", number,"the reserve number is:", reverse_number
print "The difference between", number, "and", reverse_number, "is", difference
print "The reverse difference is:", reverse_difference
print "The sum of the difference and the reversed difference is:", sum_differences
