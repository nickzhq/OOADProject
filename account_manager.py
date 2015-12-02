__author__ = 'Nick'

import sys
import os
sys.path.append( os.getcwd() )
from user import *
from store_inventory import *
from singleton import *

class account:
    def create(self, account_user,name,code):
        #account_user = input("Which user would want to create? \n1. Manager \n2. Employee\n")
        #name = input("Create the username: ")
       # code = input("Create the password: ")
        '''temp = inventory()
        try:
            temp.load_user()

            # create the manager
            if( int(account_user) == 1):
                new_user = manager( name, code )
                temp.add_user(name, new_user)
            elif( int(account_user) == 2):
                new_user = employee( name, code )
                temp.add_user(name, new_user)

        except FileNotFoundError:
            if( int(account_user) == 1):
                new_manager = manager( name, code )
                temp.add_user(name, new_manager)
            elif( int(account_user) == 2):
                new_employee = employee( name, code )
                temp.add_user(name, new_employee)
        except Exception as e:
            print( type(e) )
            print( e.args )
            print( e )
        finally:
            temp.save_user()'''
        try:
            # create the manager
            if( int(account_user) == 1):
                new_user = manager( name, code )
                inventory().add_user(name, new_user)
            elif( int(account_user) == 2):
                new_user = employee( name, code )
                inventory().add_user(name, new_user)

            inventory().save_user()
        except FileNotFoundError:
            if( int(account_user) == 1):
                new_manager = manager( name, code )
                inventory().add_user(name, new_manager)
            elif( int(account_user) == 2):
                new_employee = employee( name, code )
                inventory().add_user(name, new_employee)
        except Exception as e:
            print( type(e) )
            print( e.args )
            print( e )

    def  modify(self, username ):
        temp = input("Which would you want to modify?\n 1.password\n2.salary\n")
        if( int(temp) == 1 ):
            new_pass = input("Type your new password:")
            confirm = input("Type your new password again:")
            if( new_pass == confirm ):
                inventory().modify_user( username, password = new_pass )
            else:
                print("These passwords are NOT same!")

    def delete(self,username):
        if username in inventory().user_dict.keys():
            inventory().delete_user(username)
'''
x = account()
#x.create()
print(inventory().user_dict)
'''