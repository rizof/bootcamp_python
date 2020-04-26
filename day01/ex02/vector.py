import sys

class Vector(object):
	"""The vector class u can add vector with a size or attribute"""

	def __init__(self, value):

		if isinstance(value, list) and isinstance(value[0], float):
			for i in value: 
				if not isinstance(i, float):
					warning_usage()
					exit()
			self.value = value

		if isinstance(value, int):
			self.value = []
			i = 0
			while i != value:
				self.value.append(float(i))
				if value > 0:
					i += 1
				else:
					i -= 1

		if isinstance(value, tuple):
			if len(value) == 2:
				print("ok")
				n1 = value[0]
				n2 = value[1]
				self.value = []
				while n1 != n2:
					self.value.append(float(n1))
					if n1 < n2:
						n1 += 1
					else:
						n1 -= 1
			else:
				warning_usage()
		self.size = len(self.value)

	def warning_usage():
		print("Vector usage u have choice: \
		 _all value float in list. (Vector[0.1, 0.2, 10.3])\
		 _size (Vector(3) = Vector(0.0, 0.1, 0.2) \
		 _range Vector(5,8) = Vector(5.0, 6.0, 7.0, 8.0))")
		pass


	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new = Vector(self.size)
			i = 0
			print('e')		
			while i < self.size:
				new.value[i] = self.value[i] + other
				i += 1
			return new
		else:
			print("Error scalaire is int or float")
			return False


	def __radd__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] + other
				i += 1
			return new
		else:
			print("Error scalaire is int or float")
			return False

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] - other
				i += 1
			return new
		else:
			print("Error scalaire is int or float")
			return False

	def __rsub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] + other
				i += 1
			return new
		else:
			print("Error scalaire is int or float")
			return False

	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float) and other != 0:
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] + other
				i += 1
			return new
		else:
			print("Error scalaire is int or float and not 0")
			return False

	def __rtruediv__(self, other):
		if isinstance(other, int) or isinstance(other, float) and other != 0:
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] + other
				i += 1
			return new
		else:
			print("Error scalaire is int or float and not 0")
			return False

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float) and other != 0:
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] * other
				i += 1
			return new
		else:
			print("Error scalaire is int or float and not 0")
			return False

	def __rmul__(self, other):
		if isinstance(other, int) or isinstance(other, float) and other != 0:
			print('e')
			new = Vector(self.size)
			i = 0
			while i < self.size:
				new.value[i] = self.value[i] * other
				i += 1
			return new
		else:
			print("Error scalaire is int or float and not 0")
			return False

	def __str__(self, other):
		print("value is {} and size is {}".format(self.value, self.size))

	def __repr__(self, other):
		return "value is {} and size is {}".format(self.value, self.size)

