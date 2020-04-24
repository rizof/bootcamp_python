import sys

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
	arg = sys.argv
	if len(arg) != 1:
		if ((len(arg) != 2)):
			print("ERROR")
		elif (represents_int(arg[1])):
			if (int(arg[1]) == 0):
				print("I'm Zero.")
			elif (int(arg[1]) % 2):
				print("I'm Odd.")
			else :
				print("I'm Even.")
		else:
			print("ERROR")