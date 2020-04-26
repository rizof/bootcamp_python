from vector import Vector

if __name__ == '__main__':
	test = Vector([0.2, 0.2, 0.5])
	test1 = Vector(10)
	test2 = Vector(-5)
	test3 = Vector((10, 15))
	test4 = 20 / test2

	print(test4.value)
	print(test.value)
	print(test.size)
	print(test1.value)
	print(test1.size)
	print(test2.value)
	print(test2.size)
	print(test3.value)
	print(test3.size)