try:
  score = raw_input('Enter score: ')
  score = float(score)  
except:
  print 'Invalid input'
  quit()

if 0.0 < score and score <1.0:
  if score >= 0.9: print 'A'
  elif score >= 0.8: print 'B'
  elif score >= 0.7: print 'C'
  elif score >= 0.6: print 'D'
  elif score < 0.6: print 'F'
else:
  print 'Bad score'

