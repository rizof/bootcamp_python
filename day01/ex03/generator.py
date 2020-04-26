import time

def generator(text, sep="",option=False):
	if isinstance(text, str) and text:
		if option == False or option == "unique":
			for i in text.split():
				yield i
		if option == "ordered":
			for i in sorted(text.split()):
				yield i
		if option == "shuffle":
			tab = {}
			i2 = 1
			tab2 = text.split()
			for i in tab2:
				while i2 < len(text):
					if not ord(i[0]) * time.time() % i2  in tab:
						tab[i] = ord(i[0]) * time.time() % i2
						break
					else:
						i2 += 1
			for i in (sorted(tab2, key=tab.__getitem__)):
				yield i
	else:
		print("error")


if __name__ == '__main__':
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep="", option="shuffle"):
		print(word)