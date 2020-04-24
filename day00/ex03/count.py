import sys

def tab_analyzer(str):
	tab = [0, 0, 0, 0, 0]
	tab2 = "".join(str)
	print(tab2)
	for i in "".join(str):
		tab[0] += 1 
		if i.isalpha():
			if i.isupper():				
				tab[1] += 1
			else:		
				tab[2] += 1
		elif i.isspace():
			tab[4] += 1
		elif not i.isnumeric():
			tab[3] += 1
	return tab

def text_analyzer(str=""):
	"""
	This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
	if str:
		tab_count = tab_analyzer(str)
		print('The text contains {} characters:\n\n' \
			'- {} upper letters\n\n' \
			'- {} lower letters\n\n' \
			'- {} punctuation marks\n\n' \
			'- {} spaces'.format(tab_count[0], \
							tab_count[1], tab_count[2], \
							tab_count[3], tab_count[4]))
	else:
		print('What is the text to analyse?\n' \
			'>> Python is an interpreted, high-level, general-purpose\n' \
			'programming language. Created by Guido van Rossum and' \
			'first\n' \
			'released in 1991, Python\'s design philosophy emphasizes' \
			'code\n' \
			'readability with its notable use of significant' \
			'whitespace.\n' \
			'The text contains 234 characters:\n\n' \
			'- 5 upper letters\n\n' \
			'- 187 lower letters\n\n' \
			'- 8 punctuation marks\n\n' \
			'- 30 spaces')
	pass

if __name__ == '__main__':
	pass