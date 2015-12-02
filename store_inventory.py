import pickle
import os
import sys
sys.path.append( os.getcwd() )
#from singleton import *
import singleton

# make this class to a singleton using decorator
# this class will has an unique instance ( singleton pattern )
@singleton.singleton
class inventory:
	# for item inventory
	dict = {}
	# for user inventory
	user_dict = {}

	def load_inventory(self):
		with open("inventory.txt",'br') as f:
			inventory().dict = pickle.load(f)
			return inventory().dict

	def save_inventory( self ):
		with open("inventory.txt",'bw') as f:
			pickle.dump(inventory().dict,f)

	def add(self,barcode ,new_item ):
		if( barcode not in inventory().dict.keys()):
			inventory().dict.update({barcode:new_item})
		else:
			print("Failed! This number already exists!")

	def delete(self, info):
		for temp in inventory().dict.keys():
			if( info == inventory().dict[temp].name or info == temp ):
				del inventory().dict[temp]
				inventory().save_inventory()
		print("Failed! This item doesn't exist!")
	def sale(self,name):
		for temp in inventory().dict.keys():
			if( temp == name or inventory().dict[temp].name == name ):
				inventory().dict[temp].quantity -= 1
				print(inventory().dict[temp])
				inventory().save_inventory()
				return (inventory().dict[temp])
	# using barcode or name to change information
	# just change a kind of information in line
	def modify(self, item , saleprice = None,original_price = None  ,month = None, quantity = None ):
		for temp in inventory().dict.keys():
			if( temp == item or inventory().dict[temp].name == item ):
				if ( saleprice != None ):
					inventory().dict[temp].saleprice = saleprice
				if( original_price != None ):
					inventory().dict[temp].original_price = original_price
				if( month != None ):
					inventory().dict[temp].month = month
				if( quantity != None ):
					inventory().dict[temp].quantity = quantity
				inventory().save_inventory()
				break

	def search(self, item ):
		for temp in inventory().dict.keys():
			if( temp == item or inventory().dict[temp].name == item ):
				print(inventory().dict[temp])
				return (inventory().dict[temp])
		print("Not found!")

	# user store
	def load_user(self):
		try:
			with open("user_inventory.txt",'br') as f:
				inventory().user_dict = pickle.load(f)
				return inventory().user_dict
		except FileNotFoundError:
			with open("user_inventory.txt",'bw') as f:
				pass

	def save_user(self):
		with open("user_inventory.txt",'bw') as f:
			pickle.dump(inventory().user_dict, f )

	def add_user(self, username, new_user):
		if( username not in inventory().user_dict.keys()):
			inventory().user_dict.update({username:new_user})
		else:
			print("Failed to add user!")

	def delete_user(self, info ):
		for temp in inventory().user_dict.keys():
			if( info == temp ):
				del inventory().user_dict[info]
				return
		print("Failed! This number doesn't exist!")

	def modify_user(self, username, password = None, salary = None):
		for temp in inventory().user_dict.keys():
			if( temp == username ):
				if ( password != None ):
					inventory().user_dict[temp].password = password
				if( salary != None ):
					inventory().user_dict[temp].salary = salary
				break

	def search_user(self, username):
		for temp in inventory().user_dict.keys():
			if( temp == username ):
				print( inventory().user_dict[temp] )
				return inventory().user_dict[temp]
		print("Not found!")
'''
user = inventory().load_user()
for i in user.keys():
	print( i+"   " + user[i].password )
'''

inventory().load_inventory()
#inventory().sale("cake")
m = inventory().load_inventory()
for i in m.keys():
	print(m[i])

'''
11  111  manager
33  33   employee
'''