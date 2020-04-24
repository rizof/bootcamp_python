import sys

def numeric_string(s1, s2):
	try:
		int(s1)
		int(s2)
		return True
	except ValueError :
		return False

def calulator(n1, n2):
	print('Sum:         {}\n' \
		'Difference:  {}\n' \
		'Product:     {}'.format(n1 + n2, n1 - n2, n1 * n2))
	if (n1 == 0 or n2 == 0) :
		print('Quotient:    ERROR (div by zero)\n' \
			'Remainder:   ERROR (modulo by zero)')
	else:
		print('Quotient:    {}\n' \
			'Remainder:   {}'.format(n1 / n2, n1 % n2))

if __name__ == "__main__":
	x = ('Usage: python operations.py <number1> <number2>\n' \
			'Example:\n'\
		    '    python operations.py 10 3')
	argvs = sys.argv
	if (len(argvs) < 3):
		print(x)
	elif len(argvs) > 3:
		print('InputError: too many arguments\n\n' \
			'{}'.format(x))
	elif numeric_string(argvs[1], argvs[2]):
		calulator(int(argvs[1]), int(argvs[2]))
	else:
		print('InputError: only numbers\n\n' \
			'{}'.format(x))