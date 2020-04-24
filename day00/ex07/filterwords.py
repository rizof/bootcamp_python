import sys
import re
import string

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def filterword(s, filter):
	tab_temp = s.split()
	tab_str = []
	for i in tab_temp:
		i = i.strip(string.punctuation)
		if len(i) >= int(filter) :
			tab_str.append(i)
	print(tab_str) 

if __name__ == "__main__":
	av = sys.argv
	if len(av) == 3:
		if (re.match("[a-zA-Z]+", av[1]) and represents_int(av[2])):
			filterword(av[1], av[2])
		else:
			print("ERROR")
	else:
		print("ERROR")
