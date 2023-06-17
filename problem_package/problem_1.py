"""SOLVED"""

number = int(input("Enter your number: "))

#if number < 0:
#	print("The number", number, "is a negative number")
#	
#elif number % 2 == 0:
#	print("The number", number, "is an even number")
#elif number % 2 != 0:
#	print("The number", number, "is an odd number")
	
if number >= 0:
	if number % 2 == 0:
		print("The number", number, "is an even number")
	else:
		print("The number", number, "is an odd number")
else:
	print("The number", number, "is a negative number")
