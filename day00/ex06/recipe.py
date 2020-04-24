import sys

def init_cook():
	recipe = {"cookbook" : 
	{	
		"cake" : {
			"ingredients" : ["flour", "sugar", "eggs"],
			"meal" : "dessert",
			"prep_time" : "60"
		},
		"sandwich" : {
			"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
			"meal" : "lunch",
			"prep_time" : "10"
		},
		"salad" : {
			"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
			"meal" : "lunch",
			"prep_time" : "15"
		},
	}, }
	return recipe

def add_recipe(recipe):
	print("What name recipe u want add ?")
	name = input()
	recipe["cookbook"][name] = {}
	print("What name ingredients u want add ?")
	name1 = input()
	recipe["cookbook"][name]["ingredients"] = list(name1.split(" "))
	print("What name cookbook u want add ?")
	name1 = input()
	recipe["cookbook"][name]["meal"] = name1
	print("What name preparation time u want add ?")
	name1 = input()
	recipe["cookbook"][name]["prep_time"] = name1


def delete_recipe(name_recipe, recipe):
	print("\nthe {} is delete!\n\n".format(name_recipe))
	recipe["cookbook"].pop(name_recipe)


def print_recipe(name_recipe, recipe):
	print("Recipe for {}: \nIngredients list: {}\nTo be eaten for {}.\n"\
		"and it takes {}."\
		.format(name_recipe, recipe["cookbook"][name_recipe]["ingredients"],\
		recipe["cookbook"][name_recipe]["meal"],\
		recipe["cookbook"][name_recipe]["prep_time"]))

def while_menu(recipe, index, str=""):
	print(str)
	i = 1 
	while i != 0:
		if index == 1:
			add_recipe(recipe)
			i = 0
		else:
			print_cookbook(recipe)
		name_recipe = input()
		if name_recipe in recipe["cookbook"]:
			if index == 2:
				delete_recipe(name_recipe, recipe)
			elif index == 3:
				print_recipe(name_recipe, recipe)
			i = 0
			print_menu()
		elif name_recipe == "0":
			i = 0
			print_menu()
		else:
			print("We dont have {} if u want exit tape 0 else we have: \n" \
				.format(name_recipe))

def print_cookbook(recipe):
	for items in recipe["cookbook"]:
		print(items)

def print_menu():
	print('Please select an option by typing the corresponding number:\n' \
			'1: Add a recipe\n' \
			'2: Delete a recipe\n' \
			'3: Print a recipe\n' \
			'4: Print the cookbook\n' \
			'5: Quit')

if __name__ == "__main__":
	recipe = init_cook()
	i = 1
	print_menu()
	while i != 0:
		answer = input()
		if answer == '5':
			i = 0
			print("cookbook closed.")
		elif answer == '4':
			print_cookbook(recipe)
		elif answer == "3":
			while_menu(recipe, 3, \
				"Please enter the recipe's name to get its details:")
		elif answer == "2":
			while_menu(recipe, 2, "Whats recipe u want delete?")
		elif answer == "1":
			while_menu(recipe, 1)
		else:
			print('This option does not exist, please type the corresponding' \
				'number.\nTo exit, enter 5.')