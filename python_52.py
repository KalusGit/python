smallest = None
largest = None

while True:
	number = raw_input('Enter a number: ')
	if number == "done":
		break
	else:
		try:
			number = int(number)
		except:
			print 'Invalid input'
			continue
		if smallest is None or number < smallest:
			smallest = number
		if largest is None or number > largest:
			largest = number

print "Maximum is", largest
print "Minimum is", smallest


