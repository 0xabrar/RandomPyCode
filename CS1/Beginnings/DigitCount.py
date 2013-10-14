# DigitCount Project
# Abrar Hussain

number = int(input("Input a number: "))
digit = int(input("Enter a digit: "))

# Error check that number is valid and > 0
while (not isinstance(number, int) or number < 0):
    number = int(input("Enter a valid number: "))

# Error check that digit is valid and > 0
while (not isinstance(digit, int) or digit < 0):
    digit = int(input("Enter a valid number: "))


count = 0

# Convert to string and determine occurences of string
for x in str(number):
    if x == str(digit):
        count += 1

print("The digit occurs " + str(count) + " times.")
