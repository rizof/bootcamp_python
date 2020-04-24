import sys

def reverses_case_word(tab):
	tab3 = []
	for i in tab:
		st = list(i)
		tab2 = []
		for i2 in st:
			if (i2.isalpha()):
				tab2.append(chr(ord(i2) + 32) if i2.isupper() else \
				chr(ord(i2) - 32))
			else :	
				tab2.append(i2)
		tab3.append("".join(tab2))
	return tab3

if __name__ == '__main__' :
	arg = sys.argv
	print(" ".join(reverses_case_word(arg[1::]))[::-1], end="\n")
