#MacArthur Project
#Abrar Hussain

print "This is a puzzle favored by Gen. MacArthur. You will be asked to secretly type in your birth month (as an integer) and your age. The computer will make a special calculation, yielding a new integer. The computer will then calculate, using only that special number, your birth month and age."

month = int(raw_input("Give me your birth month:"))
age = int(raw_input("Give me your age:"))

special_number = (month * 2 + 5) * 50 + age - 365
print "Your special number is:", special_number

#115 added as part of MacArthur's trick
special_number_string = str(special_number+115)
calculated_month = special_number_string[0]
calculated_age = special_number_string[1:]

print "The computer calculates then that you are born in the,", calculated_month, "and are", calculated_age, "years old."
