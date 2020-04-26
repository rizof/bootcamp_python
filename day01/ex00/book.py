import datetime
from recipe import Recipe
class Book(object):
	"""docstring for Book"""
	def __init__(self, name):
		if type(name) == str and name:
			self.name = name
		else:
			print("error name is a string and he is can't empty")			
		self.creation_date = datetime.datetime.now()
		self.last_update = datetime.datetime.now()
		self.recipes_list = {"starter" : {}, "lunch": {}, "dessert": {}}
		pass

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for k, v in self.recipe_type:
			if name in v:
				print(v)
		pass

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if recipe_type in ["starter", "lunch", "dessert"]:
			for v, k in self.recipes_list[recipe_type].items():
				print(k)
		pass

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if isinstance(recipe, Recipe):
			self.last_update = datetime.datetime.now()
			if recipe.recipe_type and recipe.name:
				self.recipes_list[recipe.recipe_type][recipe.name] = recipe
		pass