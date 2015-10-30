__author__ = 'Nick'

from datetime import datetime
import sys
import os
sys.path.append( os.getcwd() )
from item import *
from store_inventory import *

a = item("apple",1.49, datetime.now(),20 )
b = item("cake",6.99, datetime.now(),5 )
dict = {"apple":a, "cake":b }

temp = inventory()
temp.save_inventory(dict)

for t in dict.values():
    print(t.name(), t.price(), t.exp_date(), t.quantity())