class Account(object):

	ID_COUNT = 1

	def __init__(self, name, kwargs): 
		self.id = self.ID_COUNT
		self.name = name 
		self.__dict__.update(kwargs) 
		if hasattr(kwargs, 'value'):
			self.value = 0 
		Account.ID_COUNT += 1

	def transfer(self, amount): 
		self.value += amount
