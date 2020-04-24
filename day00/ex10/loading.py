from time import sleep
import time
import sys

def ft_progress(lst):
	percentage = 0
	eta = 0
	bar = 1
	for i in lst:
		if i != 0:
			percentage = i*100 / len(lst)
			bar = int(((percentage*10) / 100))
			if bar == 0:
				bar = 1
		else:
			seconds = time.time()
		elapsed = time.time() - seconds
		if i != 0 :
			eta = (elapsed * (len(lst) / i)) - elapsed
		print("\rETA: %.2fs [%3d%%][%-9s] %d/%d | elapsed time %.2fs" % \
			(eta, int(percentage), '='* bar, i, len(lst), float(elapsed)), \
			end="")
		yield i
		print("\rETA: 0,00s [100%%][%s%s] %d/%d | elapsed time %.2fs" % \
			('='* bar,'>', len(lst), len(lst), float(elapsed)), end="")
	pass

if __name__ == '__main__':
	pass