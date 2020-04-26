from book import Book
from recipe import Recipe

if __name__ == '__main__':
	rec = Recipe("pizza", 2, 30, ["tomatos","cheese", "oignon"], \
		"", "lunch")
	to_print = str(rec)
	print(to_print)
	book = Book("pizza_book")
	book.add_recipe(rec)
	book.get_recipes_by_types("lunch")