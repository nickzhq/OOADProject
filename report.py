__author__ = 'Nick'

import sys
import os
sys.path.append( os.getcwd() )
from item import *
from store_inventory import *
import singleton

@singleton.singleton
class report:
    def __init__(self):
        pass

    def viewState(self):
        '''
        dict = inventory().load_inventory()
       # dict = inventory.__inventory__.dict
        for i,j in dict.items():
            print( i ," : ", j )

        # return items in inventory
        '''
        return inventory().load_inventory()

    def state_report(self):
        pass
    def profit_report(self):
        pass