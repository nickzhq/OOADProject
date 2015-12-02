__author__ = 'Nick'

import sys
import os
sys.path.append( os.getcwd() )
from report import *
from store_inventory import *
from account_manager import *
from item import *
from user import *

class menu:
    __current_user = None

    def login(self, name, code):
       # name = input("Please type the username:")
        #code = input("Please type the password:")

        # check the user
        if( menu.__current_user == None ):
            inventory().load_user()
            for temp in inventory().user_dict.keys():
                if ( name == temp ):
                    if( code  == inventory().user_dict[temp].password ):
                        menu.__current_user = inventory().user_dict[temp]
                        #print ("Login successfully")
                        return True
            #print("Login failed")
            return False
        else:
            #print("Please logout first!")
            return False

    def logout(self):
        menu.__current_user = None
        #print("logout successfully")
        # return ("logout successfully")
        return True

    def store_management_add( self,name,saleprice,original_price,month,quantity ):
        new_item = item(name, float(saleprice), float(original_price), int(month), int(quantity))
        inventory().add(barcode, new_item)
    def store_management_delete(self,name):
        inventory().delete(name)
    def store_management_modify(self):
        pass
    def store_management_search(self,name):
        if ( isinstance( menu.__current_user, manager ) or isinstance( menu.__current_user, employee ) ):
            result = inventory().search(name)
            return result
    def store_management_sale(self,name):
        if ( isinstance( menu.__current_user, manager ) or isinstance( menu.__current_user, employee ) ):
            result = inventory().sale(name)
            return result
        else:
            print("Sale operation failed!")
    def store_management(self):
        if (  isinstance( menu.__current_user, employee ) ):
            return ("No authorised!")
        elif ( isinstance( menu.__current_user, manager ) ):
            # choose = input("what would you want do?\n1.add item\n2.delete item\n3.modify item\n4.search item\n5.sale")
            try:
                # add
                if (int(choose) == 1):
                    barcode = input("Please type the barcode:")
                    name = input("Please type the name:")
                    saleprice = input("Please type the sale price(number only):")
                    original_price = input("Please type the original price(number only):")
                    month = input("Please type the month for when the item is stored( from 1 ~ 12):")
                    quantity = input("Please type the quantity(number only):")
                    new_item = item(name, float(saleprice), float(original_price), int(month), int(quantity))
                    inventory().add(barcode, new_item)

                # delete
                elif (int(choose) == 2):
                    name = input("Please type the barcode or name of item you want to delete:")
                    inventory().delete(name)

                # modify
                elif (int(choose) == 3):
                    name_mod = input("Please item the barcode or name you want to modify:")
                    sel = input("Which part would you want to modify?")
                    pass
                # search
                elif (int(choose) == 4):
                    name = input("Please type barcode or name you want to search:")
                    item = inventory().search(name)
                    print(item)
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)

    def account_management_create(self,account_user,name,code):
        if( isinstance(menu.__current_user, manager) ):
            temp = account()
            inventory().load_user()
            try:
                    temp.create(account_user,name,code)
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)

    def report(self):
        return report().viewState()
'''
m = menu()
m.login()
m.store_management()
'''


