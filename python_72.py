fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

count = 0
sum = 0

for line in fhand:
 	if line.startswith('X-DSPAM-Confidence:') :
		line = line.rstrip()
		start = line.find(":")
		string_number = line[start+1:]
		number = string_number.strip()
		number = float(number)
		count = count + 1
		sum = sum + number
average = sum / count
print "Average spam confidence:", average
