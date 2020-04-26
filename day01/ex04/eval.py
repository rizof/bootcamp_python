class Evaluator(object):
	"""The lists coefs and words have to be the \
		same length. If this is not the case, \
		the function should return -1."""
	@staticmethod
	def zip_evaluate(coef, word):
		if isinstance(word, list) and isinstance(coef, list):
			if Evaluator.enumerate_evaluate(coef, word):
				return -1
			else:
				tab = list(zip(coef, word))
				result = 0
				for i in tab:
					result += i[0]*len(i[1])
				return result
		else:
			return "usage: (list coef), (list word)"
		pass
		
	@staticmethod
	def enumerate_evaluate(coef, word):
		if isinstance(word, list) and isinstance(coef, list):
			if list(enumerate(word))[-1][0] != list(enumerate(coef))[-1][0]:
				return -1
		else:
			return "usage: (list coef), (list word)"
		pass

if __name__ == '__main__':
	words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	Evaluator.enumerate_evaluate(coefs, words)
	Evaluator.zip_evaluate(coefs, words)
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	Evaluator.enumerate_evaluate(coefs, words)
	Evaluator.zip_evaluate(coefs, words)