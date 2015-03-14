total = 0
count = 0

while True:
	number = raw_input('Enter a number: ')
	if number == "done":
		break
	else:
		try:
			number = float(number)
		except:
			print 'Invalid input'
			continue
		count = count + 1
		total = total + number

average = total/count
print total, count, average


