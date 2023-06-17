"""SOLVED"""

score = int(input("Enter your score: "))

#if score >= 55 and score < 65:
#	print("Your score is", score, "Your grade is D")
#elif score >= 65 and score < 80:
#	print("Your score is", score, "Your grade is C")
#elif score >= 80 and score < 90:
#	print("Your score is", score, "Your grade is B")
#elif score >= 90:
#	print("Your score is", score, "Your grade is A")
#else:
#	print("You failed, you need to retake this course")
	
if 55 >= score < 65:
	print("Your score is", score, "Your grade is D")
elif 65 >= score < 80:
	print("Your score is", score, "Your grade is C")
elif 80 >= score < 90:
	print("Your score is", score, "Your grade is B")
elif 90 >= score <= 100:
	print("Your score is", score, "Your grade is A")
else:
	print("You failed, you need to retake this course")
