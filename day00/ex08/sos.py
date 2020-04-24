import sys
import string

tab_morse = {
	'A' : '.-', 'B' : '-...', 'C' : '-.-.',
	'D'	: '-..', 'E' : '.' , 'F' : '..-.',
	'G'	: '--.', 'H' : '....', 'I' : '..',
	'J'	: '.---', 'K' : '-.-', 'L' : '.-..',
	'M'	: '--',  'N' : '-.', 'O' : '---',
	'P'	: '.--.', 'Q' : '--.-', 'R'	: '.-.',
	'S'	: '...', 'T' : '-', 'U'	: '..-',
	'V'	: '...-', 'W' : '.--', 'X' : '-..-',
	'Y'	: '-.--', 'Z' : '--..', '0' : '-----',
	'1'	: '.----', '2' : '..---', '3' : '...--',
	'4'	: '....-', '5' : '.....', '6' : '-....',
	'7'	: '--...', '8' : '---..', '9' : '----.',
	' ' : '/'}

def uncode_morse(s, space):
	if space == 2:
		for i in s:
			print(tab_morse[i.upper()], end=" ")
	else:
		i = 0
		while i < len(s):
			if i + 1 == len(s):
				print(tab_morse[s[i].upper()])
			else:
				print(tab_morse[s[i].upper()], end=" ")
			i += 1
	pass

def parse_string(s):
	for i in list("".join(s)):
		if i in string.ascii_letters or i in string.digits or i in string.whitespace:
			continue
		else:
			return (False)
	pass

if __name__ == "__main__":
	args = sys.argv
	warning = 0
	for i in args[1::]:
		if (parse_string(i) == False):
			warning = 1
	if warning == 1:
		print("ERROR")
	else:
		i = 1
		while i < len(args):
			if i + 1 == len(args):
				uncode_morse("".join(args[i]), 1)
			else:
				uncode_morse("".join(args[i]), 2)
				print('/', end=' ')
			i += 1

