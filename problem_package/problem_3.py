"""Checks if a teacher deserves bonus based on the number of students that passed in a class of 10
using selection statement"""
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

if score_1 == 1:
	passed_counter += 1
else:
	failed_counter += 1
	
if score_2 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_3 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_4 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_5 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_6 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_7 == 1:
	passed_counter += 1
else:
	failed_counter += 1
if score_8 == 1:
	passed_counter += 1
else:
	failed_counter += 1

if score_9 == 1:
	passed_counter += 1
else:
	failed_counter += 1
	
if score_10 == 1:
	passed_counter += 1
else:
	failed_counter += 1


if passed_counter > 8:
	print(passed_counter, ", is the number of student that passed!! Bonus to teacher")
else:
	print(failed_counter, ", is the number of student that failed!! Fuck")
	
