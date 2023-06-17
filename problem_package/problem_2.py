"""Checks if a teacher deserves bonus based on the number of students that passed in a class of 10
using repetition statement"""
counter = 1
student_passed = 0
student_failed = 0
pass

while counter < 10:
	score = int(input("Enter the score: "))
	if score == 1:
		print("Pass")
		student_passed += 1
	elif score == 2:
		print("Fail")
		student_failed += 1
	counter = counter + 1

if student_passed > 8:
	print(student_passed, "passed!! Bonus to the teacher")
else:
	print(student_failed, "failed!! Teacher Failed")
