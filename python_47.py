def score2grade(score):
	if 0.0 < score and score <1.0:
		if score >= 0.9: grade = 'A'
		elif score >= 0.8: grade = 'B'
		elif score >= 0.7: grade = 'C'
		elif score >= 0.6: grade = 'D'
		elif score < 0.6: grade = 'F'
	else:
		grade = 'Bad score'
	return grade

try:
	score = raw_input('Enter score: ')
	score = float(score)
	grade = score2grade(score)
	print grade
except:
	print 'Invalid input'
	quit()


