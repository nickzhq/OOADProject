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
	dict = {}

	def load_inventory(self):
		with open("inventory.txt",'br') as f:
			try:
				dict = pickle.load(f)
			except Exception as e:
				print( type(e) )
				print( e.args )
				print( e )

		return inventory.dict

	def save_inventory( self, temp_dict ):
		with open("inventory.txt",'bw') as f:
			try:
				pickle.dump(temp_dict,f)
			except Exception as e:
				print( type(e) )
				print( e.args )
				print( e )