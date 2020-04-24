import sys
from random import randint

def menu():
	print("This is an interactive guessing game!\n" \
		"You have to enter a number between 1 and 99 to find out" \
		"the secret number.\nType 'exit' to end the game.\n"\
		"Good luck!")
	pass

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def play_game(stop):
	stop = 0
	i = 1
	while stop != 1:
		print("What s your guess between 1 and 99?")
		your_numb = input()
		if your_numb == 'exit':
			stop = 1
		elif represents_int(your_numb) :
			if int(your_numb) == numb_rand :
				if i == 1:
					print("Congratulations!" \
						"You got it on your first try!")
				elif int(your_numb) == 42:
					print("The answer to the ultimate question of life," \
					"the universe and everything is 42.")
				else:
					print("Congratulations, you ve got it!\n" \
						"You won in {} attempts!".format(i))
				break
			else :
				print("Too high!") if int(your_numb) > numb_rand else \
				print("Too low!")
			i += 1
		else :
			print("error print number")
	return(stop)

if __name__ == "__main__":
	stop = 0
	while stop != 1 :
		numb_rand = randint(1, 99)
		stop = play_game(stop)
	print("Goodbye!")