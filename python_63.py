def count(word, letter):
	antal = 0
	for char in word:
		if letter == char:
			antal = antal + 1
	return antal

word = raw_input('Indtast et ord: ')
letter = raw_input('Indtast et bogstav: ')
antal = count(word, letter)
print antal
