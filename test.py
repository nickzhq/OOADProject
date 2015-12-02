__author__ = 'Nick'

#from datetime import datetime
import sys
import os
sys.path.append( os.getcwd() )
from item import *
from store_inventory import *
from account_manager import *
'''
# for test item
a = item("apple",1.49, 1, 2, 20 )
b = item("cake",6.99, 4.85, 9, 5 )
inventory().add("001", a)
inventory().add("002", b)
#inventory().delete("apple")
inventory().modify( 'apple',   saleprice = 333333333333 ,month =10)

# for test store_inventory
# save
inventory().save_inventory()
# load
dict = inventory().load_inventory()
inventory().search('003')

for t in dict.values():
    print(t)
'''
inventory().load_user()
print(inventory().user_dict)



