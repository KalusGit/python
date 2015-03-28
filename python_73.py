fname = raw_input('Enter the file name: ')
	
try:
	fhand = open(fname)
	count = 0
	for line in fhand:
		if line.startswith('Subject:') :
			count = count + 1
	print 'There were', count, 'subject lines in', fname
except:
	if fname == "na na boo boo":
		print fname.upper(),"- You have been punk'd!"
	else:
		print 'File cannot be opened:', fname
	exit()
