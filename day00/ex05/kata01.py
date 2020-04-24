import sys

if __name__ == '__main__':
	languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

	for key in languages:
		print(key, 'was created by', languages[key])