"""Still working on this"""
passed_counter = 0
failed_counter = 0


score_1 = int(input("Enter the integer: "))
score_2 = int(input("Enter the integer: "))
score_3 = int(input("Enter the integer: "))
score_4 = int(input("Enter the integer: "))
score_5 = int(input("Enter the integer: "))
score_6 = int(input("Enter the integer: "))
score_7 = int(input("Enter the integer: "))
score_8 = int(input("Enter the integer: "))
score_9 = int(input("Enter the integer: "))
score_10 = int(input("Enter the integer: "))

if score_1 == 1 or score_2 == 1 or score_3 == 1 or score_4 == 1 or score_5 == 1 or score_6 == 1 or score_7 == 1 or \
		score_8 == 1 or score_9 == 1 or score_10 == 1:
	++passed_counter
else:
	++failed_counter
	
if passed_counter > 8:
	print(passed_counter, ", is the number of student that passed!! Bonus to teacher")
else:
	print(failed_counter, ", is the number of student that failed!! Fuck")
