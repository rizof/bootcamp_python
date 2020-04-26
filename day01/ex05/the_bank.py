import re
from account import Account

class Bank(object):
	"""The bank"""
	def __init__(self): 
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest:    int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return         True if success, False if an error occured
		"""
		print(self.account[0].value)

		for i in self.account:
			if i.name == origin:
				origin = i
			if i.name == dest:
				dest = i
		if isinstance(origin, Account) and isinstance(dest, Account):
			if origin.value >= amount and isinstance(amount, float):
				dest.value += amount
				origin.value -= amount
			else:
				print("u dont have the sold in u account or tape float amount")
				return False
		else:
			print("Error name account")
			return False

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""
		for i in self.account:
			if i.name == account:
				account = i
		if isinstance(account, Account)
			control_attr = 0
			attribute = re.sub('__\w+', "", (" ".join(dir(account)))).split()

			if len(attribute) % 2:
				for i in attribute:
					if i in ["ID_COUNT", "id", "name", "zip", "ref", "value", "addr"]:
						control_attr += 1
			else:
				print("u dont have even attribut")
				return False

			if control_attr < 6:
				print("u dont have essential attribute")
				return False
			return True
		else:
			return False

