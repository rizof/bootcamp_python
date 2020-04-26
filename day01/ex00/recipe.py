import re
import sys

def represents_int(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

class Recipe(object):
	"""creation de recette, name, cooking_lvl, \
	Cooking_time, ingredients, description, and recipe_type"""
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if type(name) == str and name:
			self.name = name
		else:
			print("error name is a string and he is can't empty")
			sys.exit()
		if  represents_int(cooking_lvl) and str(cooking_lvl) in r'[12345]':
			self.cooking_lvl = cooking_lvl
		else:
			print("cooking_lvl (int) : range 1 to 5")
			sys.exit()
		if represents_int(cooking_time) and int(cooking_time) >= 0:
			self.cooking_time = cooking_time
		else:
			print("error cooking_time is int and not negatif")
			sys.exit()
		if type(ingredients) == list:
			self.ingredients = ingredients
		else:
			print("error ingredients is a list")
			sys.exit()
		self.description = description
		if recipe_type in ["starter", "lunch", "dessert"]:
			self.recipe_type = recipe_type
		else:
			print("Error recipe_type choice is: starter, lunch or dessert")
			sys.exit()

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = "name recipe: {}, cooking leve: {}, cooking_time: {}, " \
			"ingredients: {}, description {}, recipe type: {}" \
			.format(self.name, self.cooking_lvl, self.cooking_time, \
				self.ingredients, self.description, self.recipe_type)
		"""Your code goes here"""
		return txt
