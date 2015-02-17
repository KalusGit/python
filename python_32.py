try:
  hours = raw_input('Enter Hours: ')
  hours = float(hours)
  rate= raw_input('Enter Rate: ')
  rate = float(rate)
except:
  print 'Error, please enter a number'
  quit()
  
if hours <= 40:
  pay = hours*rate
else:
  extra = hours - 40
  pay = 40*rate + extra*rate*1.5
print pay
